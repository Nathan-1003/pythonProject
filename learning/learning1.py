

class cla():
    def __init__(self):
        self.first='__init__用法:'
        self.second='self用法:'
        print('6月30，你學到了什麼？')

    def one(self):
        print(self.first, '為class中預設執行')
        print(self.second, '加上self後可供後續def中引用')

    def two(self):
        print(self.first,'第二項')

learning = cla()

learning.one()
learning.two()

