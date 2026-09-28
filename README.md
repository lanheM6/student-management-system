# 班级管理系统

一个用 Python 写的命令行班级管理系统。从最基础的内存列表开始，逐步演进到 MySQL 数据库存储。

## 目前进度

| 模块 | 状态 |
|---|---|
| 登录（用户名 / 密码 / 角色区分） | ✅ 可用（比对内存列表） |
| 管理员菜单 — 添加学生（A） | ✅ 可用（批量录入、学号查重、自动初始密码） |
| 管理员菜单 — 删除（D）/ 查看（u）/ 修改（M） | ⬜ 菜单项在，功能待实现 |
| 学生菜单（查看 / 修改） | ⬜ 菜单框架完成，功能待实现 |
| 数据持久化（MySQL） | 🚧 连接试验通过，尚未接入主程序 |

> ⚠️ 现在所有用户数据都存在内存的 `users` 列表里，**程序一关就全没了**。接入数据库是下一步。

## 项目结构

```
student-management-system/
├── StudentMS.py              # 主程序：登录 + 管理员/学生菜单
├── practice/                 # 试验代码 + 主程序要用的数据库配置
│   ├── test_db.py            #   试验：连接 MySQL、查询 users 表
│   ├── db_config.example.py  #   数据库配置模板（可以提交）
│   ├── db_config.py          #   数据库配置（含真实密码，不会提交）
│   └── menu_demo.py          #   试验：菜单交互
└── docs/
    └── planning.md           # 开发规划：从内存列表到 MySQL
```

> 📌 `StudentMS.py` 第 9 行用 `sys.path.insert()` 把 `practice/` 加进了模块搜索路径，
> 所以主程序才能 `from db_config import ...` 读到配置。
> 这是个临时方案——等主程序真正接入数据库时，配置文件的归属可能要重新安排。

## 怎么运行

### 第 1 步：准备数据库配置（主程序和试验脚本都需要）

本项目**不包含数据库密码**，你需要自己建一个 `db_config.py`：

```bash
cd practice

# Windows
copy db_config.example.py db_config.py

# Mac / Linux
cp db_config.example.py db_config.py
```

然后打开 `db_config.py`，把 `DB_PASSWORD` 改成你自己的 MySQL 密码。

### 第 2 步：装依赖

```bash
py -3.10 -m pip install pymysql
```

### 第 3 步：建库建表（如果还没建过）

```sql
CREATE DATABASE student_ms DEFAULT CHARSET utf8mb4;

USE student_ms;

CREATE TABLE users (
    sid    VARCHAR(50) NOT NULL,
    passwd VARCHAR(50) NOT NULL,
    sname  VARCHAR(50) NOT NULL,
    role   VARCHAR(20) NOT NULL,
    PRIMARY KEY (sid)
);
```

### 运行主程序

```bash
py -3.10 StudentMS.py
```

登录用 `admin` / `123456`。

> 主程序目前**只用到了配置文件里的常量**，还没有真正连数据库，
> 所以跑主程序**不需要 MySQL 服务处于启动状态**，只要 `practice/db_config.py` 这个文件存在就行。

### 运行数据库试验

```bash
cd practice
py -3.10 test_db.py
```

会打印出 users 表的内容。

> ⚠️ 这一步**必须 MySQL 服务在运行**。如果报
> `OperationalError (2003, "Can't connect to MySQL server")`，
> 说明服务没启动，去 Windows 服务里启动 MySQL，或者用管理员权限运行
> `net start mysql80`（服务名以你实际安装的为准）。

## 已知问题 / 待办

- [ ] **数据不持久化** —— 内存列表，重启即丢，接入 MySQL 是主线任务
- [ ] `users` 表结构还没有 `age`、`sex` 两列，但主程序里的学生字典已经加了这两个字段，
      接数据库时要一起改表
- [ ] `StudentMS.py` 里 `import time`、`import pymysql` 目前还没用上（为后续接数据库预留）
- [ ] 管理员菜单第 54 行打印的是"**推出**（X）"，应为"退出"
- [ ] 管理员菜单的删除 / 查看 / 修改、学生菜单的全部功能

## 关于密码安全

`practice/db_config.py` 写在 `.gitignore` 里，**永远不会被提交到仓库**。

⚠️ 注意：`.gitignore` 只能阻止文件**将来**被提交。**如果密码曾经被提交过，删掉文件也没用**——git 历史里依然查得到，任何人都能 `git log` 翻出来。所以密码必须从一开始就不进仓库。

万一真的泄露了，正确处理方式是**立刻改掉 MySQL 密码**，而不是去重写 git 历史。

## 环境

- Python 3.10
- MySQL 8.0
- pymysql
