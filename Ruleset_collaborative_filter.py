import psycopg2

connection = psycopg2.connect("dbname=postgres user=postgres password=50cent")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS collab CASCADE")
cursor.execute("""CREATE TABLE collab
                (id VARCHAR PRIMARY KEY,
                 prodid VARCHAR);""")

postgreSQL_select_products_Query = "SELECT * FROM profiles, profiles_previously_viewed WHERE id = profid"

cursor.execute(postgreSQL_select_products_Query)
print("Selecting rows from products table using cursor.fetchall")
profiles_records = cursor.fetchall()

print("Adding all profiles to a set")
profiles_with_products = []
for row in profiles_records:
    profiles_with_products.append((row[0], row[4]))

for profile in profiles_with_products:
    cursor.execute("""INSERT INTO collab (id, prodid) VALUES (%s, %s)""", profile)
connection.commit()

cursor.close()
connection.close()
print("PostgreSQL connection is closed")