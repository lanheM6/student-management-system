import unicodedata

import pymysql

#安全防泄露

# 密码不写在代码里，从同目录的 db_config.py 读
# （Python 会把“脚本自己所在的目录”加进模块搜索路径，
#   所以 db_config.py 和本文件放在一起就能直接 import）
# db_config.py 已在 .gitignore 里，不会被提交到 GitHub
from db_config import DB_CHARSET, DB_HOST, DB_NAME, DB_PASSWORD, DB_USER

# 1. 建立连接（搭桥）
conn = pymysql.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME,
    charset=DB_CHARSET,
)

# 2. 拿笔（游标）
cursor = conn.cursor()

# 3. 执行查询
cursor.execute("SELECT * FROM users")

# 4. 拿结果
rows = cursor.fetchall()
print("当前数据库里的数据：")
for row in rows:
    print(row)

# 关门
cursor.close()
conn.close()
