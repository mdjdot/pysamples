import pymysql


def getConn():
    conn = pymysql.connect(
        host="127.0.0.1",
        port=1306,
        database="appdb",
        charset="utf8",
        user="root",
        password="roottest"
    )
    return conn


def addUser(name):
    try:
        conn = getConn()
        with conn.cursor() as cursor:
            result = cursor.execute(
                "insert into users (name) values (%s)", name
            )
            if result == 1:
                conn.commit()
                return True
    except Exception as ex:
        print(ex)
        return False
    finally:
        conn.close()


def queryUser(name):
    try:
        conn = getConn()
        with conn.cursor() as cursor:
            cursor.execute(
                "select id, name from users where name=%s", name
            )
            result = cursor.fetchone()
            return result
    except Exception as ex:
        print(ex)
        return ""
    finally:
        conn.close()


if __name__ == "__main__":
    addUser("张三")
    queryUser("张三")
