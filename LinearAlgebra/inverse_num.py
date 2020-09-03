# 逆序数常规求法 1 暴力 n^2 不推荐  2 在归并排序中 记录左右序列交换次数 即为逆序总合 行列式公式 -1^t ∑a1p1 a2p2...anpn
def inverse_num(lst):
    '''
    求逆序数 lst为数组
    '''
    count=0
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


if __name__ == "__main__":

    a= inverse_num([9, 8, 7, 6, 5, 4, 3, 2, 1])
    print(a)
    print(1+2+3+4+5+6+7+8)
