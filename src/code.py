from tkinter import Frame, Tk,Canvas,Label ,Frame, Entry, Button,W,E,Listbox,END, Toplevel, messagebox
from tkinter.constants import E, INSERT
from tkinter.font import names
import psycopg2

root = Tk()
root.title("Taller3")
def error_mesage():
    print("Error try again")
    ventana_error = Toplevel()
    ventana_error.geometry("200x100")
    ventana_error.title("Login Error")
    label = Label(ventana_error,text='Error, password incorrect ')
    label.grid(row = 0 , column= 3)

    button = Button(ventana_error,text="Please try again !!",command = ventana_error.destroy).grid(row=1,column=3)

def autenticate(password,name):
    conn = psycopg2.connect(
    dbname = "taller3",
    user = "postgres",
    password = "root",
    host = "localhost",
    port = "5432"
    )

    cursor = conn.cursor()
    query = '''SELECT * FROM entrenador WHERE password = %s AND nombre = %s'''
    cursor.execute(query,(password , name ))

    row = cursor.fetchone()

    if row is not None:
        print(row)
        pantalla_principal(name)
    else:
        error_mesage()
    conn.commit()
    conn.close()

def pantalla_principal(userName):
    principal = Toplevel()
    principal.geometry("300x300")
    principal.title("Game init")
    conn = psycopg2.connect(
        dbname = "taller3",
        user = "postgres",
        password = "root",
        host = "localhost",
        port = "5432"
    ) 
    
    label = Label(principal,text='nombre: ')
    label.grid(row=1,column=1)
    label = Label(principal,text=userName)
    label.grid(row=1,column=2)

    
    cursor = conn.cursor()
    query = '''SELECT * FROM entrenador WHERE nombre = %s '''
    #print(user_name)
    cursor.execute(query,(userName, ))


    row = cursor.fetchone()

    label = Label(principal,text = 'Nick name ')
    label.grid(row=2,column=1)
    label = Label(principal,text=row[3])
    label.grid(row=2,column=2)

    label = Label(principal,text = 'Date of birth ')
    label.grid(row=3,column=1)
    label = Label(principal,text=row[4])
    label.grid(row=3,column=2)
    
    label = Label(principal,text = 'Age ')
    label.grid(row=4,column=1)
    label = Label(principal,text=row[5])
    label.grid(row=4,column=2)
    
    Creatudex = Button(principal, text = "Creatudex", command=lambda : CreatudexMethod(row[0]))
    Creatudex.grid(row=5,column=2,sticky=W+E)
    Equipo_lucha = Button(principal, text = "Equipo Lucha", command=lambda : Equipo_lucha())
    Equipo_lucha.grid(row=6,column=2,sticky=W+E)
    Expedicion = Button(principal, text = "Expedicion", command=lambda : Expedicion())
    Expedicion.grid(row=7,column=2,sticky=W+E)
    Lucha = Button(principal, text = "Lucha", command=lambda : Expedicion())
    Lucha.grid(row=7,column=2,sticky=W+E)
    Cierre = Button(principal, text = "Cerrar")
    Cierre.grid(row=9,column=2,sticky=W+E)
    

def CreatudexMethod(id):
    id_user = str(id)
    Creatudex = Toplevel()
    Creatudex.geometry("300x300")
    Creatudex.title("Creatudex")
    conn = psycopg2.connect(
        dbname="taller3",
        user = "postgres",
        password = "root",
        host = "localhost",
        port = "5432"
    ) 
    curr = conn.cursor()
    query = '''SELECT * FROM equipo WHERE id_entrenador = %s '''

    curr.execute(query,id_user)

    row = curr.fetchone()

    #id_m1 = row[1]
    #id_m2 = row[2]
    #id_m3 = row[3]
    #id_m4 = row[4]
    #id_m5 = row[5]
    #id_m6 = row[6]

    q1 = '''SELECT nombre especie.nombre FROM monstruos WHERE id_user = %s'''
    curr.execute(q1,id)
    row1 = curr.fetchall()
    list = Listbox(Creatudex,width=80,height=70)
    list.grid(row = 10,columnspan= 4,sticky=E+W)

    for i in row1:
        list.insert(END,i)
    conn.commit()
    conn.close()
