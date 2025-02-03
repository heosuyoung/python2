class Counter:
    def __init__(self):
        self.count = 0

    def increment(self): #고민말고 self쓰셈
        self.count += 1
c = Counter()
# Counter.__init__
print(c.count) # 0
c.increment()
print(c.count) # 1

c2=Counter()
c.increment()
print(c2.count) # 0
print(c.count) # 2