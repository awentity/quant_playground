from pathlib import Path

import pandas as pd

def read_csv(filepath: Path):
    panda_data = pd.read_csv(filepath, index_col=0, parse_dates=True, sep=";")
    return panda_data

if __name__ == "__main__":
    csv_panda = read_csv(Path("../data/Ethereum_13_11_2023-12_11_2024_historical_data_coinmarketcap.csv"))
    print(csv_panda.info())
    csv_panda["SMA"] = csv_panda["open"].rolling(100).mean()
    figure = csv_panda.filter(items=["SMA", "open"]).loc['2023-11-21T00:00:00.000Z':].plot(title='ETH/USD exchange rate', figsize=(10, 6))
    figure.get_figure().savefig("eth_usd.pdf")