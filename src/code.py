
from tkinter import Frame, Tk,Canvas,Label ,Frame, Entry, Button,W,E,Listbox,END, Toplevel, messagebox
from tkinter.constants import E, INSERT, SEL_FIRST
from tkinter.font import names
from typing import Text
import psycopg2
import random

root = Tk()
root.title("Taller3")
#pantalla de error del login (muestra un mensaje y un boton de regreso a intentarlo)
def error_mesage():
    print("Error try again")
    ventana_error = Toplevel()
    ventana_error.geometry("200x100")
    ventana_error.title("Login Error")
    #mensaje
    label = Label(ventana_error,text='Error, password incorrect ')
    label.grid(row = 0 , column= 3)
    #boton de regreso
    button = Button(ventana_error,text="Please try again !!",command = ventana_error.destroy).grid(row=1,column=3)
#confirmacion de credenciales
def autenticate(password,name):
    #conexion con la base de datos setear parametros
    conn = psycopg2.connect(
    dbname = "taller3",
    user = "postgres",
    password = "root",
    host = "localhost",
    port = "5432"
    )

    cursor = conn.cursor()
    #seelccionamos solamente los users que tengan el nombre y la contraseña
    query = '''SELECT * FROM trainer WHERE password = %s AND nombre = %s'''
    cursor.execute(query,( password , name ))
    #la guardamos en una especie de lista
    row = cursor.fetchone()
    #si regresa un none es poe que no lo encontro
    if row is not None:
        print(row)
        pantalla_principal(name)
    else:
        error_mesage()
    conn.commit()
    conn.close()
#pantalla principal o menu
def pantalla_principal(userName):
    principal = Toplevel()
    principal.geometry("300x300")
    principal.title("Game init")
    #conexion con la base setear parametros 
    conn = psycopg2.connect(
        dbname = "taller3",
        user = "postgres",
        password = "root",
        host = "localhost",
        port = "5432"
    ) 
    #mostrar nombre
    label = Label(principal,text='nombre: ')
    label.grid(row=1,column=1)
    label = Label(principal,text=userName)
    label.grid(row=1,column=2)
    #cursor para ejecutar 
    cursor = conn.cursor()
    #seleccionamos los parametros del entrenador de la tabla trainer
    query = '''SELECT * FROM trainer WHERE nombre = %s '''
    #jecutamos
    cursor.execute(query,(userName, ))
    #guardamos
    row = cursor.fetchone()
    #mostramos el nombre encontrado
    label = Label(principal,text = 'Nick name ')
    label.grid(row=2,column=1)
    label = Label(principal,text=row[3])
    label.grid(row=2,column=2)
    #mostramos la fecha de nacimiento
    label = Label(principal,text = 'Date of birth ')
    label.grid(row=3,column=1)
    label = Label(principal,text=row[5])
    label.grid(row=3,column=2)
    #mostramos la edad
    label = Label(principal,text = 'Age ')
    label.grid(row=4,column=1)
    label = Label(principal,text=row[6])
    label.grid(row=4,column=2)
    #empezamos con los botones de los menus 
    #creatudex manda al metodo Ceatudexmethod
    Creatudex = Button(principal, text = "Creatudex", command=lambda : CreatudexMethod(row[0]))
    Creatudex.grid(row=5,column=2,sticky=W+E)
    #Equipo lucha manda al metodo EquipoluchaMethod
    Equipo_lucha = Button(principal, text = "Equipo Lucha", command=lambda : Equipo_lucha_Method(row[0]))
    Equipo_lucha.grid(row=6,column=2,sticky=W+E)
    #Expedicion boton que lleva al expedicionmethod
    Expedicion = Button(principal, text = "Expedicion", command=lambda : ExpedicionMethod(userName))
    Expedicion.grid(row=7,column=2,sticky=W+E)
    #bLucha boton que manda al menu de lucha
    Lucha = Button(principal, text = "Lucha", command=lambda : Fight(userName))
    Lucha.grid(row=8,column=2,sticky=W+E)
    #cierre boton que cierra la ventana principal quedando la de login
    Cierre = Button(principal, text = "Cerrar",command=principal.destroy)
    Cierre.grid(row=9,column=2,sticky=W+E)
