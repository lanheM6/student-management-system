import time
import os

#定义函数

#打开文件功能函数
def openFile(file_path):
    try:
        with open(file_path,"r",encoding="utf-8") as f:
            cotent = f.read()
            print("-" * 50)
            print(cotent)
            print("-" * 50)
    except FileNotFoundError:
        print("错误：找不到这个文件！")
    except Exception as e:
        print(f"出错了：{e}")    

#清屏功能函数
def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")

#编辑功能函数
def editFile():
    print("正在进行编辑操作...")
    time.sleep(3)
    print("操作完成!")

#查看功能函数
def viewFile():
    print("正在进行查看操作...")
    time.sleep(3)
    print("操作完成！")

#打印菜单函数
def showMenu():
    print("================模拟菜单================")
    print("文件(O)|编辑(E)|查看(V)|清屏(L)|退出(X)")
    
while True:
    showMenu()
    ch = input("请选择操作：")   
    if ch == "X" or ch == "x":
        print("退出系统！")
        break
    elif ch == "O" or ch== "o":
        file_path = input("请输入文件路径：")
        openFile(file_path)
    elif ch == "L" or ch == "l":
        clearScreen()
    elif ch == "E" or ch == "e":
        editFile()
    elif ch == "V" or ch =="v":
        viewFile()
    else:
        print("你选择了：" + ch)   


 