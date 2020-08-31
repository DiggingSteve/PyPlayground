def merge_sort_interation(lst):
    lenth=len(lst)
    currentStep=1 #步长 初始时候每个数字当成一个序列 直接合并
    while currentStep<lenth:
        l_start=l_end=r_start=r_end=0
        while l_start<lenth-currentStep:
            megred=[]#暂存当前组排序
            l_end=l_start+currentStep
            r_start=l_end
            r_end=r_start+currentStep
            lst[l_start:r_end]=merge(lst[l_start:l_end],lst[r_start:r_end])
            l_start+=currentStep*2
        currentStep*=2
    return lst


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