#obtenemos el id de un entrenador segun su nombre
def obtenerid(username):
    conn = psycopg2.connect(
        dbname = "taller3",
        user = "postgres",
        password = "root",
        host = "localhost",
        port = "5432"
    )    
    cur = conn.cursor()
    #seleccionamos el id del entrenador con el nombre pasado como parametro
    query = '''select id from trainer where nombre = %s'''
    cur.execute(query,(username,))
    row = cur.fetchone()
    conn.commit()
    conn.close()
    #retornamos el nombre
    return row[0]
#obtenemos el nombre de un entrenador segun su id lo mismo del metodo anterior solo retorna la id en vez del nombre   
def obtener_nombre(id):
    conn = psycopg2.connect(
        dbname = "taller3",
        user = "postgres",
        password = "root",
        host = "localhost",
        port = "5432"
    )    
    cur = conn.cursor()
    query = '''select nombre from trainer where id = %s'''
    cur.execute(query,(id,))
    row = cur.fetchone()
    conn.commit()
    conn.close()
    #regresamos la id
    return row[0]
#da al programa de lucha un jugador aleatorio
def randomPlayer():
    conn = psycopg2.connect(
        dbname = "taller3",
        user = "postgres",
        password = "root",
        host = "localhost",
        port = "5432"
    )
    cursor = conn.cursor()
    query = '''select * from trainer '''
    cursor.execute(query)
    jugadores = cursor.fetchall() 
    #el random choice dado un arreglo elige uno al azar
    jugador_random = random.choice(jugadores)
    #retornamos el nombre del jugador
    return jugador_random[1]
#metodo que da el menu de pelea
def Fight(username):
    #ventana
    Pelea = Toplevel()
    Pelea.geometry("500x500")
    Pelea.title("Gymnasio pokemon")
    #conexion
    conn = psycopg2.connect(
        dbname = "taller3",
        user = "postgres",
        password = "root",
        host = "localhost",
        port = "5432"
    ) 
    #nombre del primer entrenador
    label = Label(Pelea,text = 'entrenador :  '+username).grid(row=1,column=1)
    cursor = conn.cursor()
    #mostrar equipos con el nombre del monstruo la velocidad y la salud segun al team del jugador
    id_player1 = obtenerid(username)
    query = '''select nombre, velocidad, salud from monster where id_team = %s '''
    cursor.execute(query,(id_player1,))
    row = cursor.fetchall()       
    #mostramos los resultados en una lista
    lista = Listbox(Pelea,width=20,height=6)
    lista.grid(row = 10,columnspan= 4,sticky=W+E)    
    for i in row:
        lista.insert(END,i)
    # el mismo procedimento con el player 2
    #elegimos un jugador random con el metodo especificado arriba
    player2 = randomPlayer()
    #nombre del entrenador 2
    label = Label(Pelea,text = ' entrenador :  '+ player2).grid(row=1,column=8)
    id_player2 = obtenerid(player2)
    #seleccionamos su equipo 
    query2='''select nombre,velocidad,salud from monster where id_team = %s'''
    cursor.execute(query2,(id_player2,))
    #guardamos los monster
    row2 = cursor.fetchall()
    #lista a mostrar
    lista2 = Listbox(Pelea,width=20,height=6)
    lista2.grid(row = 10,columnspan= 4,column = 8 ,sticky=W+E)    
    for i in row2:
        lista2.insert(END,i)
    #boton que da con el metodo de lucha que simula la batalla
    pelear = Button(Pelea,text="Luchar",command=lambda:pelearMethod(id_player1,id_player2))
    pelear.grid(row =2,column=4,sticky=W+E) 
    conn.commit()
    conn.close()
