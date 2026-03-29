class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.table = [[] for _ in range(self.size)]
        
    def hash(self,key):
        return key % self.size

    def add(self, key: int) -> None:
        index = self.hash(key)
        bucket = self.table[index]

        if key not in bucket:
            bucket.append(key)
        
    def remove(self, key: int) -> None:
        index = self.hash(key)
        bucket = self.table[index]

        if key in bucket:
            bucket.remove(key)        

    def contains(self, key: int) -> bool:
        index = self.hash(key)
        bucket = self.table[index]

        return key in bucket
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)