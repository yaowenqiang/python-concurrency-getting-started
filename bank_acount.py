import threading
# thread interference/race condition demo

class BankAccount:
    def __init__(self):
        self.bal = 0

    def deposit(self, amt):
        balance = self.bal
        self.bal = balance + amt

    def withdraw(self, amt):
        balance = self.bal
        self.bal = balance - amt



b = BankAccount()

t1 = threading.Thread(target=b.deposit, args=(100,))
t2 = threading.Thread(target=b.withdraw, args=(50,))
t1.start()
t2.start()
t1.join()
t2.join()

print(b.bal)