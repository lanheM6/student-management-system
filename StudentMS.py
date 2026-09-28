import os
import time
import pymysql
import sys



# 将 practice 目录加入系统路径，以便导入其中的 db_config
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'practice'))

#从你的 db_config.py 里读取数据库配置
from db_config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_CHARSET

#初始化用户列表
users = [
    {"sid":"admin","passwd":"123456","sname":"管理员","role":"admin"}
]

#函数定义

#登录菜单“显示函数”定义
def showLoginMenu():
    print("=" * 50)
    print("=              班级管理-登录 V1.0                =")
    print("*" * 50)
    print('*      登录（L） | 清屏（C） | 退出（X）      *')
    print('*' * 50)

#清屏函数定义
def cleanScreen():
    os.system("cls" if os.name == "nt" else "clear")

#登录函数定义
def login():
    sid = input("请输入用户名：")
    pwd = input("请输入密码：")

# 遍历 users，挨个比对
    for u in users:
        if u["sid"] == sid and u["passwd"] == pwd:
            print(f'登录成功！欢迎你，{u["sname"]} (角色：{u["role"]})')
            return u  # 返回这个用户字典，后面要用
        
    # 循环结束后还没找到，说明用户不存在或密码错误
    print('用户名或密码错误')
    return None


#管理员和学生菜单的“显示函数”定义
def showAdminMenu():
    print('=' * 50)
    print('=             班级管理-管理员 V1.0             =')
    print('*' * 50)
    print('* 添加（A） | 删除（D） | 查看（u） | 修改（M） | 清屏（C） | 推出（X） *')
    print('*' * 50)

def showStuMenu():
    print('=' * 50)
    print('=             班级管理-普通成员             =')
    print('*' * 50)
    print('*查看（u） | 修改（M） | 更多（N） | 清屏（C） | 退出（X） *')
    print('*' * 50)

#添加学生功能函数定义
def addStudent():
    try:
        n = int(input("请输入要添加的学生数量："))
    except ValueError:
        print("错误：请输入一个整数！")
        return

    for i in range(n):
        print(f"\n--- 正在录入第 {i+1} 个学生 ---")
        sid = input("请输入学号：")
        #检查学号是否已经存在
        exists = False
        for u in users:
            if u["sid"] == sid:
                exists = True
                break

        if exists:
            print(f"学号 {sid} 已存在，跳过这个学生！")
            continue
        sname = input("请输入姓名：")
        age = input("请输入年龄：")
        sex = input("请输入性别：")

        #自动分配初始密码
        new_student = {
            "sid": sid,
            "passwd":"123456",   #初始密码
            "sname":sname,
            "age":age,
            "sex":sex,
            "role":"stu"
        }
        users.append(new_student)
        print(f"学生 {sname} (学号 {sid}) 添加成功！初始密码：123456")

    print("\n所有学生添加完毕！")
    print("\n当前系统里所有用户：")
    for u in users:
        print(u)


#后台（管理员）主循环函数
def adminMain(user):
    while True:
        showAdminMenu()
        ch = input('请选择操作：')
        if ch =='X' or ch == 'x':
            print('已退出前台，返回登录界面。')
            break
        elif ch == 'C' or ch == 'c':
            cleanScreen()
        elif ch == "A" or ch == "a":
            addStudent()
        else:
            print('该功能待实现')

#前台（学生）主循环函数
def stuMain(user):
    while True:
        showStuMenu()
        ch = input('请选择操作：')
        if ch =='X' or ch == 'x':
            print('已退出前台，返回登录界面。')
            break
        elif ch == 'C' or ch == 'c':
            cleanScreen()
        else:
            print('该功能待实现')

#主循环
while True:
    showLoginMenu()
    ch = input("请选择操作：")

    if ch == "L" or ch == "l":
        user = login()
        if user is not None:
            # 登录成功，根据角色进入后台或前台
                if user['role'] == 'admin':
                    adminMain(user)
                elif user['role'] == 'stu':
                    stuMain(user)

    elif ch == "C" or ch == "c":
        cleanScreen()
    elif ch == "X" or ch == "x":
        print("退出系统！")
        break
    else:
        print("非法的操作！")


