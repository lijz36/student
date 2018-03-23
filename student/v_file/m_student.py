

import time


# ----------学生信息录入----------
def info_input():
    _lst = []
    n = 1
    while True:
        name = input("学生" + str(n) + "姓名：")
        if not name:
            break
        age = int(input("学生" + str(n) + "年龄："))
        score = int(input("学生" + str(n) + "成绩："))
        d = {"name":name, "age":age, "score":score}
        _lst.append(d)
        n += 1
    return _lst


# ----------打印学生信息----------
def print_info(curList):
    # 打印边线
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
    for d in curList:
        fmt = "|" + d["name"].center(12) + "|" + str(d["age"]).center(12) \
              + "|" + str(d["score"]).center(12) + "|"
        print(fmt)
    print_frame()


# ----------按分数线学生信息----------
def find_score_line(lst, score_line):
    _lst = [x for x in lst if x["score"] >= score_line]
    if len(_lst):
        print_info(_lst)
    else:
        print("没有学生达到分数线！")


# -----按成绩排序-----
def sort_score_desc(lst, rev=False):
    def scoreKey(d):
        return d["score"]
    _lst = sorted(read_info(filename, mode, 1), key=scoreKey, reverse=rev)
    if rev:
        print("*****按成绩从高到低排序*****")
    else:
        print("*****按成绩从低到高排序*****")
    print_info(_lst)


# -----按年龄排序-----
def sort_age_desc(lst, rev=False):
    def myage(d):
        return d["age"]
    lage = sorted(read_info(filename, mode, 1), key=myage, reverse=rev)
    if rev:
        print("*****按年龄从高到低排序*****")
    else:
        print("*****按年龄从低到高排序*****")
    print_info(lage)


# ----------删除学生信息----------
def del_info(filename, mode):
    name = input("输入学生姓名：")
    if name != '':
        try:
            fr = open(filename, mode)
            b1 = bytes(name,'utf-8')
            for line in fr:
                if b1 in line:
                    fr.seek(-len(line),1)

                    fr.write(b'')
                    break
            else:
                print("没有找到这名学生！")
            fr.flush()
            fr.close()
        except Exception:
            print("文件操作异常")
    else:
        print("学生姓名不能为空")


# ----------修改学生信息----------
def chage_info():
    try:
        name = input("输入学生姓名：")
        fr = get_file_stream('r+b')
        fw = None
        flagL = fr.readlines()
        for x in range(len(flagL)):
            if name in flagL[x]:
                score = int(input("输入新成绩："))
                l = flagL[x].split(',')
                flagL[x] = l[0] + ',' + str(l[1]) + ',' + str(score) + '\n'
                fw = get_file_stream('w+b')
                fw.writelines(flagL)
                break
        else:
            print("没有找到这名学生！")
            return False
    except:
        print("文件操作异常")
        return False
    finally:
        fr.close()
        if fw != None:
            fw.close()
    return True


# --------读取信息返回列表---------
def read_info(filename, mode, type=0):
    try:
        f = open(filename, mode)
        _lst = f.readlines()
        if len(_lst) > 0:
            _lst1 = []
            for s in _lst:
                if s != '\n': 
                    l = s.split(',')
                    d = {'name':l[0], 'age':l[1], 'score':l[2][:-1]}
                    _lst1.append(d)
            if type == 0:
                print_info(_lst1)
            else:
                return _lst1
        else:
            print("学生信息为空")
        f.close()
    except:
        print("文件操作异常")


# ----------保存信息到文件----------
def save_info_file(lst, filename, mode='a+'):
    if len(lst) > 0:
        try:
            f = open(filename, mode)
            for x in lst:
                s = "%s,%d,%d\r\n" % (x["name"], x['age'], x['score'])
                f.write(bytes(s, 'utf-8'))
            f.flush()
            f.close()
        except IOError:
            print("文件操作异常")
            return False
    else:
        print("学生信息为空")
        return False
    return True
