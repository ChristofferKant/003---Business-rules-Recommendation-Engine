import psycopg2

connection = psycopg2.connect("dbname=postgres user=postgres password=50cent")
cursor = connection.cursor()

# print postgreSQL connection properties
print(connection.get_dsn_parameters(),"\n")

# print postgreSQL version
cursor.execute("SELECT version();")
record = cursor.fetchone()
print("You are connected to - ", record, "\n")

cursor.close()
connection.close()
print("PostgreSQL connection is closed")