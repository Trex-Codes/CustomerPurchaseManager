
import mysql.connector
import re
import os
import time

# Variable to update the email on file 
global email_verify 
email_verify = "dfd@gmai.com"

# Conexion Py con SQL DB remote
mydb = mysql.connector.connect(
    host= "192.168.1.13",
    user= "UserLaptop",
    password= "sebasmesi1305",
    database= "company"   
)

mycursor = mydb.cursor()

qury_case = 0;
result_case = 0;
# mostar al cliente que ID es y al mismo tiempo ofrecerle los productos 

email = "carlos@gmail.com"

query_id = "SELECT cliente_id FROM cliente WHERE email = %s"

mycursor.execute(query_id,  (email,))
result = mycursor.fetchall()

valor = result[0][0]

print(f"your ID it's {valor}")
print("Now we are going to show your the products: ")

# Query types of products 

query_product = "SELECT * FROM tipo_producto;"
mycursor.execute(query_product)
result_product = mycursor.fetchall()

# for row in result_product:
    # print(row)
    
print("now select the category")

option = int(input("Select option case: "))

if option == 1:
    print("you selected option 1")
    query_case = "SELECT producto_id, descripcion, precio FROM producto WHERE tipo_producto = %s;"
    mycursor.execute(query_case, (option,))
    result_case = mycursor.fetchall()
    
    for i in result_case:
        print(i)
    
elif option == 2:
    print("you selected option 2")
    query_case = "SELECT producto_id, descripcion, precio FROM producto WHERE tipo_producto = %s;"
    mycursor.execute(query_case, (option,))
    result_case = mycursor.fetchall()
    
    for i in result_case:
        print(i)
