
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
    w_decision.geometry('380x180+460+140')
    w_decision.transient(pacer)
    w_decision.title('итак...')
    w_decision.focus()

    def w_decision_rip():
        w_decision.destroy()
        bt_decide.config(relief='raised')
    w_decision.protocol('WM_DELETE_WINDOW', w_decision_rip)

    Label30('Что ты решил сделать?', w_decision).pack()

    frm_input = tki.Frame(w_decision, padx=6)
    frm_input.pack()

    subfrm_input = tki.Frame(frm_input)
    subfrm_input.pack(side='left')

    Label('Я обязуюсь', subfrm_input).pack(side='top', padx=3, anchor='e')


    ntr_input = st.ScrolledText(frm_input, font=treb14, padx=5, pady=2, height=4,
                                wrap='word')
    ntr_input.insert('1.0', decision)
    ntr_input.pack(side='right')

    def set_goal(_=None):
        global decision
        new_decision = ntr_input.get('1.0', 'end-1c').strip().strip('.')
        if new_decision and new_decision != decision and 'w_question' in pacer.children:
            pacer.children['w_question'].children['!label'].config(text='Ты обещал\n'+
                                                            new_decision+ '.\nСправился?')
        decision = new_decision
        if decision:    bt_question.config(state='normal', borderwidth=3)
        else:
            bt_question.config(state='disabled', borderwidth=1)
            if 'w_question' in pacer.children:
                pacer.children['w_question'].destroy()
                bt_question.config(relief='raised')
        with open('userdata.txt', 'w', encoding='utf-8') as file:
            file.write(decision)
        return 'break'

    ntr_input.bind('<Control-Return>', set_goal)
    Button('btn_set', 'Решено!', set_goal, subfrm_input).pack(side='bottom',
           padx=8, pady=11, anchor='s')

try:
    with open('userdata.txt', encoding='utf-8') as file:
        decision = file.read()
except:
    decision = ''


bt_decide = Button('bt_decide', 'Решить и Взяться', decision_window)
bt_decide.pack()

def question_window():
    if 'w_question' in pacer.children:
        bt_question.config(relief='raised')
        pacer.children['w_question'].destroy();    return

    bt_question.config(relief='sunken')
    w_question = tki.Toplevel(pacer, name='w_question')
    w_question.title('кажется...')
    w_question.transient(pacer)
    w_question.focus()

    def w_question_rip():
        w_question.destroy()
        bt_question.config(relief='raised')
    w_question.protocol('WM_DELETE_WINDOW', w_question_rip)

    question = Label30('Ты обещал\n'+decision+'.\nСправился?', w_question)
    question.pack()
    question.update()
    question.config(wraplength='215')
    w_question.geometry('250x'+str(110+question.winfo_height())+'+460+360')


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
    lb_response.config()
    lb_response.pack()
bt_question = Button('bt_question', 'Отчитаться', question_window)
if not decision:    bt_question.config(state='disabled', borderwidth=1)
bt_question.pack(pady=10)



pacer.mainloop()


