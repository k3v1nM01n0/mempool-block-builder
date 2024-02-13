import csv

class Transaction:
    def __init__(self, txid, fee, weight, parent_txids):
        self.txid = txid
        self.fee = int(fee)
        self.weight = int(weight)
        self.parent_txids = parent_txids.split(';') if parent_txids else []
        self.children = []

def parse_mempool_csv(file_path):
    transactions = {}
    with open(file_path, 'r') as file:
        for line in file:
            row = line.strip().split(',')  # Split each row by comma
            if len(row) == 4:
                txid, fee, weight, parent_txids = row
                parent_txids = parent_txids.replace('"', '')  # Remove double quotes
                transactions[txid] = Transaction(txid, fee, weight, parent_txids)
            else:
                print(f"Ignoring invalid row: {row}")
    return transactions

def construct_block(transactions):
    block = []
    block_weight = 0
    for txid in sorted(transactions.keys(), key=lambda x: transactions[x].fee, reverse=True):
        transaction = transactions[txid]
        parent_tx_not_in_block = [parent_txid for parent_txid in transaction.parent_txids if parent_txid not in block]
        if not parent_tx_not_in_block and txid not in block and block_weight + transaction.weight <= 4000000:
            block.append(txid)
            block_weight += transaction.weight
    return block

def main():
    transactions = parse_mempool_csv('mempool.csv')
    print(f"Number of transactions parsed: {len(transactions)}")
    block = construct_block(transactions)
    print(f"Number of transactions in the block: {len(block)}")
    for txid in block:
        print(txid)

if __name__ == "__main__":
    main()

