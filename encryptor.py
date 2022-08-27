from tkinter import *
from tkinter import messagebox as mb
root = Tk()
root.geometry("500x450")
f = ("Times bold", 14)
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = X )
root.title("Encryptor>>>>")
def textEnc():
    tex = inp1.get()
    encArrs = tex.replace(" ","#")
#_________________________________________________________-
    a = []
    enc2=[]
    encArr=[]
    capitals=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for j in encArrs:
        if j in capitals:
            k=j.lower()
            a.append(k)
        else:
            a.append(j)


    for i in range(len(a)):
        if a[i]=="a":
            encArr.append("s")
        elif a[i]=="s":
            encArr.append("k")
        elif a[i]=="k":
            encArr.append("o")
        elif a[i]=="o":
            encArr.append("w")
        elif a[i]=="w":
            encArr.append("b")
        elif a[i]=="b":
            encArr.append("i")
        elif a[i]=="i":
            encArr.append("v")
        elif a[i]=="v":
            encArr.append("c")
        elif a[i]=="c":
            encArr.append("n")
        elif a[i]=="n":
            encArr.append("u")
        elif a[i]=="u":
            encArr.append("x")
        elif a[i]=="x":
            encArr.append("h")
        elif a[i]=="h":
            encArr.append("y")
        elif a[i]=="y":
            encArr.append("e")
        elif a[i]=="e":
            encArr.append("a")
        elif a[i]=="?":
            encArr.append("_")
        elif a[i]==".":
            encArr.append("*")
        else:
            encArr.append(a[i])

    

    global encText 
    encText = "".join(encArr)
#__________________________________________________________
    label2 = Label(root,text=encText,font=f, wraplength=400,pady=10,justify="center")
    label2.place(y=260,x=23)
    

def encClose():
    root.destroy()

def copyClip():
    if inp1.get() == "":
        mb.showerror(title="Error",message="No text entered!")
    else:
        root.clipboard_clear()
        root.clipboard_append(encText)
        mb.showwarning(title = "Alert!", message = "Text copied to clipboard")
        root.update()

label1 = Label(root, text="Enter the text you want to encrypt!",font=f)
label1.pack()

inp1 = Entry(root,width=50,bg="#d2ebd5",border=5)
inp1.pack(padx=10,pady=20)

butn1 = Button(root,text="Encrypt",command=textEnc,font=f,width=20,height=1,border=5,bg="#5f9ea0")
butn1.pack(pady=5)

butn2 = Button(root,text="Copy",command=copyClip,font=f,width=20,height=1,border=5,bg="#d2b48c")
butn2.pack(pady=5)

butn2 = Button(root,text="Close",command=encClose,font=f,width=20,height=1,border=5,bg="#ce2029")
butn2.pack(pady=5)

root.mainloop()
