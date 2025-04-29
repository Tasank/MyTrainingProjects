from tkinter import *
root=Tk()
root.geometry("600x400")
root.title("окошко")
root["bg"]= "green"
text=Label(root, text='𓁈𓂀𓋹𓆣𓁀𓀾',font=("Consolas",100 , "bold"),fg="black",bg="dark green" )
text.pack()
x=Label(root, text="Бог Ра-бог солнца", bg="dark green" )
x.pack()

btn = Button(root, text="Нажми на меня!", fg="red", font=("Algerian",23),  bg="dark green")
btn.pack()

root.mainloop()
