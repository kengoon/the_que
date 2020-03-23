class The_Que:
    elements = [7, 4, 8, 9, 0]
    elements2 = [7, 4, 8, 9, 0]
    elements3 = [7, 4, 8, 9, 0]

    # print(elements + [10])

    # the below code are prototype

    def insert_front(self, x):
        self.elements += [""]
        index = len(self.elements) - 1
        counter = 0
        while counter < index:
            tmp = self.elements[index - 1]
            self.elements[index] = tmp
            # print(self.elements[a-1])
            index -= 1

        self.elements[0] = x
        print(self.elements)
        # self.elements[a-2].copy(self.elements[a-1])

        pass

    def insert_rear(self, x):
        self.elements2 += [x]
        print(self.elements2)

        pass

    def insert(self, i, x):
        self.elements3 += [""]
        # tmp = self.elements3[i]
        # print(tmp)
        # self.elements3[i] = x
        index = len(self.elements3) - 1
        # print(index)
        # counter = 0
        try:
            while i < index:
                tmp = self.elements3[index - 1]
                self.elements3[index] = tmp
                index -= 1

            self.elements3[i] = x
            print(self.elements3)
        except IndexError:
            print(None)

    def get_all(self):
        self.insert_front(int(input("input element:>>> ")))
        print()
        self.insert_rear(int(input("input element2:>>> ")))
        print()
        print("**********position and element**************:")
        self.insert(int(input("position>> ")), int(input("element>> ")))
        pass


The_Que().get_all()

# Kenechukwu Do not Quit
