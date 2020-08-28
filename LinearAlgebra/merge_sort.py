#课外知识 归并排序 
import random,time
count=0
def merge(left,right):
    global count
    count+=1
    i=j=0
    temp=[]
    while i<len(left) and j< len(right):
        if left[i]<=right[j]:
            temp.append(left[i])
            i=i+1
        else:
            temp.append(right[j])
            j+=1
    
    if(i<len(left)):
        temp.extend(left[i:])
    else:
        temp.extend(right[:j])
    
    return temp




 #分到只有一个序列的 递归深度为log2^n
def merge_sort(list):
   
    if(len(list)==1):
        return list
    mid=len(list)>>1
    left=merge_sort(list[:mid])
    right=merge_sort(list[mid:])
    return merge(left,right)


if __name__=="__main__":
    start=time.clock()
    rand_list=[]
    for i in range(2<<5):
        rand_list.append(round(random.random()*100,2))
    
    lst=merge_sort(rand_list)
    end=time.clock()
    print(count,"次")

    print( lst)
    print ("done  ", (end-start))
