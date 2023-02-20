from os import path
from tkinter import filedialog
from platform import system
from yfinance import download

import eel
import tkinter


@eel.expose
def fetch(ticker, start_date, end_date, frequency):
    try:
        if _platform == "Darwin":
            tk.deiconify()
            tk.update()
        destination = filedialog.askdirectory(parent=tk, title="選擇檔案儲存位置")
        if _platform == "Darwin":
            tk.withdraw()
            tk.update()
        eel.Alert()
        print(f'{ticker}\n{start_date} to {end_date}')
        fetch_data = download(ticker, start=start_date, end=end_date, interval=frequency)
        fetch_data.index = fetch_data.index.strftime('%Y-%m-%d')
        fetch_data.to_excel(f"{destination}/{str(ticker)}.xlsx")
        print()
    except Exception as e:
        print(e)
        print()


_platform = system()
root = path.dirname(path.realpath(__file__))

tk = tkinter.Tk()
tk.title("選擇檔案儲存位置")
tk.withdraw()
tk.wm_attributes('-topmost', 1)
if _platform == "Windows":
    tk.iconbitmap(default=f'{root}/web/favicon.ico')
tk.update()

print("*************************************************")
print()
print("                 BlueEyes Engine")
print("                 ccpl17/shd")
print()
print("*************************************************")
print()
print("程式啟動中，請耐心等候")
print()

eel.init(f'{root}/web')

eel.start('main.html', port=0)
