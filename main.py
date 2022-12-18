import eel
from os import path
from yfinance import download

@eel.expose
def fetch(ticker, startDate, endDate, frequency):
    try:
        print("\n")
        fetch_data = download(ticker, start = startDate, end = endDate, interval = frequency)
        print(f"\n{fetch_data}")
        fetch_data.to_excel(f"{Desktop}/{str(ticker)}.xlsx")
        print("\n操作成功\n")
    except:
        print("\n操作失敗\n")

Desktop = path.normpath(path.expanduser("~/Desktop"))
root = path.dirname(path.realpath(__file__))

print("*************************************************\n\n                 BlueEyes Engine\n                 Python\n\n*************************************************\n")

eel.init(f'{root}/web')
eel.start('main.html',shutdown_delay = 1)