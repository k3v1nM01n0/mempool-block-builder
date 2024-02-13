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
        csv_reader = csv.reader(file)
        for row in csv_reader:
            txid, fee, weight, parent_txids = row
            transactions[txid] = Transaction(txid, fee, weight, parent_txids)
    return transactions

def construct_block(transactions):
    block = []
    block_weight = 0
    for txid in sorted(transactions.keys(), key=lambda x: transactions[x].fee, reverse=True):
        transaction = transactions[txid]
        if all(parent_txid in block for parent_txid in transaction.parent_txids) and \
                txid not in block and \
                block_weight + transaction.weight <= 4000000:
            block.append(txid)
            block_weight += transaction.weight
    return block

def main():
    transactions = parse_mempool_csv('mempool.csv')
    block = construct_block(transactions)
    for txid in block:
        print(txid)

if __name__ == "__main__":
    main()
