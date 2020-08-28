# 逆序数
def getInversion(numlist):
    count = 0
    for i in range(1,len(numlist)):
        subscript = numlist[i]
        for j in range(i):
            if subscript < numlist[j]:
                count += 1
    return count
D = 0
# 全排列，求每项的积
def permutation(dd,ilist,jlist,index):
    global D
    for i in range(index,len(jlist)):
        if index == len(jlist)-1:
            term = 1
            for ii in range(len(ilist)):
                i = ilist[ii]
                j = jlist[ii]
                term *= dd[i][j]
            if getInversion(jlist) % 2 == 0:
                D += term
            else:D -= term
            return
        tmp = jlist[index]
        jlist[index] = jlist[i]
        jlist[i] = tmp
        permutation(dd,ilist,jlist,index+1)
        tmp = jlist[index]
        jlist[index] = jlist[i]
        jlist[i] = tmp
 
if __name__ == '__main__':
    dd = [[1, 2, -4], [-2, 2, 1], [-3, 4, -2]]
    dd =[[1,1,1,1],[-1,2,1,3],[1,4,1,9],[-1,8,1,27]]
    jlist = []
    ilist = []
    for ii in range(len(dd)):
        ilist.append(ii)
        jlist.append(ii)
    permutation(dd,ilist,jlist,0)
    print(D)
