# ============================================================
# 数据库配置模板
#
# 【怎么用】如果你把这个项目下载下来想跑起来，照做：
#
#   1. 把本文件复制一份，改名为 db_config.py（放在同一个目录里）
#      Windows 命令:  copy db_config.example.py db_config.py
#      Mac/Linux:     cp db_config.example.py db_config.py
#
#   2. 打开 db_config.py，把下面的 DB_PASSWORD 换成你自己的密码
#
#   3. db_config.py 不会被打包提交（它在 .gitignore 里），
#      所以你的密码不会泄露给任何人
#
# 【为什么密码不写在这里】
# 因为本文件是要公开给别人看的模板。
# 密码写在代码里提交上去，等于把钥匙和门牌号一起贴在门上。
#
# 【为什么必须和 test_db.py 放同一个目录】
# test_db.py 里写的是 `from db_config import ...`。
# Python 会自动把“脚本自己所在的目录”加进模块搜索路径，
# 所以两个文件放一起才 import 得到。
# ============================================================

DB_HOST = 'localhost'              # 数据库在哪？本机就是 localhost
DB_USER = 'root'                   # 用户名，装 MySQL 时默认就是 root
DB_PASSWORD = '在这里填你自己的密码'    # ← 改成你自己的
DB_NAME = 'student_ms'             # 要连的那个“文件夹”
DB_CHARSET = 'utf8mb4'             # 处理中文的编码
