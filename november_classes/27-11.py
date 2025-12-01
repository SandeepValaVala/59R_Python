import mysql.connector


conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'S@ndeep9347vs', #your mysql password
    database = '59r',
    autocommit = False
    # port = 13988 # remote mysql server to connect in another  mysql workbench serverr too use aiven.console 
    
)

cursor = conn.cursor()
# cursor.execute('SHOW TABLES')
# print(cursor.fetchall())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchmany(3))

print(conn.is_connected())#  it will give boolean values likke (true /false)

# ACID  --

# cursor.execute('''
#     CREATE TABLE movies (
#         id INT PRIMARY KEY AUTO_INCREMENT,
#         name varchar(60)
#     )         
# ''')

# id = int(input('Enter id :'))
# movie_name = input('Enter movie name :')

# cursor.execute('''
#     INSERT INTO movies (name) values('%s, %s')               
# ''', (5, 'og')) #(id,movie_name)

# conn.commit()


cursor.close()
conn.close()
