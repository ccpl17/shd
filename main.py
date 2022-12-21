import eel
from os import path
from yfinance import download
from tkinter import filedialog

@eel.expose
def fetch(ticker, startDate, endDate, frequency):
    try:
        print("\n")
        fetch_data = download(ticker, start = startDate, end = endDate, interval = frequency)
        print(f"\n{fetch_data}")
        destination = path.abspath(filedialog.askdirectory())
        fetch_data.to_excel(f"{destination}/{str(ticker)}.xlsx")
        print("\n操作成功\n")
    except:
        print("\n操作失敗\n")

root = path.dirname(path.realpath(__file__))

print("*************************************************\n\n                 BlueEyes Engine\n                 ccpl17/shd\n\n*************************************************\n")

eel.init(f'{root}/web')
eel.start('main.html',shutdown_delay = 1)