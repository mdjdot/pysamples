#!/usr/bin/env python3

import sqlite3

def getConn():
    conn = sqlite3.connect("appdb.db")
    return conn

def addUser():
    conn = getConn()
    cursor = conn.cursor()
    cursor.execute('create table users (id int primary key,name varchar(20) not null)')
    cursor.execute('insert into users (id,name) values (1,"张三")')
    cursor.close()
    conn.close()
 
def getUser():
    conn = getConn()
    cursor = conn.cursor()
    cursor.execute('select id,name from users where id=?',("1",))
    value=cursor.fetchone()
    cursor.close()
    conn.close()   
    return value

if __name__ == "__main__":
    # addUser()
    print(getUser())
