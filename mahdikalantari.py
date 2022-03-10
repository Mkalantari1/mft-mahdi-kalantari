# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#mohammad mahdi kalantari

#porozhe python basic (zemestan 1400)

import json
import tkinter

####################################

def Submit():
    lbl3.configure(text="")
    f = open("poi.json")
    sb = json.load(f)
    user = en1.get()
    alamat=["!","@","$","%","*","_"," ",".",",","~","#","&","(",")","^","/","'",'"',"+","-","|"]
    if user in sb:
        lbl3.configure(text="tekrari mibashad")
    else:
        if len(user)>10 or len(user)<3:
            
            lbl3.configure(text="kam ya ziad type shode")
        else:
            for i in user:
                if i in alamat:
                    lbl3.configure(text="faghat alefba va adad ha")
                else:
                    lbl3.configure(text="welcome")
                    newuser={en1.get():en2.get()}
                    
                    with open('poi.json') as file:
                        data=json.load(file)
                    with open('poi.json','w') as file:
                        data.update(newuser)
                        file.seek(0)
                        json.dump(data,file)
            
                
###############################################################################         
def Login():
    username=en1.get()
    password=en2.get()
    f = open("poi.json")
    karbaran = json.load(f)
    if username in karbaran:
        if karbaran[username]==password:
            lbl3.configure(text="welcome")
        else:
            lbl3.configure(text="error")
    else:
        lbl3.configure(text="first register")
###############################################################################            
win =tkinter.Tk()
win.geometry("250x75")
lbl1=tkinter.Label(win,text="username",bg='#E2C391')
lbl2=tkinter.Label(win,text="password",bg='#E2C391')
en1=tkinter.Entry(win,bg='#9BBEC7')
en2=tkinter.Entry(win,bg='#9BBEC7')
lbl3=tkinter.Label(win,text="")
b1 =tkinter.Button(win,text="Submit",command=Submit,fg='#F6E27F',bg='#251605')
b2 =tkinter.Button(win,text="login",command=Login,fg='#F6E27F',bg='#251605')
lbl1.grid(row=0,column=0)
lbl2.grid(row=0,column=1)
en1.grid(row=1,column=0)
en2.grid(row=1,column=1)
lbl3.grid(row=1,column=2)
b1.grid(row=2,column=0)
b2.grid(row=2,column=1)

win.mainloop()

###############################################################################