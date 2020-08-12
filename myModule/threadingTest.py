from threading import Thread, Lock
from time import sleep


class Account(object):
    def __init__(self):
        super().__init__()
        self._balance = 0
        self._lock = Lock()

    @property
    def balance(self):
        return self._balance

    def deposit(self, money):
        # 算存款余额
        self._lock.acquire()
        # 获取锁
        try:
            new_balance = self._balance+money
            sleep(0.001)
            self._balance = new_balance
            if new_balance == 50:
                raise NameError("异常了")
        finally:
            print("异常了") #如果不释放锁将造成死锁等待
            self._lock.release()


class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    # 创建100个存款的线程向同一个账户中存钱
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    # 等所有存款的线程都执行完毕
    for t in threads:
        t.join()
    print('账户余额为: ￥%d元' % account.balance)


if __name__ == '__main__':
    main()
