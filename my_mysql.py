import pymysql
def get_data(data):
    conn = pymysql.connect("xxxxxxxx", "xxxxx", "xxxxx", "xxxxx",charset='utf8')
    cursor = conn.cursor()
    values=''
    try:
        data = data.split(' ')
        if data[0]=='手机号':
            cursor.execute('SELECT * FROM 学生信息 WHERE 手机号= %s', (data[1],))
            values = cursor.fetchall()
        elif data[0] == '学号':
            cursor.execute('SELECT * FROM 学生信息 WHERE 学号 = %s', (data[1],))
            values = cursor.fetchall()
        elif data[0]=='qq' or data[0]=='QQ':
            cursor.execute('SELECT * FROM 学生信息 WHERE 邮箱 LIKE %s', (data[1],))
            values = cursor.fetchall()
        elif data[0]=='姓名' or data[0]=='QQ':
            cursor.execute('SELECT * FROM 学生信息 WHERE 姓名 = %s', (data[1],))
            values = cursor.fetchall()
        cursor.close()
        conn.commit()
        conn.close()
        s = ''
        for i in values[0]:
            s = s+" "+str(i)
        return s.strip()
    except:
        return "没有找到信息或输入格式有误(用一个空格分开)，格式如下：\n姓名 xxx；qq xxx；学号 xxx；手机号 xxx"

if __name__ == '__main__':
    print(get_data(''))
