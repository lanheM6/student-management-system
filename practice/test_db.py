import pymysql
conn = pymysql.connect(
    host='localhost',      # 数据库在哪？本机就是 localhost
    user='root',           # 用户名，你装 MySQL 时默认就是 root
    password='在这里填你的密码',    # ⚠️ 这里换成你自己 MySQL 的密码！千万别直接抄我的
    database='student_ms', # 我们要连刚才建好的那个“文件夹”
    charset='utf8mb4'      # 处理中文的编码
)

cursor = conn.cursor()

sql = "INSERT INTO users (sid, passwd, sname, role) VALUES ('admin', '123456', '管理员', 'admin')"
cursor.execute(sql)

conn.commit()
print("管理员数据插入成功！")

cursor.execute("SELECT * FROM users")
result = cursor.fetchall()
print("当前数据库里的数据：")
for row in result:
    print(row)

# 关门
cursor.close()
conn.close()
