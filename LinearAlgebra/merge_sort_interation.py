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
            left=lst[l_start:l_end]
            right=lst[r_start:r_end]
            while left and right: #非空
                if(left[0]<right[0]):
                    megred.append(left.pop(0))
                else:
                    megred.append(right.pop(0))
            megred.extend(left if left else right)
            lst[l_start:r_end]=megred
            l_start+=currentStep*2
        currentStep*=2
    return lst

    
    







