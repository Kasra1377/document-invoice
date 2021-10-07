import mysql.connector

# connect Python to MySQL database in order to 
# pass the employees info into the database
# specify the name of database of the table that you want to
# pass the informations into that 
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="kasra1377",
    database="documents",
)

def insert_table(instance):
    try:
        mycursor = mydb.cursor()
        query = "INSERT INTO documents (name, last_name, gender, email, city, state, zip_code) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        mycursor.execute(query, list(instance.values()))

        mydb.commit()
        print(mycursor.rowcount, "record inserted successfully.")

    except Exception as e:
        print("QUERY ERROR : ",e)