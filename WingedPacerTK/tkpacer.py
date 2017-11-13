
import tkinter as tki
import tkinter.scrolledtext as st
import tkinter.font as fnt
from tkinter import ttk


pacer = tki.Tk();    pacer.title('PACER');    pacer.geometry('242x220+200+250')

treb14 = fnt.Font(family='Trebuchet', size=13)

def Button(name, text, command, parent=pacer):
    return tki.Button(parent, name=name, text=text, command=command,
                      font=treb14, borderwidth=3)
def Label(text, parent=pacer):
    return tki.Label(parent, text=text, font=treb14)
def Label30(text, parent=pacer):
    return tki.Label(parent, text=text, font=treb14, pady=30)


Label30('Здравствуй!\nНу, что, ты готов?').pack()


def decision_window():
    if 'w_decision' in pacer.children:
        bt_decide.config(relief='raised')
        pacer.children['w_decision'].destroy();    return

    bt_decide.config(relief='sunken')
    w_decision = tki.Toplevel(pacer, name='w_decision')
    w_decision.geometry('380x250+460+140')
    w_decision.transient(pacer)
    w_decision.focus()

    def w_decision_rip():
        w_decision.destroy()
        bt_decide.config(relief='raised')
    w_decision.protocol('WM_DELETE_WINDOW', w_decision_rip)

    Label30('Что ты решил сделать?', w_decision).pack()

    frm_input = tki.Frame(w_decision)
    frm_input.pack()

    Label('Я обязуюсь', frm_input).pack(side='left', padx=3, pady=3, anchor='n')

    ntr_input = st.ScrolledText(frm_input, font=treb14)
    ntr_input.pack(side='right', padx=2, pady=4)
bt_decide = Button('bt_decide', 'Решить и Взяться', decision_window)
bt_decide.pack()

def question_window():
    if 'w_question' in pacer.children:
        bt_question.config(relief='raised')
        pacer.children['w_question'].destroy();    return

    bt_question.config(relief='sunken')
    w_question = tki.Toplevel(pacer, name='w_question')
    w_question.geometry('242x180+460+360')
    w_question.transient(pacer)
    w_question.focus()

    def w_question_rip():
        w_question.destroy()
        bt_question.config(relief='raised')
    w_question.protocol('WM_DELETE_WINDOW', w_question_rip)

    Label30('Ты сделал то, что собирался?', w_question).pack()

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

    bt_yes = Button('bt_yes', 'Да', approve, frm_buttons)
    bt_yes.config(padx=7)
    bt_yes.pack(side='left', padx=10)
    bt_no = Button('bt_no', 'Нет', disapprove, frm_buttons)
    bt_no.config(padx=3)
    bt_no.pack(side='right', padx=10)

    lb_response = Label30('Признавайся, не таясь!', w_question)
    lb_response.pack()
bt_question = Button('bt_question', 'Отчитаться', question_window)
bt_question.pack(pady=10)



pacer.mainloop()