#simulacion de una pelea
def pelearMethod(id1,id2):
    conn = psycopg2.connect(
        dbname = "taller3",
        user = "postgres",
        password = "root",
        host = "localhost",
        port = "5432"
    ) 
    cursor = conn.cursor()
    #sacamos el nombre velocidad salud daño base el tipo la fortaleza la debilidad el nombre del dueño el nombre de la especie y el tipo de ataque que necesitaremos para simular
    query = '''Select  m.nombre,m.velocidad,m.salud,a.daño_base as daño, t.nombre ,t.fortaleza, t.debilidad , tr.nombre,e.nombre ,a.tipo_at from monster m join ataque a on m.id_ataque = a.id join especie e on m.id_especie = e.id join tipos t on t.id = e.id_tipo join trainer tr on m.id_trainer = tr.id  where m.id_team = %s;'''

    cursor.execute(query,(id1,))
    lista_player1 = cursor.fetchall()
    #descomentar para lanzar la lista por consola
    """for i in range(len(lista_player1)):
        print(lista_player1[i])"""

    cursor.execute(query,(id2,))
    lista_player2 = cursor.fetchall()
    #descomentar para lanzar la lista por consola
    """for i in range(len(lista_player2)):
        print(lista_player2[i])"""
    #medimos los largos de las listas que equivalen a los monstruos que tiene cada entrenador
    largo_lista1 = len(lista_player1)
    largo_lista2 = len(lista_player2)
    #seteamos un minimo para guardar cual es la cantidad de monster que pelearan
    min = 0
    #configuracion del minimo
    if (largo_lista1 > largo_lista2):
        min = largo_lista2
    else :
        min = largo_lista1
    #ver minimo descomentar
    #print(min)
    #sacamos el nombre del jugador 1
    nombrej1 = obtener_nombre(id1)
    #sacamos el nombre del segundo jugador sacado aleatoriamente
    nombrej2 = obtener_nombre(id2)
    #seteamos las partidas totales jugadas
    setS(nombrej1)
    setS(nombrej2)
    #seteamos los contadores individuales de las batallas ganadas si un monster gana contra otro setea este valor
    jugador1 = 0
    jugador2 = 0
    #definir matriz de pelea iterando con los monster que se estan primeros dependiendo del valor del minimo sera los que vayan a pelear 
    #segun este requerimiento :Si uno de los entrenadores no tiene 6 monstruos solo pelearán la cantidad máxima que tenganlos dos, ejemplo 3 vs 3
    for a in range(min):
        #tiramos los primeros monster
        m1 = lista_player1[a]
        m2 = lista_player2[a]
        #el metodo quien gana simula la pelea entre los 2  le enviamos todos los datos de los moster para analizarlos
        ganador = QuienGana(m1,m2)
        #quien gana retorna el nombre del jugador ganador y se compara para setear las batallas ganadas
        if ganador == nombrej1:
            jugador1+=1
        else:
            jugador2+=1
    #vemos que jugador gano 
    if jugador1 > jugador2:
        #mostramos por pantalla un mensaje de ganador con el jugador
        message = "El jugador "+ nombrej1 + "Ha ganado"
        #seteamos las batallas ganadas
        setearStats(nombrej1)
        #seteamos las batallas perdidas si uno gana el otro pierde se setean enseguida
        setStatNegative(nombrej2)
        messagebox.showinfo("Ganador",message)
    if jugador2 > jugador1 :
        #mostramos por pantalla un mensaje de ganador con el jugador
        message = "El jugador "+ nombrej2 + "Ha ganado"
        #seteamos las batallas ganadas
        setearStats(nombrej2)
        #seteamos las batallas perdidas si uno gana el otro pierde se setean enseguida
        setStatNegative(nombrej1)
        messagebox.showinfo("Ganador",message)
    conn.commit()
    conn.close()
#seteamos la estadistica de las partidas jugadas
def setS(name):
    conn = psycopg2.connect(
        dbname = "taller3",
        user = "postgres",
        password = "root",
        host = "localhost",
        port = "5432"
    ) 
    cursor = conn.cursor()
    q1 = '''select partidasTotales, partidasGanadas, partidasPerdidas from trainer where nombre = %s'''
    cursor.execute(q1,(name,))
    row = cursor.fetchone()
    #aca aumentamos 1 el contador con la funcion Fil
    contador = Fil(int(row[0]))
    #seteamos el nuevo valor
    query = '''update trainer set partidasTotales = %s where nombre = %s'''
    cursor.execute(query,(contador,name))

    conn.commit()
    conn.close()
