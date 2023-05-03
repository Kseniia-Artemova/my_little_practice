class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.head is None:
            self.head = obj
            self.tail = obj
        else:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
            self.tail = obj

    def remove_obj(self):
        prev = self.tail.get_prev()
        if prev is None:
            self.head = None
            self.tail = None
        else:
            self.tail = prev
            prev.set_next()

    def get_data(self):
        data_list = []
        if self.head:
            point = self.head

            while point.get_next():
                data_list.append(point.get_data())
                point = point.get_next()

        if self.tail:
            data_list.append(self.tail.get_data())
        return data_list


class ObjList:

    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.__data = data

    def set_next(self, obj=None):
        self.__next = obj

    def set_prev(self, obj=None):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data


obj_1 = ObjList("Data_1")
obj_2 = ObjList("Data_2")
obj_3 = ObjList("Data_3")
obj_4 = ObjList("Data_4")
my_list = LinkedList()
my_list.add_obj(obj_1)
my_list.add_obj(obj_2)
my_list.add_obj(obj_3)
my_list.add_obj(obj_4)
print(my_list.get_data())
while my_list.get_data():
    my_list.remove_obj()
    print(my_list.get_data())
