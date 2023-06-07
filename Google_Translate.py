from tkinter import *
from tkinter import ttk,messagebox
import googletrans
from googletrans import Translator
from googletrans import constants


# Set a custom user agent
constants.DEFAULT_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'


root=Tk()
root.title("Google Translator 2.0")
root.geometry("1180x400")
# root.resizable(False,False)
root.configure(background="white")


#Change lable
def label_change():
    c=combo1.get()
    c1=combo2.get()
    lable1.configure(text=c)
    lable2.configure(text=c1)
    root.after(500,label_change)


#Translate fuction
def translate_now():
    try:
        text_ = text1.get(1.0, END)
        t1 = Translator()
        trans_text = t1.translate(text_, dest=combo2.get(), src=combo1.get())
        trans_text = trans_text.text

        text2.delete(1.0, END)
        text2.insert(END, trans_text)
    except Exception as e:
        messagebox.showerror("Error", str(e))




#icon
# image_icon=PhotoImage(file="icon1.png")
# root.iconphoto(False,image_icon)
def load_icon():
    global image_icon
    image_icon = PhotoImage(file="icon1.png")
    root.iconphoto(False, image_icon)

#Logo Image 
logo_image=PhotoImage(file="icon1.png")
image_label=Label(root,image=logo_image,width=220)
image_label.place(x=470,y=85)

language=googletrans.LANGUAGES
languageV=list(language.values())
langl=language.keys()

#first combobox
combo1=ttk.Combobox(root,values=languageV, font="Roboto 14",state="r")
combo1.place(x=110,y=20)
combo1.set("ENGLISH")

lable1=Label(root,text="ENGLISH",font="segoe 30 bold",bg="white",width=15,bd=5,relief=GROOVE)
lable1.place(x=10,y=50)


#Second combobox
combo2=ttk.Combobox(root,values=languageV, font="Roboto 14",state="r")
combo2.place(x=830,y=20)
combo2.set("SELECT LANGUAGE")

lable2=Label(root,text="ENGLISH",font="segoe 30 bold",bg="white",width=15,bd=5,relief=GROOVE)
lable2.place(x=720,y=50)


#first frame
f=Frame(root,bg="Black",bd=3)
f.place(x=10,y=118,width=430,height=210)

text1=Text(f,font="Roboto 20",bg="white",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=415,height=200)

scrollbar1=Scrollbar(f)
scrollbar1.pack(side="right",fill='y')

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)



#second frame
f1=Frame(root,bg="Black",bd=3)
f1.place(x=720,y=118,width=430,height=210)

text2=Text(f1,font="Roboto 20",bg="white",relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=415,height=200)

scrollbar2=Scrollbar(f1)
scrollbar2.pack(side="right",fill='y')

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)



#Translate button
translate=Button(root,text="Translate",font=("Roboto",15),activebackground="white",cursor="hand2",bd=1,width=10,height=2,bg="black",fg="white",command=translate_now)
translate.place(x=495,y=330)

label_change()
root.mainloop()