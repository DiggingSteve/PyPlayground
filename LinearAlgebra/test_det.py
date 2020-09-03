import numpy as np
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from LinearAlgebra.det import *

#定义矩阵
D=np.array([[2,1,-5,1],[1,-3,0,-6],[0,2,-1,2],[1,4,-7,6]])
#输出矩阵D行列式运算的值
d=np.linalg.det(D)
print ("D=",d)
c=det(D)
print("C=",c)
 
