class The_Que:
    list = None

    # print(list + [10])

    # the below code are prototype

    def insert_front(self, x):
        self.list += [""]
        index = len(self.list) - 1
        counter = 0
        while counter < index:
            tmp = self.list[index - 1]
            self.list[index] = tmp
            # print(self.list[a-1])
            index -= 1

        self.list[0] = x
        # print(self.list)
        # self.list[a-2].copy(self.list[a-1])

        pass

    def insert_rear(self, x):
        self.list += [x]
        # print(self.list)

        pass

    def insert(self, i, x):
        self.list += [""]
        index = len(self.list) - 1
        try:
            while i < index:
                tmp = self.list[index - 1]
                self.list[index] = tmp
                index -= 1

            self.list[i] = x
            # print(self.list)
        except IndexError:
            print(None)


# Kenechukwu Do not Quit

"""
Example code:
replace object with any variable of choice

from de_que import The_Que

object = The_Que()
object.list = [20, 'a', 3.0, "..."]
object.insert_front(3)

print(object.list)
"""
