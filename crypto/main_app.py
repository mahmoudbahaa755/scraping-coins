import my_function as fn
import boost as bs


tickers = [["ETCUSDT", "ETHUSDT"], ["LTCUSDT", "XRPUSDT"], ["XEMUSDT", "PNTUSDT"]]

def get_crypto_data():
    
    x=bs.boost(fn.get_asset_data, tickers, "4h", "24 hours ago UTC+1")
    print(x)

get_crypto_data()