
import tkinter as tki
from tkinter import ttk


pacer = tki.Tk()
pacer.title('PACER')
pacer.geometry('240x180+200+250')

lb_greeting = tki.Label(pacer, text='Здравствуй! Ну, что, ты готов?', pady=30)
lb_greeting.pack()

def question_window():
    if 'w_question' in pacer.children:
        pacer.children['bt_question'].config(relief='raised')
        pacer.children['w_question'].destroy()
        return

    pacer.children['bt_question'].config(relief='sunken')
    w_question = tki.Toplevel(pacer, name='w_question')
    w_question.geometry('240x180+400+350')
    w_question.transient(pacer)
    w_question.focus()

    def w_question_rip():
        w_question.destroy()
        pacer.children['bt_question'].config(relief='raised')
    w_question.protocol('WM_DELETE_WINDOW', w_question_rip)

    lb_question = tki.Label(w_question, text='Ты сделал то, что собирался?', pady=30)
    lb_question.pack()

    frm_buttons = tki.Frame(w_question)
    frm_buttons.pack()

    def approve():
        if bt_yes.cget('relief') == 'sunken':
            lb_response.config(text='Признавайся, не таясь!')
            bt_yes.config(relief='raised')
        else:
            lb_response.config(text='Молодец, так держать!')
            bt_yes.config(relief='sunken')
            bt_no.config(relief='raised')
    def disapprove():
        if bt_no.cget('relief') == 'sunken':
            lb_response.config(text='Признавайся, не таясь!')
            bt_no.config(relief='raised')
        else:
            lb_response.configure(text='Так делай, чего откладывать!')
            bt_no.config(relief='sunken')
            bt_yes.config(relief='raised')

    bt_yes = tki.Button(frm_buttons, text='Да', padx=10, command=approve)
    bt_no = tki.Button(frm_buttons, text='Нет', padx=7, command=disapprove)
    bt_yes.pack(side='left', padx=10)
    bt_no.pack(side='right', padx=10)

    lb_response = tki.Label(w_question, text='Признавайся, не таясь!', pady=30)
    lb_response.pack()

bt_question = tki.Button(pacer, name='bt_question', text='Отчитаться',
                         command=question_window)
bt_question.pack()



pacer.mainloop()


