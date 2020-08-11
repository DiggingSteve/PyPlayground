import os
import sys,time
# change running path
print(sys.path)
os.chdir(sys.path[0])


def main():
   # 通过for-in循环逐行读取
    with open('test.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            
    print()


if __name__ == '__main__':
    main()
