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
                       3. actualizar
                       /> """))
# Agregar en la DB 
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
    
# Consultar en la DB 
elif  COND_start == 2:
    query = "SELECT * FROM users;"
    mycursor.execute(query)
    
    myresult = mycursor.fetchall()
    for row in myresult:
        print(row)
        
elif  COND_start == 3:
    user_id = int(input("Dime su ID: "))
    new_email = input("Digame su nuevo email:")
    
    
    query1= "SELECT * FROM users WHERE user_id = %s"
    query2 = "UPDATE users SET email =  %s WHERE user_id = %s"
    
    # Query1 find the row with that ID
    mycursor.execute(query1, (user_id,))
    myresult = mycursor.fetchall()
    
    # If the ID for the input exists in the DB
    if(len(myresult) > 0):
        # Query2 update the email related with the ID
        mycursor.execute(query2, (new_email, user_id))
        mydb.commit()
        print(mycursor.rowcount, "Regsitro(s) acutalizado(s) correctamente en ID", mycursor.lastrowid)
        
        for row in myresult:
            print(row)  
    else:
        print("Ese ID no existe en la DB")
else:
    print("Opcion o valida")