from pandastable import Table
import pandas as pd
from tkinter import *

df = pd.DataFrame(pd.read_csv('gui\\training\\AAPL (1).csv'))


class Show_Historical_Data:

    def __init__(self, main_frame):
        for widget in main_frame.winfo_children():
            widget.destroy()

        self.frame = Frame(main_frame)
        self.frame.pack(padx=10, pady=10)


        self.table = Table(self.frame, dataframe=df)
        self.table.show()