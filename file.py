import mysql.connector

# Conexion Py con SQL DB remote
mydb = mysql.connector.connect(
    host= "192.168.1.13",
    user= "UserLaptop",
    password= "sebasmesi1305",
    database= "practicapy"    
)

mycursor = mydb.cursor()

COND_start = int(input("""
                       Que opcion desea 1. 
                       1. añadir
                       2. consultar
                       /> """))

if  COND_start == 1:
    name = input("Digame su nombre: ")
    last_name = input("Digame su apellido: ")
    age = int(input("Digame su edad: ")) 
    email = input("Digame su email: ")

    query = "INSERT INTO users (name, last_name, age, email) VALUES(%s, %s, %s, %s)"
    val = (name, last_name, age, email)

    mycursor.execute(query, val)
    mydb.commit()
    print(mycursor.rowcount, "registro(s) insertado(s) correctamente en ID", mycursor.lastrowid)
elif  COND_start == 2:
    query = "SELECT name, age FROM users WHERE age ORDER BY age ASC;"
    mycursor.execute(query)
    
    myresult = mycursor.fetchall()
    for row in myresult:
        print(row)

else:
    print("Opcion no valida")