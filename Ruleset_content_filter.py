import psycopg2

connection = psycopg2.connect("dbname=postgres user=postgres password=50cent")
cursor = connection.cursor()
postgreSQL_select_products_Query = "SELECT * FROM products"

cursor.execute(postgreSQL_select_products_Query)
print("Selecting rows from products table using cursor.fetchall")
products_records = cursor.fetchall()


print("Print each row and it's columns values")
teller = 0
for row in products_records:
    if row[6] == None:
        continue
    else:
        teller += 1
        print("ID = ", row[0])
        print("Name = ", row[1])
        print("Category = ", row[4])
        print("Subcategory = ", row[5])
        print("Subsubcategory = ", row[6], "\n")

print(teller)

cursor.close()
connection.close()
print("PostgreSQL connection is closed")