# 课外知识 归并排序
import random
import time
import sys,os
print(__file__)
print(os.path.abspath(__file__))  # 获取当前文件的绝对路径
print(os.path.dirname(os.path.abspath(__file__)))  # 去掉文件名，返回目录
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # 返回上2级目录
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from LinearAlgebra.merge_sort_interation import *

count = 0


def merge(left, right):
    i = j = 0
    temp = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            temp.append(left[i])
            i = i+1
        else:
            temp.append(right[j])
            j += 1

    if(i < len(left)):
        temp.extend(left[i:])
    else:
        temp.extend(right[j:])

    return temp

 # 分到只有一个序列的 递归深度为log2^n


def merge_sort(list):
    global count
    count += 1
    if(len(list) <= 1):
        return list
    mid = len(list) >> 1
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])
    return merge(left, right)


if __name__ == "__main__":
    rand_list = []
    for i in range(2 << 5):
        rand_list.append(round(random.random()*100, 2))
    rand_lis2 = []
    for i in range(2 << 21):
        rand_lis2.append(round(random.random()*100, 2))
    for i in range(1):
        start = time.clock()
        lst = merge_sort(rand_list)
        end = time.clock()
        s1=time.clock()
        lst2=merge_sort_interation(rand_lis2)
        s2=time.clock()
        print("递归法排序时间  ", (end-start))
       # print(lst)
        print("迭代法排序时间  ", (s2-s1))
        #print(lst2)
