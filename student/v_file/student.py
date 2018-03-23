

import m_student as Stu
import sys


def show_select():
    def print_line():
        print("+" + "-" * 38 + "+")

    print_line()
    print("|  1)　添加学生信息" + " " * 20 + "|")
    print("|  2)　显示所有学生信息" + " " * 16 + "|")
    print("|  3)　删除学生信息" + " " * 20 + "|")
    print("|  4)　修改学生成绩" + " " * 20 + "|")
    print("|  5)　按学生成绩高-低显示学生信息" + " " * 5 + "|")
    print("|  6)　按学生成绩低-高显示学生信息" + " " * 5 + "|")
    print("|  7)　按学生年龄高-低显示学生信息" + " " * 5 + "|")
    print("|  8)　按学生年龄低-高显示学生信息" + " " * 5 + "|")
    print("|  9)　保存信息到文件" + " " * 18 + "|")
    print("| 10)　从文件中提取信息数据" + " " * 12 + "|")
    print("| 11)　保存信息到excel文件" + " " * 13 + "|")
    print("| 12)　从excel中提取信息数据" + " " * 11 + "|")
    print("|  q)　退出" + " " * 28 + "|")
    print_line()
    F_Select()


# ----------选择功能----------
def F_Select():
    s = input("请选择：")
    global L_stu
    if s == str(1):
        try:
            Lnew = Stu.info_input()
            L_stu += Lnew
        except Exception:
            print("输入格式错误！")
    elif s == str(2):
        Stu.read_info("./student.txt", 'r+')
    elif s == str(3):
        Stu.del_info("./student.txt", 'r+b')
    elif s == str(4):
        flag = Stu.chage_info()
        if flag:
            print("修改成功")
        else:
            print("修改失败")
    elif s == str(5):
        Stu.sort_score_desc("./student.txt", "r+", True)
    elif s == str(6):
        Stu.sort_score_desc("./student.txt", "r+")
    elif s == str(7):
        Stu.sort_age_desc("./student.txt", "r+", True)
    elif s == str(8):
        Stu.sort_age_desc("./student.txt", "r+")
    elif s == str(9):
        flag = Stu.save_info_file(L_stu, "./student.txt", 'a+b')
        if flag:
            L_stu.clear()
            print("保存成功")
        else:
            print("保存失败")
    elif s == str(10):
        Stu.read_info("./student.txt", "r+")
    elif s == str(11):
        flag = Stu.save_info_file(L_stu, "./student.csv", 'a+b')
        if flag:
            L_stu.clear()
            print("保存成功")
        else:
            print("保存失败")
    elif s == str(12):
        Stu.read_info("./student.csv", "r+")
    elif s == 'q':
        sys.exit()
    elif s == 't':
        show_select()
    F_Select()


# 文件操作入口

L_stu = []
show_select()
