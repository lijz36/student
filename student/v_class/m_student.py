

import time


docs = []


class Student:
    '''此类用来描述一个学生的信息'''
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def printInfo(self):
        fmt = "|" + self.name.center(12) + "|" + str(self.age).center(12) \
              + "|" + str(self.score).center(12) + "|"
        print(fmt)

    def __repr__(self):
        return "Student(%r,%d, %d)\r\n" % (self.name, self.age, self.score)


def info_input(lst=[]):
    '''录入学生信息'''
    n = 1
    while True:
        name = input("学生" + str(n) + "姓名：")
        if not name:
            break
        age = int(input("学生" + str(n) + "年龄："))
        score = int(input("学生" + str(n) + "成绩："))
        lst.append(Student(name, age, score))
        n += 1
    return lst


def output_info(lst):
    '''打印学生信息'''
    def print_frame():
        print("+" + (12 * "-" + "+") * 3)

    def print_title():
        title = "|" + "Name".center(12) + "|" + "Age".center(12) \
            + "|" + "Score".center(12) + "|"
        print_frame()
        print(title)
        print_frame()

    print("请稍后. . .")
    time.sleep(2)
    print_title()
    for o in lst:
        o.printInfo()
    print_frame()


# -----按成绩排序-----
def sort_score_desc(rev=False):
    global docs
    def scoreKey(o):
        return o.score
    l_score = sorted(docs, key=scoreKey, reverse=rev)
    if rev:
        print("*****按成绩从高到低排序*****")
    else:
        print("*****按成绩从低到高排序*****")
    show_student_info(l_score)


# -----按年龄排序-----
def sort_age_desc(rev=False):
    global docs
    def myage(o):
        return o.age
    l_age = sorted(docs, key=myage, reverse=rev)
    if rev:
        print("*****按年龄从高到低排序*****")
    else:
        print("*****按年龄从低到高排序*****")
    show_student_info(l_age)


# -----保存信息到文件-----
def save_info_txt():
    global docs
    if len(docs) > 0:
        try:
            f = open("./student.txt", 'a+')
            for o in docs:
                # s = "%s,%d,%d\r\n" % (o.name, o.age, o.score)
                f.write(repr(o))
            f.flush()
            f.close()
            docs.clear()
            print("文件保存成功")
        except IOError:
            print("文件操作异常")
    else:
        print("学生信息为空")


# -----保存信息到Excel-----
def save_info_excel():
    global docs
    if len(docs) > 0:
        try:
            f = open("./student.csv", 'a+b')
            for o in docs:
                # s = "%s,%d,%d\r\n" % (o.name, o.age, o.score)
                f.write(repr(o).encode("utf-8"))
            f.flush()
            f.close()
            docs.clear()
            print("文件保存成功")
        except IOError:
            print("文件操作异常")
    else:
        print("学生信息为空")


# ------从文件读取信息数据-------
def read_info_txt():
    global docs
    docs.clear()
    try:
        f = open("./student.txt", 'r+b')
        while True:
            s = f.readline()
            if not s:
                break
            docs.append(eval(s))
        print("文件信息提取完成")
        f.close()
    except:
        print("文件操作异常")


# ------从Excel读取信息数据-------
def read_info_excel():
    global docs
    docs.clear()
    try:
        f = open("./student.csv", 'r+b')
        while True:
            s = f.readline()
            if not s:
                break
            docs.append(eval(s.decode('utf-8')))
        print("文件信息提取完成")
        f.close()
    except:
        print("文件操作异常")


# -----删除学生信息-----
def del_student_info():
    name = input("输入学生姓名：")
    if name:
        try:
            f = open("./student.csv", 'r+b')
            for line in f:
                ln = len(name)
                s = line.decode("utf-8")
                if (s[8:10+ln] == "'"+name+"'"):
                    f.seek(-len(line),1)
                    b = b' ' * len(line) + b"\r\n"
                    f.write(b)
                    break
            else:
                print("没有找到这名学生！")
            f.flush()
            f.close()
        except Exception:
            print("文件操作异常")
    else:
        print("学生姓名不能为空")


# -----修改学生信息-----
def chage_student_score():
    name = input("输入学生姓名：")
    if name:
        try:
            f = open("./student.csv", 'r+b')
            for line in f:
                ln = len(name)
                s = line.decode("utf-8")
                if (s[8:10+ln] == "'"+ name + "'"):
                    score = checkInputScore()
                    l = s.split(',')
                    b1 = l[2].encode('utf-8')
                    pos = f.seek(-len(b1), 1)

                    b1 = bytes(str(score), 'utf-8') + b")\r\n"
                    print(b1)
                    f.write(b1)
                    break
            else:
                print("没有找到这名学生！")
            f.flush()
            f.close()
        except Exception:
            print("文件操作异常")
    else:
        print("学生姓名不能为空")


def checkInputScore():
    try:
        score = int(input("输入新成绩："))
        if score >= 0 and score <= 150:
            return score
    except Exception:
        print("输入成绩格式错误！")
        checkInputScore()


# -----添加学生信息-----
def add_student_info():
    global docs
    docs.extend(info_input())


# -----显示所有学生信息-----
def show_student_info(lst):
    output_info(lst)