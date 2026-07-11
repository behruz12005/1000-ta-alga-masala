def my_append(lst, x):
    
    return lst + [x]
# print(my_append([1,2,3,4,5],6))


def my_index(lst, x):
    for i in range(len(lst)):
        if lst[i] == x:
            return i
    return -1

# print(my_index([1,2,3,4,5],3))


class Mylist:
    def __init__(self):
        self.emptyvalue = 4
        self.data = [None] * self.emptyvalue
        self.lenght = 0

    def append(self,x):
        if self.lenght == len(self.data):
            self.data = self.data + [None] * 4
        self.data[self.lenght] = x
        self.lenght += 1
   
    def natija(self):
        return self.data


onelist = Mylist()

onelist.append(1)
onelist.append(2)
onelist.append(3)
onelist.append(4)
onelist.append(5)
onelist.append(6)


# print(onelist.natija())



def my_remove(lst, x):
    for i in range(len(lst)):
        if lst[i] == x:
            for k in range(i,len(lst)- 1):
                lst[k] = lst[k+1]
            return lst[:-1]
    return lst

# print(my_remove([1,2,3,4],5))


def my_slice(lst, a, b):
    natija_list = []
    for i in range(a,b):
        natija_list.append(lst[i])
    return natija_list

    
print(my_slice([10, 20, 30, 40, 50],2,4))

