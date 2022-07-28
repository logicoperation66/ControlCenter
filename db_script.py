import os
import sys
import mysql.connector


#Take data from DB
connection = mysql.connector.connect(user="admin", password="passw.txt", host="vpsdb.cmrwutxibrqt.eu-west-1.rds.amazonaws.com",
                                    database="awsvps", auth_plugin="mysql_native_password")

query = 'SELECT id, username, ami FROM users'

cursor = connection.cursor()
cursor.execute(query)

for row in cursor:
    print(row)



# vps_name = sys.argv[-1]
#
# os.system(f"touch {vps_name}.txt")