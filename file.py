import mysql.connector
import re
import os
import sys
import io
import time
from tabulate import tabulate

# Configurar la codificación de salida a UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Variable to update the email on file 
global email_verify

# Conexion Py con SQL DB remote
mydb = mysql.connector.connect(
     host="localhost",        # Dirección del servidor MySQL
    user="root",       # Tu usuario MySQL
    password="Sebasmesi1305",# Tu contraseña MySQL
    database="company" # Nombre de la base de datos"    
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
        os.system('clear')
        info_specific = int(input("""
        Which details you would to change it:
        1. Legal name
        2. phone number
        3. email
        4. city and address 
        >/: 
        """))
        
        # update legal name
        if info_specific == 1:
                os.system('clear')
                
                legal_nameChanged = input("Which is your new legal name: ")
                
                if legal_nameChanged == "":
                    print("Enter a valid name")
                else:
                    query = "UPDATE cliente SET nombre = %s WHERE email = %s"
                        
                    mycursor.execute(query, (legal_nameChanged, email_verify))
                    mydb.commit()   
                    print("Your legal name has been successfully changed!!") 
                    time.sleep(2)
        
        # update phone number 
        if info_specific == 2:
            os.system('clear')
            
            phoneNumber_changed = input("Which is your new phone number (use indicative): ")
            query = "UPDATE cliente SET telefono =  %s WHERE email = %s"
            
            mycursor.execute(query, (phoneNumber_changed, email_verify))
            mydb.commit()
            print("Your phone number has been successfully changed!!")
            time.sleep(2)

        # update email address 
        if  info_specific == 3:
        
            while True:
                os.system('clear')
            
                email_changed = input("Which is your new email address: ")
            
                if (Validation_email(email_changed)):
                
                    query_1 = "SELECT * from cliente  WHERE email = %s"
                    mycursor.execute(query_1, (email_changed,))
                    myresult = mycursor.fetchall()
                    
                    if (len(myresult) > 0):
                        print("This email is already in use!!, try another one")
                        time.sleep(2)
                    else:
                        query_2 = "UPDATE cliente SET email = %s WHERE email = %s"
                    
                        mycursor.execute(query_2, (email_changed, email_verify))
                        mydb.commit()
                        
                        """ After to update the email, that new one may be equal
                        as the first input when they start the program to validate
                        again on the DB """
                        email_verify = email_changed  
                        print("Your email address has been successfully changed!!")
                        time.sleep(2)
                        break;
                else:
                    print("Enter a valid email")
                    time.sleep(2)
                
        # update city and address 
        if  info_specific == 4:
            os.system('clear')
            
            city_changed = input("Which is your new city: ")
            address_changed = input("Which is your new address: ")
            
            query_cityAddr = "UPDATE cliente SET ciudad = %s, direccion = %s WHERE email = %s;"
            mycursor.execute(query_cityAddr,  (city_changed, address_changed, email_verify))
            mydb.commit()
            print("Your  city and address has been successfully changed!!")
            time.sleep(2)

        if  info_specific == 5:
            break;

# Delete all the information related with that email

def Delete_info():
    os.system('clear')
    
    # First we need to find  the id related with the email
    query_1 = "SELECT cliente_id FROM cliente WHERE email = %s" 
    mycursor.execute(query_1, (email_verify,))
    myresult = mycursor.fetchall()

    """ find the ID related with that email
        and shows as int """
    data = myresult
    data_int = data[0][0]

    # Confirm to delete the row
    sure = input("s/n: ")
    if sure  == "y":
        query_2 = "DELETE FROM cliente WHERE cliente_id  = %s"
        mycursor.execute(query_2, (data_int,))
        mydb.commit()
        print("Your information has been successfully deleted!!")
        exit()

# Find the products related with that specific client
def Find_products():
    os.system('clear') 
    print("You will see all the products related with your information",'\n')
    
    # Find the ID of the cx to show the products that they have    
    query_id = "SELECT cliente_id FROM cliente WHERE email = %s"
    mycursor.execute(query_id,  (email_verify,))
    result = mycursor.fetchall()
    valor = result[0][0] # Get Value INT of the ID of the client
    
    query_product = """
SELECT
	cliente.cliente_id,
    cliente.nombre,
    venta.cantidad,  
    venta_producto.venta_id AS "ID VENTA venta_producto",
    venta_producto.producto_id AS "ID PRODUCTO venta_producto",
    producto.descripcion,
    producto.tipo_producto,
    categoria,
    producto.precio,
    SUM(producto.precio * venta.cantidad) AS "VALOR PAGADO"
FROM cliente 
JOIN venta ON cliente.cliente_id = venta.cliente_id
JOIN venta_producto ON venta.venta_id = venta_producto.venta_id
JOIN producto ON venta_producto.producto_id = producto.producto_id
JOIN tipo_producto ON tipo_producto.tipo_producto_id = producto.tipo_producto
WHERE cliente.cliente_id = %s
GROUP BY 
    cliente.cliente_id,
    cliente.nombre,
    venta_producto.venta_id,
    venta_producto.producto_id,
    producto.descripcion,
    producto.tipo_producto,
    tipo_producto.categoria,
    producto.precio;"""

    mycursor.execute(query_product, (valor,))
    result_query = mycursor.fetchall()

    # name column required by Quey
    column_names = [i[0] for i in mycursor.description]
    print(tabulate(result_query, headers=column_names, tablefmt="fancy_grid", floatfmt=".3f"))

    input("\n Press enter to go  back to the main menu...")

# Buy a new product for the customer 
def Buy_product():
    def encapsulation_buyOptions(option_tipeProduct):
        
        os.system('clear')
        print(f"you have select {option_tipeProduct}")
        
        # Query table (producto) with ID = x, products with that ID 
        query_case = "SELECT producto_id, descripcion, precio FROM producto WHERE tipo_producto = %s;"
        mycursor.execute(query_case, (option,))
        result_case = mycursor.fetchall()
    
        print(tabulate(result_case, headers=['ID', 'Desccription', 'Cost'], tablefmt="fancy_grid", floatfmt=".3f"))
    
        # quantify and ID of the specific product in those variables    
        product_choose = int(input("Tell me the ID of the product that you want: "))
        product_choose_quanty = int(input("Tell me the Quantity of the product: "))
        
        """ 1. we need to add in venta (valor, product_choose_quanty) -- valor its the ID of the cx 
            2. add to venta_producto el venta_id created for the new sell and the product ID for the cx selected
      
        """
        
        # SECTION 1 
        #  Add to table (venta) the new sell with the customer ID and the value of the product
        
        query_ID_insert = "INSERT INTO venta (cliente_id, cantidad) VALUES (%s, %s);"
        mycursor.execute(query_ID_insert, (valor, product_choose_quanty))
        mydb.commit()
        
        # SECTION 2
        # With a another Query we identify the venta_id of table (venta) that we need to add into venta_producto
        # get the size of the tuples in the table 
        
        TUPLE_count = "SELECT COUNT(*) AS total_fila FROM venta;"
        mycursor.execute(TUPLE_count)
        result_case = mycursor.fetchall()
            
        result_TUPLE = result_case[0][0] # show a value type INT | The last venta_id  into the table
        query_ID_insert_product = "INSERT INTO venta_producto (venta_id, producto_id) VALUES (%s, %s);"
        mycursor.execute(query_ID_insert_product, (result_TUPLE, product_choose))
        mydb.commit()
                      
    os.system('clear')

    """
        1. find  the ID of the client on the DB 
        2. get the ID of the product that they want from Table (tipo_producto)
        3. Depends of the option, they will see the table (producto) related with his ID 
        4. in each case, we wil ask for the ID of specific product of table (producto) 
           and also que quantity
        
        TO INSERT THE DATA ON DB
        5. table (venta) we add the ID of the client and the quantity of the product 
        6. table (venta_producto) we add the ID of the venta and the ID of the product 
    """
    
    query_id = "SELECT cliente_id FROM cliente WHERE email = %s"

    mycursor.execute(query_id,  (email_verify,))
    result = mycursor.fetchall()
    valor = result[0][0] # Get Value INT of the ID of the client
    

    print(f"your ID it's {valor}")
    print("Now we are going to show your the products: ","\n")
    
    # Query types of products 
    query_product = "SELECT * FROM tipo_producto;"
    mycursor.execute(query_product)
    result_product = mycursor.fetchall()

    print(tabulate(result_product, headers=['ID', 'Category'], tablefmt="fancy_grid"))

    # Input with function of to show the specifics products depending on the ID selected
    print("\nnow select the category\n")
    
    option = int(input("Select option case: "))
    Option_case = encapsulation_buyOptions(option) if 1 <= option <= 9 else "option not found" 
    os.system('clear')
    print(Option_case)
    input("Enter to go back.. ")


# ----------- START -----------          
Messgae_Starting ="Welcome, please login with your credentials"
print(Messgae_Starting.upper())

# email request to verify the client
# email_verify = "carlos@gmail.com"
email_verify = input("Email: ")

while True:
    os.system('clear')

    if Validation_email(email_verify):
        
        #  validate that the client has a email on file 
        query = "SELECT * FROM cliente WHERE email = %s"
        
        mycursor.execute(query,(email_verify,))
        result = mycursor.fetchall()
        
        # Validate if the  email is on the DB
        if len(result) >  0:
            
            print("Client Exist, now  you can login")
            login_acces_won = input("""
                Now which options you would like to do:
                1. Update your personal information
                2. Delete your information
                3. Find the list of products that you  have purchased
                4. Buy a new product --
                >/: """)
            
            if login_acces_won == "1":
                os.system('clear')
                Update_info()
            elif  login_acces_won == "2":
                os.system('clear')
                Delete_info()
            elif  login_acces_won == "3":
                os.system('clear')
                Find_products()
            elif login_acces_won == "4":
                os.system('clear')
                Buy_product()
            elif  login_acces_won == "5":
                break;
        else:
            print("Option no valid, create an account")
            Create_email()
            break;
    else:
        print("Email format is not valid")
        break