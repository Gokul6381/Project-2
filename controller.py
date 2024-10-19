import json
import mysql.connector


def jsonData():
    with open ('flight_data.json') as file:
        data=json.load(file)
    return data  


def insert_data(form,file):
        
    with open(file,'r') as json_file:
            data=json.load(json_file)

    data.append(form)
        
    with open(file,'w') as json_file:
        json.dump(data, json_file, indent=4)






def connect_db():
    connect=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='madras_flight'   
    )
    return connect

def insert(query):
    connect=connect_db()
    cursor=connect.cursor()
    cursor.execute(query)
    connect.commit()
    connect.close()


def redrive_1(query):
    connect=connect_db()
    cursor=connect.cursor()
    cursor.execute(query)
    data=cursor.fetchone()
    connect.close()
    return data

def redrive_all(query):
    connect=connect_db()
    cursor=connect.cursor()
    cursor.execute(query)
    data=cursor.fetchall()
    connect.close()
    return data




def crt_flight_data():
    data=jsonData()

    for i in range(0,len(data)):
        query=f"""insert into flight_data(flight_id,air_line,origin,destination,departure,price)  values('{data[i]['flight_number']}','{data[i]['flight_company']}','{data[i]['from']}','{data[i]['to']}','{data[i]['date_time']}','{data[i]['price_in_rupees']}');"""
        insert(query=query)


