import mysql.connector

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='sportschool')
cursor = cnx.cursor()

query = ("SELECT firstname, email FROM users ")

cursor.execute(query)

firstname = []
email = []

for x in cursor:
    firstname.append(x[0])
    email.append(x[1])

if 'Richie' in firstname and 'richietjin@gmail.com' in email:
    print('welkom')
else:
    print('wellou')
cursor.close()
cnx.close()