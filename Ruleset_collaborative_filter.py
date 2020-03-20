import psycopg2

connection = psycopg2.connect("dbname=postgres user=postgres password=50cent")
cursor = connection.cursor()
postgreSQL_select_products_Query = "SELECT * FROM profiles, profiles_previously_viewed WHERE id = profid"

cursor.execute(postgreSQL_select_products_Query)
print("Selecting rows from products table using cursor.fetchall")
profiles_records = cursor.fetchall()


print("Print each row and it's columns values")
teller = 0
profiles_with_products = {}
for row in profiles_records:
    teller += 1
    profiles_with_products.add(row[0])
    profiles_with_products.add(row[4])

print(teller)
print(profiles_with_products)

cursor.close()
connection.close()
print("PostgreSQL connection is closed")