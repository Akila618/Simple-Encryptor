from tkinter import *
from tkinter import messagebox as mb

root = Tk()
root.title("Decryptor>>>ATW")
fnt = ("Arial" , 14)
root.geometry("500x450")

#functions
def closeFunc():
    root.destroy()

def copyFunc():
    if inp1.get() == "":
        mb.showerror(title="Error",message="No text entered!")
    else:
        root.clipboard_clear()
        root.clipboard_append(fina)
        mb.showwarning(title="Notice", message="Text copied t clipboard!")
        root.update()

def decFunc():
    cypher = inp1.get()
    a = []
    decArr=[]
    for i in range(len(cypher)):
        if cypher[i] == "a":
            a.append("e")
        elif cypher[i] == "e":
            a.append("y")
        elif cypher[i] == "y":
            a.append("h")
        elif cypher[i] == "h":
            a.append("x")
        elif cypher[i] == "x":
            a.append("u")
        elif cypher[i] == "u":
            a.append("n")
        elif cypher[i] == "n":
            a.append("c")
        elif cypher[i] == "c":
            a.append("v")
        elif cypher[i] == "v":
            a.append("i")
        elif cypher[i] == "i":
            a.append("b")
        elif cypher[i] == "b":
            a.append("w")
        elif cypher[i] == "w":
            a.append("o")
        elif cypher[i] == "o":
            a.append("k")
        elif cypher[i] == "k":
            a.append("s")
        elif cypher[i] == "s":
            a.append("a")
        elif cypher[i] == "_":
            a.append("?")
        elif cypher[i] == "*":
            a.append(".")
        else:
            a.append(cypher[i])
    
    decText = "".join(a)
    global fina
    fina = decText.replace("#", " ")

    labl2 = Label(root,text=fina, font=fnt)
    labl2.pack(pady=10)

header = Label(root, text="Enter your cypher text to decrpyt:",font=fnt,pady=20)
header.pack()

inp1 = Entry(root, width=50,bg="#d2ebd5",border=5)
inp1.pack(padx=10,pady=20)

btn1 = Button(root, text="Decrypt",font=fnt,width=20,height=1,border=5,bg="#5f9ea0",command=decFunc)
btn1.pack(pady=5)
btn2 = Button(root, text="Copy",font=fnt,width=20,height=1,border=5,bg="#d2b48c",command=copyFunc)
btn2.pack(pady=5)
btn3 = Button(root, text="Close",font=fnt,width=20,height=1,border=5,bg="#ce2029",command=closeFunc)
btn3.pack(pady=5)

root.mainloop()