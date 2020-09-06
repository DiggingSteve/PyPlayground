# 行列式计算D=-1^t ∑a1p1 a2p2...anpn
import itertools
import numpy as np
import sys
import os
import copy
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def det(arr):
    '''
                arr->必须为方阵
        '''
    lenth = len(arr)
    nums = np.arange(lenth)
    temp_permutation = permute(nums)
    permutation= copy.deepcopy(temp_permutation)#计算完逆序数后被排序了 深拷贝
    permutation_arr = []
    for index in range(len(temp_permutation)):
        p = temp_permutation[index]
        permutation_arr.append(inverse_num(p))
    result = 0
    cc = ''

    for i in range(len(permutation)):
        temp = 1
        gg=''
        for j in range(len(permutation[i])):
            t = permutation[i][j]
            temp *= arr[j][t]
            
            gg += 'a'+str(j+1)+str(t+1)
        gg= ( '+' if pow(-1, permutation_arr[i])>0  else '-' )+gg
        cc += gg+',  '
        result += temp*pow(-1, permutation_arr[i])
        
    print(cc)
    return result


def inverse_num(lst):
    '''
    求逆序数 lst为数组
    '''
    count = 0

    def merge(left, right):
        i = j = 0
        temp = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                temp.append(left[i])
                i = i+1
            else:
                nonlocal count
                count += len(left)-i
                temp.append(right[j])
                j += 1

        if(i < len(left)):
            temp.extend(left[i:])
        else:
            temp.extend(right[j:])

        return temp

    lenth = len(lst)
    currentStep = 1  # 步长 初始时候每个数字当成一个序列 直接合并
    while currentStep < lenth:
        l_start = l_end = r_start = r_end = 0
        while l_start < lenth-currentStep:
            megred = []  # 暂存当前组排序
            l_end = l_start+currentStep
            r_start = l_end
            r_end = r_start+currentStep
            lst[l_start:r_end] = merge(lst[l_start:l_end], lst[r_start:r_end])
            
            l_start += currentStep*2
        currentStep *= 2
    return count
# 全排列


def permute(nums):
    result = []
    visited = [False] * len(nums)

    def backtrack(tmp):
        if len(tmp) == len(nums):
            result.append(tmp)
            return
        for i in range(len(nums)):
            if visited[i]:
                continue
            visited[i] = True
            backtrack(tmp + [nums[i]])
            visited[i] = False
        return result
    return backtrack([])  # 从空数组开始填充 直到

a=np.arange(100).reshape(10 , 10)
print(det(a))




# intertools.permutaions()

