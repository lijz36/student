

import time


# ----------学生信息录入----------
def info_input():
    L_stu = []
    n = 1
    while True:
        name = input("学生" + str(n) + "姓名：")
        if not name:
            break
        age = int(input("学生" + str(n) + "年龄："))
        score = int(input("学生" + str(n) + "成绩："))
        d = {"name":name, "age":age, "score":score}
        L_stu.append(d)
        n += 1
    return L_stu

def info_input2(lst):
    L_stu = []
    for x in range(0,len(lst),3):
        print(x)
        name = lst[x]
        age = int(lst[x+1])
        score = int(lst[x+2])
        print(name,age,score)
        d = {"name":name, "age":age, "score":score}
        L_stu.append(d)
    return L_stu

# ----------打印学生信息----------
def print_info(curList):
    # 打印边线
    def print_frame():
        print("+" + (12 * "-" + "+") * 3)
    # 打印标题
    def print_title():
        title = "|" + "姓名".center(10) + "|" + "年龄".center(10) \
            + "|" + "成绩".center(10) + "|"
        print_frame()
        print(title)
        print_frame()

    print("请稍后. . .")
    time.sleep(3)
    print_title()
    for d in curList:
        fmt = "|" + d["name"].center(12) + "|" + str(d["age"]).center(12) \
              + "|" + str(d["score"]).center(12) + "|"
        print(fmt)
    print_frame()


# ----------按分数线学生信息----------
def find_score_line(L_stu, score_line):
    L_line = [x for x in L_stu if x["score"] >= score_line]
    if len(L_line):
        print_info(L_line)
    else:
        print("没有学生达到分数线！")


# ----------按成绩排序----------
def sort_score_desc(L_stu, rev=False):
    def scoreKey(d):
        return d["score"]
    L_score = sorted(L_stu, key=scoreKey, reverse=rev)
    print("*****按成绩从高到低排序*****")
    print_info(L_score)


# ----------按年龄排序----------
def sort_age_desc(lst, rev=False):
    def myage(d):
        return d["age"]
    lage = sorted(lst, key=myage, reverse=rev)
    if rev:
        print("*****按年龄从高到低排序*****")
    else:
        print("*****按年龄从低到高排序*****")
    print_info(lage)


# ----------删除学生信息----------
def del_info(lst):
    name = input("输入学生姓名：")
    for x in range(len(lst)):
        if lst[x]['name'] == name:
            del lst[x]
            print("删除成功！")
            break
    else:
        print("没有找到这名学生！")

# ----------修改学生信息----------
def chage_info(lst):
    name = input("输入学生姓名：")
    for x in range(len(lst)):
        if lst[x]['name'] == name:
            print("姓名:%s,成绩:%d" % (lst[x]['name'], lst[x]['score']))
            score = int(input("输入新成绩："))
            lst[x]['score'] = score
            print("修改成功！")
            break
    else:
        print("没有找到这名学生！")