#seteamos las estadisticas de las partidas perdidas
def setStatNegative(name):
    conn = psycopg2.connect(
        dbname = "taller3",
        user = "postgres",
        password = "root",
        host = "localhost",
        port = "5432"
    ) 
    cursor = conn.cursor()
    q1 = '''select partidasTotales, partidasGanadas, partidasPerdidas from trainer where nombre = %s'''
    cursor.execute(q1,(name,))
    row = cursor.fetchone()
    #aca aumentamos 1 el contador con la funcion Fil
    contador = Fil(int(row[2]))
    #seteamos el nuevo valor
    query = '''update trainer set partidasPerdidas = %s where nombre = %s'''
    cursor.execute(query,(contador,name))
    conn.commit()
    conn.close()
#sumamos iterativamente 1 al contador de partidas para despues setearlo
def Fil(num):
    return num+1
#setear las partidas ganadas
def setearStats(name):
    conn = psycopg2.connect(
        dbname = "taller3",
        user = "postgres",
        password = "root",
        host = "localhost",
        port = "5432"
    ) 
    cursor = conn.cursor()
    q1 = '''select partidasTotales, partidasGanadas, partidasPerdidas from trainer where nombre = %s'''
    cursor.execute(q1,(name,))
    row = cursor.fetchone()
    #aca aumentamos 1 el contador con la funcion Fil
    contador = Fil(int(row[1]))
    #seteamos el nuevo valor
    query = '''update trainer set partidasGanadas = %s where nombre = %s'''
    cursor.execute(query,(contador,name))
    conn.commit()
    conn.close()
#este metodo muestra el algoritmo de la batalla por turnos
def QuienGana(m1,m2):
    #tener las saludes y daños de los monstruos
    print(m1[0])
    print(m2[0])
    #descomentar para ver el monster que batalla
    print("----------------------")
    #sacamos las velocidades
    v1 = int(m1[1]) 
    v2 = int(m2[1])
    #sacamos las salud
    s1 = int(m1[2])
    s2 = int(m2[2])
    #sacamos los damos bases de los moster ingresados a la funcion
    d1 = calculo_daño(m1,m2)
    d2 = calculo_daño(m2,m1)
    print("vel "+ str(v1) + " salud "+ str(s1))
    #definir velocidad mayor
    vmayor = 0

    if v1 > v2:
        vmayor = v1
    else :
        vmayor = v2
    #ataca primero 
    if vmayor == v1: 
        print("ataca el primer player")
        #aca vemos si las saludes llegan a 0 o negativo se estable un ganador y retorna el nombre
        while s1 > 0 and s2 > 0:
            s2 = atacar(s2,d1)
            s1 = atacar(s1,d2)
        if s2 <= 0:
            return m1[7]
        else :
            return m2[7]
    else: 
        print(" ataca el segundo player ")
        #aca vemos si las saludes llegan a 0 o negativo se estable un ganador y retorna el nombre
        while s1 > 0 and s2 > 0:
            s1 = atacar(s1,d2)
            s2 = atacar(s2,d1)
        if s2 <= 0:
            return m1[7]
        else :
            return m2[7]
#calculamos el daño dependiendo de sus preferencias segun
# Si el ataque y la especie son del mismo tipo aumenta 15% el daño base del ataque.-Si el tipo del ataque es fuerte contra el tipo de especie del contrincante 20% más de daño.-Si el tipo del ataque es débil contra el tipo de especie del contrincante 20% menos de daño.       
def calculo_daño(m_añalisis,m2_referencia):
    #si las especies y los tipos son iguales aumenta 15 % el daño base
    d1 = int(m_añalisis[3])
    esp1 = m_añalisis[4]
    tipo1 = m_añalisis[9]
    if esp1 == tipo1:
        d1 = d1+(d1*0.15)
    else :
        d1 =  int(m_añalisis[3])

    #si la fortaleza es la debilidad del otro 20 %mas de daño al que tiene la fortaleza
    tipoA = m_añalisis[9]
    deb = m2_referencia[6]
    if tipoA == deb:
        d1 += d1*0.2
    #si la fortaleza de uno es el tipo de ataque descuento 20 %
    fort = m2_referencia[5]
    if tipoA == fort:
        d1 -= d1*0.2
    #retornamos el daño ya calcular 
    return d1
