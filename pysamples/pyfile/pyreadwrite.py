#!/usr/bin/env python3

"""
|操作模式    |具体含义
|'r'         |读取 （默认）
|'w'         |写入（会先截断之前的内容）
|'x'         |写入，如果文件已经存在会产生异常
|'a'         |追加，将内容写入到已有文件的末尾
|'b'         |二进制模式
|'t'         |文本模式（默认）
|'+'         |更新（既可以读又可以写）
"""

def readWrite():
    try:
        with open("./timg.jpg", "rb") as f1:
            with open("./timg_replication.jpg", "wb") as f2:
                for line in f1:
                    f2.write(line)
    except Exception as ex:
        raise ex
    finally:
        print("read and write done")

if __name__ == "__main__":
    try:
        readWrite()
    except FileNotFoundError:
        print("No such file")
    except UnicodeDecodeError:
        print("read file with decode error")
        
        