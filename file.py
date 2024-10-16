import mysql.connector
import re

# Conexion Py con SQL DB remote
mydb = mysql.connector.connect(
    host= "192.168.1.13",
    user= "UserLaptop",
    password= "sebasmesi1305",
    database= "company"    
)

# Initiate instance of use MYSQL
mycursor = mydb.cursor()

def Validation_email(email_patter):
    pattern = r"^[\w.-]+@([\w-]+\.)+[\w-]{2,4}$" 
    return re.match(pattern,email_verify) is not None

def Create_email():
        
        # Request to the new user, the new information to create a row
        datos = ["nombre", "edad", "telefono", "ciudad", "direccion"]
        data_saved = []
        for i in range(len(datos)):
            data = input(f"digame su {datos[i]}: ")
            data_saved.append(data)
        
        # query to insert the new information of the client on the DB 
        query = "INSERT INTO cliente (nombre, edad, telefono, email, ciudad, direccion) VALUES (%s, %s, %s, %s, %s, %s);"
        val = (data_saved)
        data_saved.insert(3,email_verify) # list with all the information requested ready to go on DB!!
        
        mycursor.execute(query, val)
        mydb.commit()
        print(mycursor.rowcount, "Register(s) inserted in right way!")
        

Messgae_Starting ="Welcome, please login with your credentials"
print(Messgae_Starting.upper())

# email request to verify the client
email_verify = input("Email: ")
Validation_email(email_verify)

if Validation_email(email_verify):
    
    #  validate that the client has a email on file 
    query = "SELECT * FROM cliente WHERE email = %s"
    
    mycursor.execute(query,(email_verify,))
    result = mycursor.fetchall()
    
    # Validate if the  email is on the DB
    if len(result) >  0:
        print("Client Exist, now  you can login")
        login_acces_won = input("""Now which options you would like to do:
                                    1. Update your personal information
                                    2. Delete your information3
                                    3. Find the list of products that you  have purchased
                                    4. Buy a new product -- 
                                """)
    else:
        print("Client does not exist, please register first")
        Create_email() 
else:
    print("Email is not valid")
    
    