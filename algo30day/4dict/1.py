class MyHashMap:
    def __init__(self):
        self.data = []   # [("olma", 5), ("non", 3)] ko'rinishida

    def _find(self,key):
        for i in range(len(self.data)):
            if self.data[i][0] == key:
                return i
        return None
    def put(self,key, value):
        i = self._find(key)
        if i is not None:
            self.data[i] = (key, value)
            return 
        self.data.append((key,value))
        return 


    def get(self, key):
        i = self._find(key)
        if i is not None:
            return self.data[i][1]
        return None

    def __contains__(self,key):
        i = self._find(key)
        if i is not None:
            return True
        return False
        
dictmap = MyHashMap()

dictmap.put("olma",5)
dictmap.put("nok",2)
print(dictmap.put("olma",4))

print(dictmap.get("olma"))
print(dictmap.__contains__("dfdf"))