#atacar solo resta el daño a la salud de un mosnter se usa en el metodo quien gana 
def atacar(salud,daño):
    d = daño
    s = salud
    return s - d
#menu que muestra el quipo de batalla para que lo pueda ver el usuario con sus stats
def  Equipo_lucha_Method(id):
    
    TeamF = Toplevel()
    TeamF.geometry("500x400")
    TeamF.title("Equipo Lucha")
    conn = psycopg2.connect(
        dbname = "taller3",
        user = "postgres",
        password = "root",
        host = "localhost",
        port = "5432"
    )
    cursor = conn.cursor()
    q = '''select nombre,partidasTotales, partidasGanadas, partidasPerdidas from trainer where id = %s'''
    cursor.execute(q,(id,))
    result = cursor.fetchone()

    query = '''select m.id, m.nombre , m.velocidad, m.salud ,t.nombre as tipo, a.nombre as ataque from monster m join especie e on m.id_especie = e.id join ataque a on a.id = m.id_ataque join tipos t on e.id_tipo = t.id where m.id_team = %s'''
    cursor.execute(query,(id,))
    row = cursor.fetchall()
    label = Label(TeamF,text = 'equipo del entrenador :  '+result[0]).grid(row=1,column=1)
    label = Label(TeamF,text = 'partidas ganadas :  '+str(result[2])).grid(row=2,column=1)
    label = Label(TeamF,text = 'partidas perdidas :  '+str(result[3])).grid(row=3,column=1)
    label = Label(TeamF,text = 'partidas totales :  '+str(result[1])).grid(row=4,column=1)

    list =Listbox(TeamF,width=80,height=70)
    list.grid(row = 10,columnspan= 4,sticky=W+E)
    list.insert(END,"id "+ "monster "+ "velocidad "+ "salud "+ "tipo "+"ataque ")
    for i in row:
        list.insert(END,i)

    #TODO:Poner estadisticas 
    conn.commit()
    conn.close() 
#   metodo expedicion se llama para dar a a conocer los mosters que se encuuentra y los puede capturar
def ExpedicionMethod(name):
    Expedicion = Toplevel()
    Expedicion.geometry("437x300")
    Expedicion.title("Expedicion")
    conn = psycopg2.connect(
        dbname="taller3",
        user = "postgres",
        password = "root",
        host = "localhost",
        port = "5432"
    )
    cursor=conn.cursor()
    queryMonsters = '''select e.nombre from especie e'''
    cursor.execute(queryMonsters)
    row = cursor.fetchall()
    #print(row)
    lista = Listbox(Expedicion,width=20,height=5)
    lista.grid(row = 10,columnspan= 4,sticky=W+E)
    #for i in row:
     #   lista.insert(END,i)
    #muestra 1 monster
    for j in range(1):
        a = random.choice(row)
        lista.insert(END,a)
        
    label = Label(Expedicion,text='ingresar el nombre del monstruos que quieras agregar a tu equipo ')
    label.grid(row = 1 , column= 1)
    entry_monster = Entry(Expedicion)
    entry_monster.grid(row = 2, column=1)
    #boton
    #boton registrar GUI llamada a la funcion registrar_query para ingresar el usuario en la base de datos 
    #el metodo capturar es quien se encarga si captura o no el mosnter
    boton_Capturar = Button(Expedicion,text="Registrar",command=lambda:Capturar(name,entry_monster.get()))
    #boton position
    boton_Capturar.grid(row =3,column=1,sticky=W+E)
    #boton rechazar  transferir solo deja escapar el mosnter
    boton_Cancelar = Button(Expedicion,text="Trasferir",command=Expedicion.destroy)
    #boton position
    boton_Cancelar.grid(row =4,column=1,sticky=W+E) 
    conn.commit()
    conn.close() 
