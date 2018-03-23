

'''此模块主要存放与菜单相关的操作'''

import m_student as ms
import time
import sys


def show_menu():
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
    print("| 11)　保存信息到Excel文件" + " " * 13 + "|")
    print("| 12)　从Excel中提取信息数据" + " " * 11 + "|")
    print("|  q)　退出" + " " * 28 + "|")
    print_line()


# ----------选择功能----------
def run():
    while True:
        show_menu()
        s = input("请选择：")
        global L_Stu
        if s == str(1):
            ms.add_student_info()
        elif s == str(2):
            if len(ms.docs) > 0:
                ms.show_student_info(ms.docs)
            else:
                print("没有录入学生信息")
        elif s == str(3):
            ms.del_student_info()
        elif s == str(4):
            ms.chage_student_score()
        elif s == str(5):
            ms.sort_score_desc(True)
        elif s == str(6):
            ms.sort_score_desc()
        elif s == str(7):
           ms.sort_age_desc(True)
        elif s == str(8):
            ms.sort_age_desc()
        elif s == str(9):
            ms.save_info_txt()
        elif s == str(10):
            ms.read_info_txt()
        elif s == str(11):
            ms.save_info_excel()
        elif s == str(12):
            ms.read_info_excel()
        elif s == 'q':
            sys.exit()
        else:
            print("选择错误，请重新输入")
            time.sleep(2)


# 文件操作入口

L_Stu = []
if __name__ == "__main__":
    run()
