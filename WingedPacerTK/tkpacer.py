
import tkinter as tki
from tkinter import ttk


pacer = tki.Tk()
pacer.title('PACER')
pacer.geometry('240x180+400+350')

lb_question = tki.Label(pacer, text='Ты сделал то, что собирался?', pady=30)
lb_question.pack()

bt_frame = tki.Frame(pacer)
bt_frame.pack()

def approve(): lb_response.configure(text='Молодец, так держать!')
def disapprove(): lb_response.configure(text='Так делай, чего откладывать!')

bt_yes = tki.Button(bt_frame, text='Да', padx=10, command=approve)
bt_no = tki.Button(bt_frame, text='Нет', padx=7, command=disapprove)
bt_yes.pack(side='left', padx=10)
bt_no.pack(side='right', padx=10)

lb_response = tki.Label(pacer, text='Признавайся, не таясь!', pady=30)
lb_response.pack()





pacer.mainloop()