#cueenta los monstruos de los equipos para que eccedan los 6
def contadorMo(id):
    #id del trainer es el valor a contar 
    conn = psycopg2.connect(
        dbname="taller3",
        user = "postgres",
        password = "root",
        host = "localhost",
        port = "5432"
    )
    query = '''Select count(*) from monster where id_team = %s'''
    cur = conn.cursor()
    cur.execute(query,(id,))
    row = cur.fetchone()
    cant_monster = int(row[0])
    return cant_monster
#este da con los parametros de velocidad y salud de manera random y setea el moster si lo puede o no capturar dependiendo de las probabilidades    
def Capturar(name,entry_monster):
    conn = psycopg2.connect(
        dbname="taller3",
        user = "postgres",
        password = "root",
        host = "localhost",
        port = "5432"
    )
    
    a = random.randint(1,10)
    
    qCrearMonster = '''insert into monster(nombre, velocidad , salud , id_trainer, id_team , id_especie, id_ataque ) values (%s,%s,%s,%s,%s,%s,%s)  '''
    #nombre moster entry_monster
    #TODO:experimentar hacer una query con join
    #generar velocidad de ataque aleatoria
    velocidad = random.randint(50,100)
    #generar salud aleatoria
    salud = random.randint(70,100)
    #pedimos el id el trainer y el id del equipo 
    query_trainer = '''Select id ,id_team from trainer where nombre = %s '''
    cursor=conn.cursor()
    cursor.execute(query_trainer,(name,))
    #guardamos en una variable la respuesta de la pericion 
    row = cursor.fetchone()
    #variables indiduales
    id_trainer = row[0]
    id_team = row[1]
    contador = contadorMo(id_trainer)
    query_especie = '''select id, id_tipo , id_tipo2 from especie where nombre = %s '''
    cursor.execute(query_especie,(entry_monster, ))
    row_specie = cursor.fetchone()
    #guardamos la id de la especie
    id_especie = row_specie[0]
        #pedimos la id del monstruo ingresado y las id del tipo 

    #sacamos el nombre del tipo de ataque para buscarlo en los ataques relacionados a esa especie 
    query_tipo = '''select nombre from tipos where id = %s'''

    cursor.execute(query_tipo,(row_specie[1],))
    row_a = cursor.fetchone()
    #guardo el nombre del tipo de atque y busco su id
    query_atack = '''select id from ataque where tipo_at = %s'''
    cursor.execute(query_atack,(row_a[0],))
    row_ataque = cursor.fetchone()

    #Guardamos la id del ataque
    id_ataque = row_ataque[0]    

    if contador < 6:
        if a > 5:
            #lanzamos el sql con la query con los datos del monstruo listo
            cursor.execute(qCrearMonster,(entry_monster,velocidad,salud,id_trainer,id_team,id_especie,id_ataque))
            message = "monstruo :" + entry_monster + " ,Salud : "+ str(salud) + " ,Velocidad : ", str(velocidad)
            messagebox.showinfo("Monster Saved Successfully",message)
            conn.commit()
            conn.close() 
        else :
            messagebox.showinfo("monstruo perdido ","Tu monstruo se ha escapado, intentalo nuevamente")
    else :
        messagebox.showinfo("Equipo Completo","Lo sentimos, no podemos ingresar mas de 6 monstruos en el equipo")
        
        editarEquipo(entry_monster,name,id_especie,id_trainer,velocidad,salud,id_team,id_ataque)       
