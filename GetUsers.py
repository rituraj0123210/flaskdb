import sqlite3
import json
def getAllusers():
    conn=sqlite3.connect("my_medicalShop.db")
    cursor= conn.cursor()
    cursor.execute("SELECT * From User")
    users= cursor.fetchall()
    conn.close()
   
    userJson=[]
    for user in users:
        tempUser= {
        "id": user[0],
        "user_id": user[1],
        "password"  : user[2] ,
        "Level": user[3],
        "DateOfAccountCreation": user[4],
        "approved": user[5],
        "Block": user[6],
        "name": user[7]  ,
        "Address": user[8] ,
        "email": user[9] ,
        "phone": user[10] ,
        "PinCode": user[11]    
        }

        userJson.append(tempUser)

    return json.dumps(userJson)

    
def getSpecificUsers(userId):
    conn=sqlite3.connect("my_medicalShop.db")
    cursor= conn.cursor()
    cursor.execute("SELECT * From User WHERE user_id=?", (userId))
    users= cursor.fetchall()
    conn.close()
   
    userJson=[]
    for user in users:
        tempUser= {
        "id": user[0],
        "user_id": user[1],
        "password"  : user[2] ,
        "Level": user[3],
        "DateOfAccountCreation": user[4],
        "approved": user[5],
        "Block": user[6],
        "name": user[7]  ,
        "Address": user[8] ,
        "email": user[9] ,
        "phone": user[10] ,
        "PinCode": user[11]    
        }

        userJson.append(tempUser)

    return json.dumps(userJson)


