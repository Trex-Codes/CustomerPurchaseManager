
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
product_choose = 0;


# mostar al cliente que ID es y al mismo tiempo ofrecerle los productos 

email = "carlos@gmail.com"

query_id = "SELECT cliente_id FROM cliente WHERE email = %s"

mycursor.execute(query_id,  (email,))
result = mycursor.fetchall()

valor = result[0][0]

print(f"your ID it's {valor}")
print("Now we are going to show your the products: ","\n")

Query types of products 
query_product = "SELECT * FROM tipo_producto;"
mycursor.execute(query_product)
result_product = mycursor.fetchall()

for row in result_product:
    print(row)
    
print("\nnow select the category\n")

option = int(input("Select option case: "))

if option == 1:
    print("you selected option 1")
    query_case = "SELECT producto_id, descripcion, precio FROM producto WHERE tipo_producto = %s;"
    mycursor.execute(query_case, (option,))
    result_case = mycursor.fetchall()
    
    for i in result_case:
        print(i)
        
    product_choose = int(input("Tell me the ID of the product that you want: "))
    product_choose_quanty = int(input("Tell me the Quantity of the product: "))
    
    print("Product selected at your order!!, thaks")
     
    # INSERT DATA IN DB
    # 1. we need to add in venta (valor, product_choose_quanty)
    # 2. add to venta_producto el venta_id created for the new sell and the product id for the cx selected
    
    # SECTION 1 
    query_ID_insert = "INSERT INTO venta (cliente_id, cantidad) VALUES (%s, %s);"
    mycursor.execute(query_ID_insert, (valor, product_choose_quanty))
    mydb.commit()
    
    # SECTION 2
    
    # get the size of the tuples in the table 
    TUPLE_count = "SELECT COUNT(*) AS total_fila FROM venta;"
    mycursor.execute(TUPLE_count)
    result_case = mycursor.fetchall()
        
    result_TUPLE = result_case[0][0]
    print(type(result_TUPLE)) 
    
    query_ID_insert_product = "INSERT INTO venta_producto (venta_id, producto_id) VALUES (%s, %s);"
    mycursor.execute(query_ID_insert_product, (result_TUPLE, product_choose))
    mydb.commit()
