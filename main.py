import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import pandas as pd
import openpyxl


my_w = tk.Tk()
my_w.geometry('400x300')
my_w.title('www.plus2net.com')
my_font1=('times', 18, 'bold')
l1 = tk.Label(my_w, text='Upload SLO Files', width=30, font=my_font1)
l1.grid(row=1, column=1)
b1 = tk.Button(my_w, text='Upload Grade Sheet', width=20, command=lambda:upload_id_file())
b1.grid(row=2, column=1)
b2 = tk.Button(my_w, text='Upload Course SLO Sheet', width=20, command=lambda:upload_canvas_file())
b2.grid(row=3, column=1)
b3 = tk.Button(my_w, text='Student ID to SLO Sheet', width=20, command=lambda:coalate_files())
b3.grid(row=4, column=1)
def upload_id_file():
    global grade_sheet_df
    grade_sheet = filedialog.askopenfilename()
    grade_sheet_df=pd.read_csv(grade_sheet)
    print(grade_sheet_df)

def upload_canvas_file():
    global SLO_sheet_df
    SLO_sheet = filedialog.askopenfilename()
    SLO_sheet_df = pd.read_csv(SLO_sheet)
    print(SLO_sheet_df)
    return SLO_sheet_df

def coalate_files():
    for i in range(len(SLO_sheet_df)):
        for j in range(len(grade_sheet_df)):
            if grade_sheet_df.loc[j, 'ID'] == SLO_sheet_df.loc[i, 'Student ID']:
                SLO_sheet_df.loc[i, 'Student ID'] = grade_sheet_df.loc[j, 'SIS Login ID']
                print(j, grade_sheet_df.loc[j, 'SIS Login ID'], SLO_sheet_df.loc[i, 'Student ID'], grade_sheet_df.loc[j, 'ID'])
                print(SLO_sheet_df)
    SLO_sheet_df['Student ID'] = SLO_sheet_df['Student ID'].apply(lambda x: '{0:0>7}'.format(x))
    print(j, grade_sheet_df.loc[j, 'SIS Login ID'], SLO_sheet_df.loc[i, 'Student ID'], grade_sheet_df.loc[j, 'ID'])
    print(SLO_sheet_df)


my_w.mainloop()