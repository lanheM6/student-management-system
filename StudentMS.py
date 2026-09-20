import os
import time

#初始化用户列表
users = [
    {"sid":"admin","passwd":"123456","sname":"管理员","role":"admin"}
]

#函数定义

#登录菜单函数定义
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
            print(f"登录成功！欢迎你，{u["sname"]} (角色：{u['role']})")
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


#后台主循环函数
def adminMain(user):
    while True:
        showAdminMenu()
        ch = input('请选择操作：')
        if ch =='X' or ch == 'x':
            print('已退出前台，返回登录界面。')
            break
        elif ch == 'C' or ch == 'c':
            cleanScreen()
        else:
            print('该功能待实现')

#前台主循环函数
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
            user = login()
            if user is not None:
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