#editar equipo das el nombre del moster a reemplazar en pantalla y el metodo reemplazo hace la magia
def editarEquipo(nombre_monster,username,especie_id,id_trainer,veloc,salud,idteam,id_atack):
    Equipo = Toplevel()
    Equipo.geometry("600x300")
    Equipo.title("Edicion de equipo")
    conn = psycopg2.connect(
        dbname="taller3",
        user = "postgres",
        password = "root",
        host = "localhost",
        port = "5432"
    ) 
    query = '''Select (id, nombre, velocidad, salud) from monster where id_team = %s'''

    curr = conn.cursor()
    
    curr.execute(query,(id_trainer,))

    row = curr.fetchall()
    
    lista = Listbox(Equipo,width=30,height=7)
    lista.grid(row = 20,columnspan=5,sticky=W+E)
    lista.insert(END,'id, '+'nombre,'+' velocidad,' + ' salud')
    for i in row:
        lista.insert(END,i)

    label = Label(Equipo,text= ' Reemplazar monstruos en tu equipo ').grid(row = 1, column = 1)
    label = Label(Equipo,text='Lista de monstruos en tu equipo').grid(row = 2, column = 1)

    label = Label(Equipo,text='nombre :').grid(row = 3, column = 1)
    label = Label(Equipo,text = nombre_monster).grid(row = 3, column = 2)

    label = Label(Equipo,text='Velocidad :').grid(row = 4, column = 1)
    label = Label(Equipo,text = str( veloc)).grid(row = 4, column = 2)

    label = Label(Equipo,text = "Salud : ").grid(row = 5, column = 1)
    label = Label(Equipo,text=str (salud)).grid(row = 5, column = 2)
    
    label = Label(Equipo,text='ingresar la id del monstruos que quieras reemplazar por tu nuevo monstruo ')
    label.grid(row = 6 , column= 1)

    entry_monster = Entry(Equipo)
    entry_monster.grid(row = 7, column=1)

    boton_Reemplazar = Button(Equipo,text="Trasferir",command=lambda:Reemplazo(entry_monster.get(),
        nombre_monster,username,especie_id,id_trainer,veloc,salud,idteam,id_atack
    ))
    #boton position
    boton_Reemplazar.grid(row =8,column=1,sticky=W+E) 
 
    conn.commit()
    conn.close() 

#reemplaza un moster con otro
def Reemplazo(monster_old_id,monster_new,username,especie_id,id_trainer,veloc,salud,id_team,id_atack):
    conn = psycopg2.connect(
        dbname="taller3",
        user = "postgres",
        password = "root",
        host = "localhost",
        port = "5432"
    )
    print(monster_new+' viejo '+monster_old_id)
    cursor = conn.cursor()

    query = '''update monster set id_team = null where id = %s '''
    cursor.execute(query,(monster_old_id,))
    
    queryCreate = '''insert into monster(nombre, velocidad , salud , id_trainer, id_team , id_especie, id_ataque ) values (%s,%s,%s,%s,%s,%s,%s)'''
    cursor.execute(queryCreate,(monster_new,veloc,salud,id_trainer,id_trainer,especie_id,id_atack))
    
    
    messagebox.showinfo("reemplazo exitoso","el reemplazo se llevo a cabo satisfactoriamente")
    
        
    conn.commit()
    conn.close()    
    ShowTeam(id_team)
 
#muestra un equipo de batalla segun una id
def ShowTeam(id):
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
    query = '''SELECT * FROM monster where id_team = %s'''
    curr.execute(query,(id,))

    row = curr.fetchall()
    list =Listbox(show,width=80,height=70)
    list.grid(row = 10,columnspan= 4,sticky=W+E)

    for i in row:
        list.insert(END,i)
    conn.commit()
    conn.close()  
#muestra los mosnter que se haya topado el jugador
def CreatudexMethod(id):
    
    Creatudex = Toplevel()
    Creatudex.geometry("500x400")
    Creatudex.title("Creatudex")
    conn = psycopg2.connect(
        dbname="taller3",
        user = "postgres",
        password = "root",
        host = "localhost",
        port = "5432"
    ) 
    cursor = conn.cursor()
    query = '''select count( distinct id_especie) from monster m where id_trainer = %s'''
    cursor.execute(query,(id,))
    row = cursor.fetchone()
    label = Label(Creatudex,text='Especies atrapadas: '+ str(row[0])).grid(row=2,column= 1)
    
    query2 = '''Select count(*) from especie '''
    cursor.execute(query2,(id,))
    result=cursor.fetchone()
    faltantes = result[0] - row[0]
    label = Label(Creatudex,text='Monstruos faltantes : '+ str(faltantes)).grid(row=3,column= 1)

    query1 = '''select m.id, m.nombre, t.nombre from monster m join  especie e on m.id_especie = e.id join tipos t on t.id = e.id_tipo where m.id_trainer = %s'''

    cursor.execute(query1,(id,))

    row1 = cursor.fetchall()

    list =Listbox(Creatudex,width=80,height=70)
    list.grid(row = 10,columnspan= 4,sticky=W+E)
    list.insert(END,"id "+" nombre"+" tipo")
    for i in row1:
        list.insert(END,i)



    conn.commit()
    conn.close() 


