#! /usr/bin/python3

import sqlite3 #导入sqlite3模块 

if __name__ == '__main__':
    
    #连接数据库
    conn = sqlite3.connect("sf.db")

    #创建游标对象
    cursor = conn.cursor()

    #查询数据
    rows = cursor.execute("select * from customer;")

    #获取结果集 把记录转换成字典对象并装入数组
    columns = [col[0] for col in cursor.description]
    results = [dict(zip(columns,row)) for row in rows]
    

    #打印结果集
    for row in results:
        print(row)

    # 关闭游标和连接 
    cursor.close()
    cursor.close()
    
    

