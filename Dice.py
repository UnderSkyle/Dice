#coding:utf-8
from tkinter import *
from functools import partial
import webbrowser
from random import *
from tkinter.messagebox import *
import sqlite3

connection = sqlite3.connect("base.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS tt_users (user_name TEXT, Force INTEGER, Dexte INTEGER, Constit  INTEGER, Intel INTEGER, Sagesse INTEGER, Charisme INTEGER)")
#debug purpuses if db empty and here for more changes to the username feature 
#cursor.execute("INSERT INTO tt_users(user_name, Force, Dexte, Constit, Intel, Sagesse, Charisme) VALUES('Rick', 0, 0, 0, 0, 0, 0)")
connection.commit()
my_username = ("Rick",)
get_db_value = cursor.execute('SELECT * FROM tt_users WHERE user_name = ?', my_username)



def open_under_twitter():
    webbrowser.open_new("https://twitter.com/Skyle_Tale")

def roll(Num):
    result=int(randint(1,Num))
    Stat=ChoixStat.get()
    titre1="Ca passe tu as fais "+str(result)
    titre2="Ca ne passe pas tu as fais "+str(result)
    titre3=' WOUAA REUSSITE CRITIQUE'
    titre4 = ' DOMMAGE ECHEC CRITIQUE'
    if Stat == "Force":
        check = int(boutton1.getvalue())
        if result <= check:
            titre = titre1
            if result == 1:
                titre = titre1 + titre3
            showinfo("DiceV2", titre)
        elif result > check:
            titre = titre2
            if result == Num:
                titre = titre2 + titre4
            showinfo("DiceV2", titre)

    elif Stat == "Dexterite":
        check = int(boutton2.getvalue())
        if result <= check:
            titre = titre1
            if result == 1:
                titre = titre1 + titre3
            showinfo("DiceV2", titre)
        elif result > check:
            titre = titre2
            if result == Num:
                titre = titre2 + titre4
            showinfo("DiceV2", titre)

    elif Stat == "Constitution":
        check = int(boutton3.getvalue())
        if result <= check:
            titre = titre1
            if result == 1:
                titre = titre1 + titre3
            showinfo("DiceV2", titre)
        elif result > check:
            titre = titre2
            if result == Num:
                titre = titre2 + titre4
            showinfo("DiceV2", titre)

    elif Stat == "Intelligence":
        check = int(boutton4.getvalue())
        if result <= check:
            titre = titre1
            if result == 1:
                titre = titre1 + titre3
            showinfo("DiceV2", titre)
        elif result > check:
            titre = titre2
            if result == Num:
                titre = titre2 + titre4
            showinfo("DiceV2", titre)
    elif Stat == "Sagesse":

        check = int(boutton5.getvalue())
        if result <= check:
            titre = titre1
            if result == 1:
                titre = titre1 + titre3
            showinfo("DiceV2", titre)
        elif result > check:
            titre = titre2
            if result == Num:
                titre = titre2 + titre4
            showinfo("DiceV2", titre)
    elif Stat == "Charisme":

            check=int(boutton6.getvalue())
            if result <= check:
                titre=titre1
                if result == 1 :
                    titre=titre1+titre3
                showinfo("DiceV2", titre)
            elif result > check:
                titre=titre2
                if result == Num:
                    titre = titre2 + titre4
                showinfo("DiceV2", titre)
    elif Stat == "autre":
            showinfo("DiceV2", "vous avez fais "+str(result))

