同学，先给你吃颗定心丸：**MySQL 不是新语言，它只是一个“仓库”**。你之前用 `users = [...]` 把数据放在内存里，程序一关就没了；用 JSON 文件保存，相当于记在笔记本上；MySQL 就是请了一个专业仓库管理员，帮你把数据存得又稳、又安全、还能快速查找。

你现在已经做到“添加学生”，接下来我帮你规划成：**每天一个小模块，前端、后端、数据库三层同时推进**。你不需要一天学完 MySQL，而是每天用一点，慢慢就懂了。

---

## 一、MySQL 到底是什么？先搞懂三件事

### 1. 数据库 = 仓库
- 内存 `users` 列表：临时放桌上，关程序就丢。
- JSON 文件：记在本子上，能持久，但查起来慢，多人同时写会乱。
- MySQL：专业仓库，有货架（表）、有编号（主键）、有索引（快速查找）、有权限（谁能看什么）。

### 2. 表 = Excel 工作表
比如学生表：

| sid | passwd | sname | age | sex | role |
|---|---|---|---|---|---|
| admin | 123456 | 管理员 | 30 | 男 | admin |
| 2023001 | 123456 | 张单 | 18 | 男 | stu |

- 一行 = 一个学生
- 一列 = 一个字段
- `sid` 是主键，唯一，不能重复

### 3. SQL = 操作仓库的语言
你以后会学这 5 句话：

```sql
CREATE TABLE users (...);   -- 建表
INSERT INTO users VALUES (...);  -- 插入
SELECT * FROM users;        -- 查询
UPDATE users SET age=19 WHERE sid='2023001';  -- 修改
DELETE FROM users WHERE sid='2023001';        -- 删除
```

Python 通过 `pymysql` 或 `sqlite3` 执行这些 SQL。

---

## 二、强烈建议：先用 SQLite 练手，再换 MySQL

你已安装 MySQL，但直接连 MySQL 对初学者容易卡在：
- 服务没启动
- 密码不对
- 数据库没创建
- 驱动没安装

所以建议：

> **第 1 周用 SQLite，Python 自带，零配置。学会 SQL 后，第 2 周把连接换成 MySQL，代码几乎不用大改。**

SQLite 也是数据库，只是存成一个文件 `student_ms.db`。  
以后换 MySQL 只需改连接字符串：

```python
# SQLite
engine = create_engine('sqlite:///data/student_ms.db')

# MySQL
engine = create_engine('mysql+pymysql://root:你的密码@localhost/student_ms?charset=utf8mb4')
```

---

## 三、你的项目要改成“三层架构”

以后每做一个功能，都同时碰这三层：

| 层 | 作用 | CLI 阶段 | GUI 阶段 | Web 阶段 |
|---|---|---|---|---|
| 前端 | 给用户看和点 | 命令行菜单 | Tkinter 窗口 | HTML/CSS/Bootstrap |
| 后端 | 业务逻辑 | service 函数 | service 函数 | Flask 路由 |
| 数据库 | 存数据 | SQLite/MySQL | 同左 | 同左 |

目录建议：

```text
StudentMS/
├── main_cli.py
├── main_gui.py
├── app.py
├── core/
│   ├── models.py
│   └── services.py
├── dao/
│   ├── db.py
│   ├── user_dao.py
│   └── announcement_dao.py
├── cli/
├── gui/
├── web/
│   ├── templates/
│   └── static/
├── data/
├── tests/
├── docs/
└── requirements.txt
```

---

## 四、从明天开始：30 天每日小模块规划

### 第 1 周：CLI 完整版 + SQLite
| 天 | 模块 | 前端 | 后端 | 数据库 | 学习点 |
|---|---|---|---|---|---|
| Day 1 | 建库建表 + 登录改数据库 | 登录菜单不变 | `login()` 查库 | 创建 student_ms 库、 `users` 表 | SQLite、CREATE、SELECT |
| Day 2 | 查看学生 | 菜单加 U | `search_students()` | SELECT 按学号/姓名/全部 | WHERE、LIKE |
| Day 3 | 修改学生 | 管理员 M | `update_student()` | UPDATE | 参数化查询 |
| Day 4 | 删除学生 | 管理员 D | `delete_student()` | DELETE | 主键删除 |
| Day 5 | 学生改密码 | 前台 M | `change_password()` | UPDATE | 权限判断 |
| Day 6 | 公告 CRUD | 公告菜单 | `add/list/delete_announcement()` | 建 `announcements` 表 | 外键、时间 |
| Day 7 | JSON 导入导出 + 测试 | 导入导出菜单 | `export_json()` | 批量读写 | 文件、异常、Git |

