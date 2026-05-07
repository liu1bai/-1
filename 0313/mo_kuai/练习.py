def jv_zheng(h):
    # import random
    # a=list()
    # while len(set(a))<h*h:
    #     a.append(random.randint(1,h*h))
    # b=set(a)
    # a=list(b)
    # for i in range(h):
    #     for j in range(h):
    #         print(a[i*h+j],end='\t')
    #     print()
#以上无法突破无序
#难方法
    a=[]
    import random
    for x in range(1,h+1):
        a.append([])                           #增加空行
        for y in range(h):                     #每行加元素
            c=0                                #重置后续循环变量
        #随机数生成必须在循环内，因为不符条件要重新输出
            while c==0:                        #循环执行
                num = random.randint(1, h*h)   #随机数生成
                w=len(a)
                cs = 0                         #查找次数
                for i in a:                    #遍历每行
                    if num not in i:           #判断条件
                        cs=cs+1                #次数控制
                    else:continue              #跳过后续
                if cs==len(a):                 #判断是增加
                    a[x-1].append(num)
                    c=+1
                if c==h: break
    for i in a:
        print(i)
    return a



def zhuan_zhi(a):
    b=[]
    for m in range(len(a)):
        b.append([])
    for x in range(3):
        for y in range(3):
            b[x].append(a[y][x])
    return b

# 对角线和
# sum=0
# for i in range(0,len(zhuan_zhi(a))):
#     sum+=zhuan_zhi(a)[i][i]
# print(sum)


# 2. 多列表交叉筛选（8分）
# 定义函数接收三个整数列表和阈值m、n；
# 筛选出第一个列表中大于m的元素，
# 筛选出第二个列表中小于n的元素，
# 筛选出第三个列表中能被3整除的元素；
# 将三个结果合并为一个列表，去重后升序返回；
# 调用函数测试。

def dyqc(a,b,c,m,n):
    e=set()
    for i in a:
        if i>m: e.add(i)
    for i in b:
        if i<n: e.add(i)
    for i in c:
        if i%3==0: e.add(i)
    x=list(e)
    return x

# 3. 字典统计与排序（8分）
# 给定学生分数字典 {"语文": [85,90,78], "数学": [92,88,95], "英语": [80,85,90]}；
# 统计每门课程的最高分、最低分、平均分；
# 将结果存储到新字典中，键为课程名，值为包含三个统计值的列表；
# 按平均分降序输出结果。
# a={"语文": [85,90,78], "数学": [92,88,95], "英语": [80,85,90]}
# print(list(a.items()))
# b=[]
# for i in list(a.items()):
#     c=0
#     for j in i[1]:
#         c+=j
#     c=c/len(i[1])
#     b.append([i[0],max(i[1]),min(i[1]),c])
# print(b)
# a={}
# for i in b:
#     a[i[0]]=[i[1],i[2],i[3]]
# print(a)
# print(sorted(a.items(),key=lambda x:x[1][2],reverse=True))

# 生成一个5x5的螺旋矩阵（从1开始顺时针填充）；
# 例如：
# 1  2  3  4  5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9
# 计算矩阵的主、次对角线之和；
# 输出矩阵和对角线之和。


def lxjz(p):
    szb=[i for i in range(1,p*p+1)]
    b=[]
    for i in range(p):
        b.append([])
    for x in range(p):
        for y in range(p):
            b[x].append([])    #创建空表
    c=1#方向参数（拐点）
    srz=0
    for i in range(len(b)**2):
        if c%4==1:                                #向右输出
            for j in range(len(b)-c//2):          #输出次数
                b[c//4][c//4+j].append(szb[srz])  #c//4  控制输出不变的行/列
                srz+=1
            c+=1
        elif c%4==2:        #向下输出
            for j in range(len(b)-c//2):
                b[c//4+1+j][len(b)-1-c//4].append(szb[srz])
                srz+=1
            c+=1
        elif c%4==3:        #向左输出
            for j in range(len(b)-c//2):
                b[len(b)-1-c//4][len(b)-2-c//4-j].append(szb[srz])  # c//4  控制输出不变的行/列
                srz += 1
            c += 1
        elif c%4==0:        #向上输出
            for j in range(len(b)-c//2):
                b[len(b)-1-c//4-j][0-1+c//4].append(szb[srz])
                srz += 1
            c += 1
    for i in b:
        for j in i:
            for k in j:
                print(k,end='\t')
        print()









