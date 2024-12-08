from customtkinter import *
from PIL import Image
from customtkinter import CTkImage
from tkinter import messagebox
def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','Vous devez saisir tous les champs')
    elif usernameEntry.get()=='scarface' and passwordEntry.get()=='123456':
        messagebox.showinfo('Success','Vous êtes connecté 😊')
        root.destroy()
        import  ems
    else:
        messagebox.showerror('Error','Mauvais mot de passe ou nom d\'utilisateur')


root=CTk()
root.geometry('930x478')
root.resizable(0,0)
root.title('Page de connexion')
image= CTkImage(Image.open('login.png'),size=(930,478))
imageLabel=CTkLabel(root,image=image,text='')
imageLabel.place(x=0,y=0)
headinglabel=CTkLabel(root,text='Gestion des Employés',bg_color='#1C304A',font=('Goudy old style',20,'bold'),text_color='#CF1F3E')
headinglabel.place(x=20,y=100)

usernameEntry=CTkEntry(root,placeholder_text='Entrer votre nom',width=180)
usernameEntry.place(x=30,y=150)
passwordEntry=CTkEntry(root,placeholder_text='Entrer votre mot de passe',width=180,show='*')
passwordEntry.place(x=30,y=200)
loginButton=CTkButton(root,text='Se Connecter',cursor='hand2',command=login)
loginButton.place(x=50,y=250)
root.mainloop()



