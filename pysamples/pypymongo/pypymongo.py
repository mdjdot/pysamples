import pymongo


def getConn():
    conn = pymongo.MongoClient("mongodb://dm:dmtest@127.0.0.1:27017/appdb")
    # conn = pymongo.MongoClient(
    #     host="127.0.0.1",
    #     port=27017,
    # )
    return conn


def setDocument():
    conn = getConn()
    db = conn.get_database(name="appdb")
    col = db.get_collection(name="logs")
    result = col.insert_one({"user":"张三","age":18,"friends":[{"name":"李四"},{"name":"王五"}]})
    print(result.acknowledged)
    


def getDocument():
    conn = getConn()
    db = conn.get_database(name="appdb")
    col = db.get_collection(name="logs")
    result = col.find_one()
    return result


if __name__ == "__main__":
    # setDocument()
    print(getDocument())
