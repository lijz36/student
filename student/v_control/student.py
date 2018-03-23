

import m_student as Stu
import sys


def show_operator():
    def print_line():
        print("+" + "-" * 38 + "+")
    def print_err():
        print("发生异常！！！")

    print_line()
    print("|  1)　添加学生信息" + " " * 20 + "|")
    print("|  2)　显示所有学生信息" + " " * 16 + "|")
    print("|  3)　删除学生信息" + " " * 20 + "|")
    print("|  4)　修改学生成绩" + " " * 20 + "|")
    print("|  5)　按学生成绩高-低显示学生信息" + " " * 5 + "|")
    print("|  6)　按学生成绩低-高显示学生信息" + " " * 5 + "|")
    print("|  7)　按学生年龄高-低显示学生信息" + " " * 5 + "|")
    print("|  8)　按学生年龄低-高显示学生信息" + " " * 5 + "|")
    print("|  q)　退出" + " " * 28 + "|")
    print_line()

    s = input("请选择：")
    global L_stu
    if s == str(1):
        try:
            Lnew = Stu.info_input()
            L_stu += Lnew
            Stu.print_info(L_stu)
        except Exception:
            print_err()
    elif s == str(2):
        Stu.print_info(L_stu)
    elif s == str(3):
        try:
            Stu.del_info(L_stu)
        except Exception:
            print_err()
    elif s == str(4):
        try:
            Stu.chage_info(L_stu)
        except Exception:
            print_err()
    elif s == str(5):
        Stu.sort_score_desc(L_stu, True)
    elif s == str(6):
        Stu.sort_score_desc(L_stu)
    elif s == str(7):
        Stu.sort_age_desc(L_stu, True)
    elif s == str(8):
        Stu.sort_age_desc(L_stu)
    elif s == 'q':
        sys.exit()
    show_operator()


L_stu = []

# -------------文件操作实例---------------
# show_operator()
try:
    f = open("./myfile.txt",'a+')
    L = f.readlines()
    for x in range(len(L)):
        L[x] = L[x][0:-1]
    L_stu += Stu.info_input2(L)

    print(L_stu)
    f.close()
    print("文件已经关闭")
except Exception:
    print("文件打开失败！")

