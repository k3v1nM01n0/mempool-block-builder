# mempool-block-builder

This is a tool that constructs a valid block from transactions in a mempool CSV file, outputing the txids.

## Requirements
- Python 3.x

## Installation
1. Clone the repository: `git clone <repository-url>`
2. Navigate to the repository directory: `cd mempool-block-constructor`

## Usage
1. Place your mempool.csv file in the repository directory.
2. Run the program with Python:

```bash
python main.py
```

## CSV Format
The mempool CSV file should follow this format:

- `<txid>`: Transaction identifier
- `<fee>`: Transaction fee
- `<weight>`: Transaction weight
- `<parent_txids>`: List of immediate parent transactions' txids separated by semicolons

## Example
An example mempool.csv file and a block sample are provided for demonstration.

## License
This project is licensed under the [MIT License](LICENSE).
