from customtkinter import *
from PIL import Image
from tkinter import ttk,messagebox
import database
# function

def delete_all():
    result=messagebox.askyesno('Confim','Voulez vous vraiment tout supprimer ? ☣️ ')
    if result:
        database.deleteall_records()
    else:
        pass
def delete_employe():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('Error', 'Selectionne un employé pour le supprimer')
    else:
        database.delete(idEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','L\'employé a été supprimé de la base des données 😎')
def update_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Selectionne un employé pour le modifier 🫡' )
    else:
        database.update(idEntry.get(),nameEntry.get(),phoneEntry.get(),roleBox.get(),genderBox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','l\'employé a été modifier ')

def selection(event):
    selected_item=tree.selection()
    if selected_item:
        row=tree.item(selected_item)['values']
        clear()
        idEntry.insert(0,row[0])
        nameEntry.insert(0,row[1])
        phoneEntry.insert(0,row[2])
        roleBox.set(row[3])
        genderBox.set(row[4])
        salaryEntry.insert(0,row[5])



def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0,END)
    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)
    salaryEntry.delete(0, END)
    genderBox.set('Masculin')
    roleBox.set('Web Developer')

def treeview_data():
    employees=database.fetch_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert('',END,values=employee)


def add_employe():
    if idEntry.get()=='' or phoneEntry.get()=='' or nameEntry.get() == '' or salaryEntry.get()=='':
        messagebox.showerror('Error','Vous devez remplir tout les champs')
    elif database.id_exists(idEntry.get()):
        messagebox.showerror('Error','Id existe déjà')
    elif not idEntry.get().startswith('EMP'):
        messagebox.showerror('Error',"L'identifiant doit être composé comme suit (e.g., 'EMP1').")
    else:
        database.insert(idEntry.get(),nameEntry.get(),phoneEntry.get(),roleBox.get(),genderBox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Employe ajouter avec succès 👌')


def search_employee():
    if searchEntry.get()=='':
        messagebox.showerror('Error','Entrer une valeur pour la recherche 🕵️')
    elif searchBox.get()=='rechercher par':
        messagebox.showerror('Error', 'Selectionnez une valeur pour la recherche 🕵️')
    else:
        searched_data=database.search(searchBox.get(),searchEntry.get())
        tree.delete(*tree.get_children())
        for employee in searched_data:
            tree.insert('', END, values=employee)

def show_all():
    treeview_data()
    searchEntry.delete(0,END)
    searchBox.set('recherche par')


window=CTk()
window.geometry('900x700+150+150')
window.resizable(False,False)
window.title('Système de gestion des employés')
window.configure(fg_color='#161C30',posiy=0)
logo=CTkImage(Image.open('job.png'),size=(900,300))
logoLabel=CTkLabel(window,image=logo,text='')
logoLabel.grid(row=0,column=0,columnspan=2)


leftFrame=CTkFrame(window,fg_color='#161C30')
leftFrame.grid(row=1,column=0)

idLabel=CTkLabel(leftFrame,text='id',font=('arial',18,'bold'))
idLabel.grid(row=0,column=0,padx=20,pady=15,sticky='w')
idEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
idEntry.grid(row=0,column=1)

nameLabel=CTkLabel(leftFrame,text='name',font=('arial',18,'bold'))
nameLabel.grid(row=1,column=0,padx=20,pady=15,sticky='w')
nameEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
nameEntry.grid(row=1,column=1)

phoneLabel=CTkLabel(leftFrame,text='Télephone',font=('arial',18,'bold'))
phoneLabel.grid(row=2,column=0,padx=20,)
phoneEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
phoneEntry.grid(row=2,column=1)

roleLabel=CTkLabel(leftFrame,text='Role',font=('arial',18,'bold'))
roleLabel.grid(row=3,column=0,padx=20,pady=30)
role_options=['Web Developer', 'Technicien Reseau', 'Business Anylist', 'Cloud Architect', 'Network Engineer']
roleBox=CTkComboBox(leftFrame,values=role_options,width=180,font=('arial',18,'bold'),state='readonly')
roleBox.grid(row=3,column=1)
roleBox.set(role_options[0])

genderLabel=CTkLabel(leftFrame,text='Sexe',font=('arial',18,'bold'))
genderLabel.grid(row=4,column=0,padx=20,)
sexe_options=['M', 'F']
genderBox=CTkComboBox(leftFrame,values=sexe_options,width=180,font=('arial',18,'bold'),state='readonly')
genderBox.grid(row=4,column=1)
genderBox.set(sexe_options[0])

salaryLabel=CTkLabel(leftFrame,text='Salaire',font=('arial',18,'bold'))
salaryLabel.grid(row=5,column=0,padx=20,pady=20)
salaryEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
salaryEntry.grid(row=5,column=1)

rightFrame=CTkFrame(window)
rightFrame.grid(row=1,column=1)

search_options=['id', 'Name', 'Sexe', 'Salaire', 'Télephone','role']

searchBox=CTkComboBox(rightFrame,values=search_options,state='readonly')
searchBox.grid(row=0,column=0)

searchBox.set('rechercher par')

searchEntry=CTkEntry(rightFrame)
searchEntry.grid(row=0,column=1)

searchButton=CTkButton(rightFrame,text='Rechercher',width=100,command=search_employee)
searchButton.grid(row=0,column=2)

showallButton=CTkButton(rightFrame,text='Voir tout',width=100,command=show_all)
showallButton.grid(row=0,column=3,pady=5)

tree=ttk.Treeview(rightFrame,height=15,)
tree.grid(row=1,column=0,columnspan=4)

tree['columns']=('Id','Name','Télephone','Role','Sexe','Salaire')

tree.heading('Id',text='Id')
tree.heading('Name',text='Name')
tree.heading('Role',text='Role')
tree.heading('Sexe',text='Sexe')
tree.heading('Salaire',text='Salaire')
tree.heading('Télephone',text='Télephone')

tree.config(show='headings')

tree.column('Id',width=70)
tree.column('Name',width=110)
tree.column('Télephone',width=140)
tree.column('Sexe',width=50)
tree.column('Salaire',width=100)
tree.column('Role',width=200)

style=ttk.Style()
style.configure('Treeview.Heading', font=('arial',18,'bold'))
style.configure('Treeview',font=('arial',15,'bold'),rowhight=30,background='#161C30',foreground='white')

scrollbar=ttk.Scrollbar(rightFrame,orient=VERTICAL,command=tree.yview)
scrollbar.grid(row=1,column=4,sticky='ns')
tree.config(yscrollcommand=scrollbar)

buttonFrame=CTkFrame(window,fg_color='#161C30')
buttonFrame.grid(row=2,column=0,columnspan=2,pady=10)

newButton=CTkButton(buttonFrame,text='Nouveau employé',font=('arial',15,'bold'),width=160,corner_radius=15,command=lambda: clear(True) )
newButton.grid(row=0,column=0,pady=5,padx=5)

addButton=CTkButton(buttonFrame,text='Ajouter un employé',font=('arial',15,'bold'),width=160,corner_radius=15,command=add_employe)
addButton.grid(row=0,column=1,pady=5,padx=5)


updateButton=CTkButton(buttonFrame,text='Modifier employé',font=('arial',15,'bold'),width=160,corner_radius=15,command=update_employee)
updateButton.grid(row=0,column=2,pady=5,padx=5)

deleteButton=CTkButton(buttonFrame,text='Supprimer employé',font=('arial',15,'bold'),width=160,corner_radius=15,command=delete_employe)
deleteButton.grid(row=0,column=3,pady=5,padx=5)

deleteallButton=CTkButton(buttonFrame,text='Supprimer tout',font=('arial',15,'bold'),width=160,corner_radius=15,command=delete_all)
deleteallButton.grid(row=0,column=4,pady=5,padx=5)


treeview_data()
window.bind('<ButtonRelease>',selection)

def center_window(window):
    window.update_idletasks()  # Mise à jour des dimensions de la fenêtre
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = window.winfo_width()
    window_height = window.winfo_height()

    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Centrer la fenêtre
center_window(window)

window.mainloop()