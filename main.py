from os import path
from random import randint
from tkinter import filedialog
from yfinance import download

import eel

@eel.expose
def fetch(ticker, startDate, endDate, frequency):
    try:
        print("\n")
        fetch_data = download(ticker, start = startDate, end = endDate, interval = frequency)
        fetch_data.index = fetch_data.index.strftime('%Y-%m-%d')
        print(f"\n{fetch_data}")
        destination = path.abspath(filedialog.askdirectory())
        fetch_data.to_excel(f"{destination}/{str(ticker)}.xlsx")
        print("\n操作成功\n")
    except:
        print("\n操作失敗\n")

port = randint(10000,65535)

root = path.dirname(path.realpath(__file__))

print(f"*************************************************\n\n                 BlueEyes Engine\n                 ccpl17/shd\n\n*************************************************\n\n程式啟動中，請耐心等候\n\n端口號碼：{port}\n")

eel.init(f'{root}/web')

eel.start('main.html', port = port, shutdown_delay = 1)