def registrar_user():
    registrar = Toplevel()
    registrar.geometry("600x200")
    registrar.title("Registrar nuevo usuario ")

    label = Label(registrar,text='Registrar al usuario ')
    label.grid(row = 0 , column= 1)

    label = Label(registrar,text='Ingrese su nombre  ')
    label.grid(row = 1, column= 0)
    entry_name = Entry(registrar)
    entry_name.grid(row =1 ,column=1)

    label = Label(registrar,text='Ingrese su password  ')
    label.grid(row = 2 , column= 0)
    entry_password = Entry(registrar)
    entry_password.grid(row = 2, column=1)

    label = Label(registrar,text='Elija un nombre de usuario ')
    label.grid(row = 3 , column= 0)

    entry_username = Entry(registrar)
    entry_username.grid(row=3,column=1)
    
    label = Label(registrar,text='Ponga fecha de nacimiento format="dia-mes-año" ')
    label.grid(row = 4 , column= 0)
    entry_fecha = Entry(registrar)
    entry_fecha.grid(row=4,column=1)
    
    label = Label(registrar,text='Ingrese su edad  ')
    label.grid(row = 5 , column= 0)
    entry_edad = Entry(registrar)
    entry_edad.grid(row=5,column=1)

    boton_registrar = Button(registrar,text="Registrar",command=lambda:registrar_query(
        entry_name.get(),
        entry_password.get(),
        entry_username.get(),
        entry_fecha.get(),
        entry_edad.get()
        ))
    boton_registrar.grid(row =6,column=1,sticky=W+E) 



def registrar_query(name,password,username,fecha,edad):

    conn = psycopg2.connect(
        dbname = "taller3",
        user = "postgres",
        password = "root",
        host = "localhost",
        port = "5432"
    )
    
    cur = conn.cursor()
    query = '''INSERT INTO entrenador (nombre, password ,nombre_usuario , fecha_nac , edad) VALUES (%s,%s,%s,%s,%s)'''

    cur.execute(query,(name , password , username , fecha , edad))
    print("data saved !!")
    conn.commit()
    conn.close()
    show(); 

def show ():
    show = Toplevel()
    show.geometry("600x200")
    show.title("User Register")

    conn = psycopg2.connect(
        dbname="taller3",
        user = "postgres",
        password = "root",
        host = "localhost",
        port = "5432"
    ) 
    curr = conn.cursor()
    query = '''SELECT * FROM entrenador '''
    curr.execute(query)

    row = curr.fetchall()
    list =Listbox(show,width=80,height=70)
    list.grid(row = 10,columnspan= 4,sticky=W+E)

    for i in row:
        list.insert(END,i)
    conn.commit()
    conn.close()  

def pantallLogin():

    #canvas

    canvas = Canvas(root,height=380,width=400)
    canvas.pack()

    frame = Frame()
    frame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)
    #nombre
    label = Label(frame,text = 'User Login')
    label.grid(row=0,column = 1)

    label = Label(frame,text= ' User_name : ')
    label.grid(row=1,column=0)

    entry_name = Entry(frame)
    entry_name.grid(row=1,column=1)


    label = Label(frame,text = ' Password :')
    label.grid(row=2,column = 1)

    label = Label(frame,text= ' Password : ')
    label.grid(row=2,column=0)

    entry_pass = Entry(frame)


    entry_pass.grid(row=2,column=1)


    button = Button(frame, text="Login", command=lambda: autenticate(
        entry_pass.get(),
        entry_name.get()
        ))
    buttonregistro = Button(frame ,text = "Sign up",command = lambda:registrar_user())
    button.grid(row=4,column=1,sticky=W+E)
    buttonregistro.grid(row =5,column=1,sticky=W+E) 

pantallLogin()
root.mainloop()