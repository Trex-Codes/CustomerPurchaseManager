import mysql.connector
import re

global email_verify

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
    return re.match(pattern,email_patter) is not None

# Create new email (account) into the DB 
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
        
# Update personal information of the client that already have account 
def  Update_info():
    global  email_verify


    while True:
        info_specific = int(input("""Which details you would to change it:
                                    1. Legal name
                                    2. phone number
                                    3. email
                                    4. city and address 
                                    >/: 
            
                                """))
        # update legal name
        if info_specific == 1:
                legal_nameChanged = input("Which is your new legal name: ")
                
                if legal_nameChanged == "":
                    print("Enter a valid name")
                else:
                    query = "UPDATE cliente SET nombre = %s WHERE email = %s"
                        
                    mycursor.execute(query, (legal_nameChanged, email_verify))
                    mydb.commit()   
                    print("Your legal name has been successfully changed!!") 
        
        # update phone number 
        if info_specific == 2:
            phoneNumber_changed = input("Which is your new phone number (use indicative): ")
            query = "UPDATE cliente SET telefono =  %s WHERE email = %s"
            
            mycursor.execute(query, (phoneNumber_changed, email_verify))
            mydb.commit()
            print("Your phone number has been successfully changed!!")

        # update email address 
        if  info_specific == 3:
            email_changed = input("Which is your new email address: ")
            
            if (Validation_email(email_changed)):
                
                query_1 = "SELECT * from cliente  WHERE email = %s"
                mycursor.execute(query_1, (email_changed,))
                myresult = mycursor.fetchall()
                
                if (len(myresult) > 0):
                    print("This email is already in use!!, try another one")
                else:
                    query_2 = "UPDATE cliente SET email = %s WHERE email = %s"
                
                    mycursor.execute(query_2, (email_changed, email_verify))
                    mydb.commit()
                    
                    """ After to update the email, that new one may be equal
                    as the first input when they start the program to validate
                    again on the DB """
                    email_verify = email_changed  
                    print("Your email address has been successfully changed!!")
            else:
                print("Enter a valid email")
                
        # update city and address 
        if  info_specific == 4:
            city_changed = input("Which is your new city: ")
            address_changed = input("Which is your new address: ")
            
            query_cityAddr = "UPDATE cliente SET ciudad = %s, direccion = %s WHERE email = %s;"
            mycursor.execute(query_cityAddr,  (city_changed, address_changed, email_verify))
            mydb.commit()
            print("Your  city and address has been successfully changed!!")

        if  info_specific == 5:
            break;






        
                
                

        


Messgae_Starting ="Welcome, please login with your credentials"
print(Messgae_Starting.upper())

# email request to verify the client
email_verify = input("Email: ")

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
                                    2. Delete your information
                                    3. Find the list of products that you  have purchased
                                    4. Buy a new product -- 
                                """)
    if login_acces_won == "1":
        Update_info()
    else:
        print("Option no valid, create an account")
        Create_email() 
else:
    print("Email is not valid")
    
    