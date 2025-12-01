# import mysql.connector
# from mysql.connector import Error

# try:
#     # Try to connect to MySQL
#     conn = mysql.connector.connect(
#         host = 'localhost',
#         user = 'root',
#         password = 'S@ndeep9347vs', #your mysql password
#         database = '59r',
#         autocommit = False
#     )

#     if conn.is_connected():
#         print("Connected to MySQL database")

#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM employees")

#     rows = cursor.fetchall()

# except Error as e:
#     print("Error while connecting to MySQL:", e)

# else:
#     print("Query executed successfully!")
#     for row in rows:
#         print(row)

# finally:
#     if 'conn' in locals() and conn.is_connected():
#         conn.close()
#         print("MySQL connection closed.")