#registro de usuario

def registrar_user():
    #ventanas
    registrar = Toplevel()
    registrar.geometry("600x200")
    registrar.title("Registrar nuevo usuario ")

    #title
    label = Label(registrar,text='Registrar al usuario ')
    label.grid(row = 0 , column= 1)

    #ingresar y capturar nombre
    label = Label(registrar,text='Ingrese su nombre  ')
    label.grid(row = 1, column= 0)
    #input
    entry_name = Entry(registrar)
    entry_name.grid(row =1 ,column=1)
    #ingresar y capturar contraseña
    label = Label(registrar,text='Ingrese su password  ')
    label.grid(row = 2 , column= 0)
    #input password
    entry_password = Entry(registrar)
    entry_password.grid(row = 2, column=1)
    #elegir el nombre de usuario
    label = Label(registrar,text='Elija un nombre de usuario ')
    label.grid(row = 3 , column= 0)
    #input username
    entry_username = Entry(registrar)
    entry_username.grid(row=3,column=1)
    #ingresar y capturar la fecha de nacimiento
    label = Label(registrar,text='Ponga fecha de nacimiento format="dia-mes-año" ')
    label.grid(row = 4 , column= 0)
    #input de la fecha
    entry_fecha = Entry(registrar)
    entry_fecha.grid(row=4,column=1)
    #ingresar y capturar la edad
    label = Label(registrar,text='Ingrese su edad  ')
    label.grid(row = 5 , column= 0)
    #input de la edad
    entry_edad = Entry(registrar)
    entry_edad.grid(row=5,column=1)
    #boton registrar GUI llamada a la funcion registrar_query para ingresar el usuario en la base de datos 
    boton_registrar = Button(registrar,text="Registrar",command=lambda:registrar_query(
        entry_name.get(),
        entry_password.get(),
        entry_username.get(),
        entry_fecha.get(),
        entry_edad.get()
        ))
    #boton position
    boton_registrar.grid(row =6,column=1,sticky=W+E) 

#definir funcion que cuente la cantidad de jugadores y la cantidad de equipos en la base para la insercion nueva
def contador():
    conn = psycopg2.connect(
        dbname = "taller3",
        user = "postgres",
        password = "root",
        host = "localhost",
        port = "5432"
    )
    cur = conn.cursor()
    query = '''Select count(*) from trainer'''
    cur.execute(query)
    row = cur.fetchone()
    print(row)

    return row[0]

#funcion registrar query
def registrar_query(name,password,username,fecha,edad):
    #conexion a la base de datos
    conn = psycopg2.connect(
        dbname = "taller3",
        user = "postgres",
        password = "root",
        host = "localhost",
        port = "5432"
    )
    #query 
    cur = conn.cursor()
    id_team = contador() + 1
    query = '''INSERT INTO trainer (nombre, password ,username ,id_team , fecha_nac , edad) VALUES (%s,%s,%s,%s,%s,%s)'''

    cur.execute(query,(name , password , username, id_team , fecha , edad))
    
    print("data saved !!")
    conn.commit()
    conn.close()
    #llamada a un metodo mostrar para ver que usuarios estan registrados
    show()
#funcion para mostrar los usuarios registrados solo de prueba sacar problemas de seguridad
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
    query = '''SELECT nombre FROM trainer '''
    curr.execute(query)

    row = curr.fetchall()
    list =Listbox(show,width=80,height=70)
    list.grid(row = 10,columnspan= 4,sticky=W+E)

    for i in row:
        list.insert(END,i)
    conn.commit()
    conn.close()  
#menu principal login donde se llama a la pantalla principal 
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
#program begin
pantallLogin()
root.mainloop()