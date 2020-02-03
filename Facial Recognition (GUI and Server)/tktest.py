from tkinter import *

#main
window= Tk()

#
def click():
    entered_text=textentry.get()#this will collect the text from textentry box
    if (len(entered_text))==0:
       pass
    else:
        output.delete(0.0,END)
        try:
            defination=my_compdictionary[entered_text]
        except:
            defination="sorry no word found"
        output.insert(END,defination)

def close_window():
    window.destroy()
    exit()
#title
window.title("Upasthiti")

#background
#Label(window,bg="black").grid(row=0,column=0,sticky=W)

#create a text entry box
Label(window,text="Enter the word you wold like to defination for", bg="black",fg="white",font="none 12 bold").grid(row=1,column=0,sticky=W)

#textbox
textentry=Entry(window,width=20,bg="white")
textentry.grid(row=2,column=0,sticky=W)

#submit button
Button(window,text="Submit",width=6,command=click).grid(row=3,column=0,sticky=W)

#create label
Label(window,text="Defination",bg="black",fg="white",font="none 12 bold").grid(row=4,column=0,sticky=W)

#output in window
output=Text(window,width=75,height=6,wrap=WORD,background="white")
output.grid(row=5,columnspan=2,sticky=W)

#dictionary
my_compdictionary={
    'algorithm':'Step by 1','bug':'piece of code'
}

#exit label
Label (window,text="click to exit",bg="black",fg="white",font="none 12 bold").grid(row=6,column=0,sticky=W)

#exit button
Button(window,text="Exit", width=14,command=close_window).grid(row=7,column=0,sticky=W)

window.mainloop()