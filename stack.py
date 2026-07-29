class Stack:
    def __init__(self):
        self.__items = []


    def __len__(self):
        return len(self.__items)


    def is_empty(self):
        return not self


    def push(self, data):
        self.__items.append(data)


    def pop(self):
        if self.is_empty():
            raise IndexError("Стэк пуст")

        return self.__items.pop()


    def peek(self):
        if self.is_empty():
            raise IndexError("Стэк пуст")

        return self.__items[-1]


    def size(self):
        return len(self)


    def get_items(self):
        return self.__items



