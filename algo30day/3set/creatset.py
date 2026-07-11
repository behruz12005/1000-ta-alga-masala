class MyHashset:
    def __init__(self):
        self.size = 8
        self.buckets = [[] for _ in range(self.size)]

    def _index(self, value):
        return hash(value) % self.size
    
    def add(self, value):
        idx = self._index(value)
        bucket = self.buckets[idx]
        print(idx)
        print(value)
        print(bucket)
        if value not in bucket:    
            bucket.append(value)   

    def contains(self, value):
        idx = self._index(value)
        bucket = self.buckets[idx]
        if value in bucket:    
            return True
        return False


s = MyHashset()
s.add("olma")
s.add("olma")
print(s.contains("olma"))
print(s.contains("anor"))
print(s.buckets)

print(hash(1) % 4)
print(hash(2) % 4)
print(hash(3) % 4)
print(hash(4) % 4)
print(hash(5) % 4)