class SpinboX:
    def __init__(self, frame, Stat,):
        self.frame = frame
        self.label = Label(self.frame, text=1, bg='#2222df', fg='white', font=("Arial", 15))
        self.value = DoubleVar(self.frame)
        self.stat = Stat
        self.labelS = Label(self.frame, text=self.stat, bg='#2222df', fg='white', font=("Arial", 15))
        self.labelS.pack(side=LEFT)
        self.label.pack(side=LEFT, padx=10)

        self.create()

    def update_label(self):
        self.label.config(text=int(self.value.get()))
    def create(self):
        #setup taken into account
        spin=Spinbox(self.frame, textvariable=self.value, from_=1, to=20, increment=1,state='readonly' , fg ='black')
        spin.config(command=self.update_label)
        spin.pack(side=TOP, padx=10,pady=3)

    def getvalue(self):
        return self.value.get()


#save all the values into db
def save():
    liste=[]
    liste.append(boutton1.getvalue())
    liste.append(boutton2.getvalue())
    liste.append(boutton3.getvalue())
    liste.append(boutton4.getvalue())
    liste.append(boutton5.getvalue())
    liste.append(boutton6.getvalue())
    cursor.execute('UPDATE tt_users SET Force = ?, Dexte= ?, Constit = ?, Intel = ?, Sagesse = ?, Charisme = ?', liste)
    connection.commit()


window = Tk()

window.title("Dice V2")
window.geometry("1080x720")
window.minsize(1080, 720)
window.config(background='#2222df')

# boite


label_title = Label(window, text="Dice V2", font=("Arial", 40), bg='#2222df', fg='white')
label_title.pack()

label_title = Label(window, text="W.I.P", font=("Arial", 30), bg='#2222df', fg='white')
label_title.pack()


result=get_db_value.fetchall()
result=result[0]
frame0=Frame(window, bg='#2222df')
frame1 = Frame(frame0, bg='#2222df', pady=10)
boutton1 = SpinboX(frame1,"Force",)
boutton1.value.set(result[1])
boutton1.update_label()

frame2 = Frame(frame0, bg='#2222df', pady=10,)
boutton2 = SpinboX(frame2,"Dexterité",)
boutton2.value.set(result[2])
boutton2.update_label()

frame3 = Frame(frame0, bg='#2222df', pady=10,)
boutton3 = SpinboX(frame3,"Constitution",)
boutton3.value.set(result[3])
boutton3.update_label()

frame4 = Frame(frame0, bg='#2222df', pady=10,)
boutton4 = SpinboX(frame4,"Intelligence",)
boutton4.value.set(result[4])
boutton4.update_label()

frame5 = Frame(frame0, bg='#2222df', pady=10,)
boutton5 = SpinboX(frame5,"Sagesse",)
boutton5.value.set(result[5])
boutton5.update_label()

frame6 = Frame(frame0, bg='#2222df', pady=10,)
boutton6 = SpinboX(frame6,"Charisme",)
boutton6.value.set(result[6])
boutton6.update_label()

frame7 = Frame(frame0, bg='#2222df', pady=10,)
savebutton= Button(frame0, text='save',font=('Arial',10), padx=10 , pady=10)
savebutton.config(command=save)
savebutton.pack()

frame0.pack(side=RIGHT)
frame1.pack(side=BOTTOM,)
frame2.pack(side=BOTTOM,)
frame3.pack(side=BOTTOM,)
frame4.pack(side=BOTTOM,)
frame5.pack(side=BOTTOM,)
frame6.pack(side=BOTTOM,)
frame7.pack(side=TOP,)

framedown = Frame(window, bg='#2222df',pady=20)
ChoixStat = Spinbox(framedown,values=('Charisme','Sagesse','Intelligence','Constitution','Dexterite','Force','autre'),state='readonly' , fg ="black")
D100 = Button(framedown, text="D100", command=partial(roll,100))
D20 = Button(framedown, text="D20", command=partial(roll,20))
D4 = Button(framedown, text="D4", command=partial(roll,4))


D100.pack(side=LEFT,padx=10)
D20.pack(side=LEFT,padx=10)
D4.pack(side=LEFT,padx=10)
ChoixStat.pack(side=LEFT,padx=10)
framedown.pack(side=BOTTOM,)


window.mainloop()
connection.close()
