# 班级管理系统

一个用 Python 写的命令行班级管理系统。从最基础的内存列表开始，逐步演进到 MySQL 数据库存储。

## 目前进度

| 模块 | 状态 |
|---|---|
| 登录（用户名 / 密码 / 角色区分） | 🚧 框架完成，有已知问题 |
| 管理员菜单（增删改查） | ⬜ 菜单框架完成，功能待实现 |
| 学生菜单（查看 / 修改） | ⬜ 菜单框架完成，功能待实现 |
| 数据持久化（MySQL） | 🚧 连接试验完成，尚未接入主程序 |

## 项目结构

```
student-management-system/
├── StudentMS.py              # 主程序：登录 + 管理员/学生菜单
├── practice/                 # 试验代码（验证技术方案用，不是主程序的一部分）
│   ├── test_db.py            #   试验：连接 MySQL、建表、插入、查询
│   ├── db_config.example.py  #   数据库配置模板（可以提交）
│   ├── db_config.py          #   数据库配置（含真实密码，不会提交）
│   └── menu_demo.py          #   试验：菜单交互
└── docs/
    └── planning.md           # 开发规划：从内存列表到 MySQL
```

## 怎么运行

### 主程序

```bash
py -3.10 StudentMS.py
```

### 数据库试验（`practice/test_db.py`）

**第 1 步：准备数据库配置**

本项目**不包含数据库密码**，你需要自己建一个 `db_config.py`：

```bash
cd practice

# Windows
copy db_config.example.py db_config.py

# Mac / Linux
cp db_config.example.py db_config.py
```

然后打开 `db_config.py`，把 `DB_PASSWORD` 改成你自己的 MySQL 密码。

**第 2 步：装依赖**

```bash
py -3.10 -m pip install pymysql
```

**第 3 步：建库建表**（如果还没建过）

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

**第 4 步：运行**

```bash
cd practice
py -3.10 test_db.py
```

会打印出 users 表的内容。脚本是**幂等**的——重复运行不会报"主键重复"错误。

## 关于密码安全

`practice/db_config.py` 写在 `.gitignore` 里，**永远不会被提交到仓库**。

⚠️ 注意：`.gitignore` 只能阻止文件**将来**被提交。**如果密码曾经被提交过，删掉文件也没用**——git 历史里依然查得到，任何人都能 `git log` 翻出来。所以密码必须从一开始就不进仓库。

万一真的泄露了，正确处理方式是**立刻改掉 MySQL 密码**，而不是去重写 git 历史。

## 环境

- Python 3.10
- MySQL 8.0
- pymysql
