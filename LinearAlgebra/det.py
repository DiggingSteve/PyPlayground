# 逆序数常规求法 1 暴力 n^2 不推荐  2 在归并排序中 记录左右序列交换次数 即为逆序总合 行列式公式 -1^t ∑a1p1 a2p2...anpn
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
            global count
            count+=len(left)-i #右边有个小的 也就是说左边剩下的都是逆序
            j += 1
    if(i < len(left)):
        temp.extend(left[i:])
    else:
        temp.extend(right[j:])

    return temp

 # 分到只有一个序列的 递归深度为log2^n


def merge_sort(list):

    if(len(list) <= 1):
        return list
    mid = len(list) >> 1
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])
    return merge(left, right)


merge_sort([2,1])
print(count)
print(1+2+3+4+5+6+7+8)
