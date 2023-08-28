import requests
import base64


def get_transaction_data(block_number):
    url = f"https://akash-api.w3coins.io/blocks/{block_number}"

    response = requests.get(url)

    if response.status_code == 200:
        block_data = response.json()
        txs_base64 = block_data.get('block', {}).get('data', {}).get('txs', [])

        transaction_data = []

        for tx_base64 in txs_base64:
            try:
                tx_bytes = base64.b64decode(tx_base64)
                transaction_data.append(tx_bytes)
            except (base64.binascii.Error, UnicodeDecodeError):
                transaction_data.append("Error decoding transaction data")

        return transaction_data
    else:
        print("Failed to retrieve block data. Status code:", response.status_code)  # Отладочный вывод
        return None


print(f'Введите номер интересуемого блока: ')
block_number = int(input())

transactions = get_transaction_data(block_number)

if transactions is not None:
    for idx, tx in enumerate(transactions, start=1):
        print(f"Transaction {idx}:\n{tx}\n{'=' * 50}\n")
else:
    print("Sorry! empty block data.")
