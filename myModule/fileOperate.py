import os
import sys
# change running path
print(sys.path)
os.chdir(sys.path[0])


def main():
    f = open('test.txt', encoding='utf-8')
    print(f.read())
    f.close()


if __name__ == '__main__':
    main()
