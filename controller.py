import json
import mysql.connector

def jsonData():
    with open ('flight_data.json') as file:
        data=json.load(file)
    return data  


def cnt_db(query):
    connect=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='flight_list'   
    )

    cursour=connect.cursor()
    cursour.execute(query)
    data=cursour.fetchall()
    return data

def close_db(connect):
    connect.close()


def insert_data(form):
        
    file=r'Book_data.json'

    with open(file,'r') as json_file:
            data=json.load(json_file)

    data.append(form)
        
    with open(file,'w') as json_file:
        json.dump(data, json_file, indent=4)