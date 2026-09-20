import unicodedata

import pymysql

# 密码不写在代码里，从同目录的 db_config.py 读
# （Python 会把“脚本自己所在的目录”加进模块搜索路径，
#   所以 db_config.py 和本文件放在一起就能直接 import）
# db_config.py 已在 .gitignore 里，不会被提交到 GitHub
from db_config import DB_CHARSET, DB_HOST, DB_NAME, DB_PASSWORD, DB_USER

conn = pymysql.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME,
    charset=DB_CHARSET,
)

cursor = conn.cursor()

# ---------- 1. 插入 admin：先查再插，避免主键冲突 ----------
admin_sid = 'admin'

# 用 %s 当占位符，值放在后面的元组里传进去
# 这样不用自己拼字符串，也不用担心里面的引号把 SQL 搞乱
cursor.execute("SELECT sid FROM users WHERE sid = %s", (admin_sid,))

if cursor.fetchone():
    print(f"用户 {admin_sid} 已存在，跳过插入。")
else:
    cursor.execute(
        "INSERT INTO users (sid, passwd, sname, role) VALUES (%s, %s, %s, %s)",
        (admin_sid, '123456', '管理员', 'admin'),
    )
    conn.commit()   # 只有真的插入了才需要提交
    print("管理员数据插入成功！")

# ---------- 2. 查询并打印成表格 ----------
cursor.execute("SELECT sid, passwd, sname, role FROM users")
rows = cursor.fetchall()

headers = ('sid', 'passwd', 'sname', 'role')


def display_width(text):
    """算字符串在终端里占几格。中文是双宽字符，占 2 格。"""
    return sum(2 if unicodedata.east_asian_width(ch) in 'WF' else 1
               for ch in str(text))


def pad(text, width):
    """按终端显示宽度补空格，让表格对齐。"""
    return str(text) + ' ' * (width - display_width(text))


# 每一列的宽度 = 表头和该列所有数据里最宽的那个
widths = [display_width(h) for h in headers]
for row in rows:
    for i, value in enumerate(row):
        widths[i] = max(widths[i], display_width(value))

border = '+-' + '-+-'.join('-' * w for w in widths) + '-+'


def render(cells):
    return '| ' + ' | '.join(pad(c, w) for c, w in zip(cells, widths)) + ' |'


print("\n当前数据库里的数据：")
print(border)
print(render(headers))
print(border)
for row in rows:
    print(render(row))
print(border)
print(f"共 {len(rows)} 行")

# 关门
cursor.close()
conn.close()
