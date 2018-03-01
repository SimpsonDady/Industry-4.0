import random


class CreateChild:
    def __init__(self, filter):
        self.filter = filter
        self.kid = {}
        self.allkid = []
        self.child()

    def child(self):
        for i in range(800):
            list = []
            m = random.uniform(1, 40)
            s = random.uniform(0, 10)
            m2 = random.uniform(1, 40)
            s2 = random.uniform(0, 10)
            if s == 0.0:
                s = 0.0000000000000001
            if s2 == 0.0:
                s2 = 0.0000000000000001
            list.append(m)
            list.append(s)
            if self.filter:
                list.append(m2)
                list.append(s2)
            self.kid.update({"child" + str(i + 1): list})
        self.allkid.append(self.kid)
        # print(self.allkid)
        print(".............隨機產生子代................")