### 第 2 周：Tkinter GUI + MySQL
| 天 | 模块 | 前端 | 后端 | 数据库 |
|---|---|---|---|---|
| Day 8 | MySQL 迁移 | 不变 | 改连接 | 建 MySQL 库和表 |
| Day 9 | Tkinter 登录窗 | `Tk()`、Entry、Button | 复用 `login()` | 查 MySQL |
| Day 10 | 主窗口 + Treeview | 表格显示学生 | `list_students()` | SELECT |
| Day 11 | 添加/编辑/删除 | 弹窗表单 | 复用 service | INSERT/UPDATE/DELETE |
| Day 12 | 公告窗口 | 文本框、列表 | 公告 service | 公告表 |
| Day 13 | 样式 + 图标 | 字体、颜色、图片 | 不变 | 不变 |
| Day 14 | GUI 测试 + 打包 | `pyinstaller` | 测试 | 备份 |

### 第 3 周：Flask Web + 前端美化
| 天 | 模块 | 前端 | 后端 | 数据库 |
|---|---|---|---|---|
| Day 15 | Flask 项目结构 + 登录 | `login.html` | Flask 路由 | 查库 |
| Day 16 | 学生列表 + 搜索分页 | Bootstrap 表格 | `@app.route('/students')` | LIMIT/OFFSET |
| Day 17 | 增删改查 | 表单页 | 路由 + service | INSERT/UPDATE/DELETE |
| Day 18 | 公告管理 | 公告页 | 路由 | 公告表 |
| Day 19 | 权限 + 美化 | 导航栏、Flash | `@admin_required` | 角色判断 |
| Day 20 | ECharts 数据看板 | 图表 | 统计接口 | GROUP BY |
| Day 21 | 部署 + 测试 | Nginx/Gunicorn | 日志 | 备份 |

### 第 4 周：爬虫 + 数据分析 + AI 亮点
| 天 | 模块 | 技术 |
|---|---|---|
| Day 22 | 爬天气/新闻 | requests + BeautifulSoup |
| Day 23 | 成绩分析 | pandas + matplotlib |
| Day 24 | 公告自动分类 | 朴素贝叶斯 |
| Day 25 | 学生聚类 | K-Means |
| Day 26 | 成绩预测 | 感知机 |
| Day 27 | 整合进 Web | Flask + ECharts |
| Day 28 | 文档 + 答辩 | README、ER 图、PPT |

---

## 五、每天固定动作（很重要）

1. **20 分钟学知识点**：只学今天要用的。
2. **60 分钟写代码**：先写数据库，再写 service，最后接前端。
3. **15 分钟测试**：正常输入、错误输入、边界情况。
4. **10 分钟 Git**：
   ```bash
   git add .
   git commit -m "feat: 完成查看学生功能"
   ```
5. **5 分钟写日志**：今天做了什么、遇到什么问题、怎么解决。

---

## 六、明天 Day 1 具体做什么？

**目标：把登录从内存列表改成 SQLite 数据库查询。**

1. 安装 DB Browser for SQLite（可选，方便看表）。
2. 在 `dao/db.py` 写：
   ```python
   import sqlite3
   def get_conn():
       return sqlite3.connect('data/student_ms.db')
   ```
3. 建表：
   ```sql
   CREATE TABLE IF NOT EXISTS users (
       sid TEXT PRIMARY KEY,
       passwd TEXT NOT NULL,
       sname TEXT,
       age INTEGER,
       sex TEXT,
       role TEXT DEFAULT 'stu'
   );
   ```
4. 插入初始管理员：
   ```sql
   INSERT OR IGNORE INTO users VALUES ('admin','123456','管理员',30,'男','admin');
   ```
5. 写 `user_dao.py`：
   ```python
   def find_user(sid, passwd):
       conn = get_conn()
       cur = conn.cursor()
       cur.execute("SELECT * FROM users WHERE sid=? AND passwd=?", (sid, passwd))
       row = cur.fetchone()
       conn.close()
       return row
   ```
6. 把 `login()` 改成调用 `find_user()`。

做完后，你的登录就是真正从数据库查了。  
明天你做到哪一步，遇到报错，直接贴给我，我继续像老师一样带你。

**记住：不要一天学完所有东西。每天一个小模块，三层都碰一点，30 天后你就有 CLI + GUI + Web + 数据库 + 爬虫 + AI 的完整项目了。**