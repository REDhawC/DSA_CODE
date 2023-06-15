class hashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashFunction(self, key):
        return key % self.size

    def reHash(self, oldHashValue):
        return (oldHashValue + 1) % self.size

    def put(self, key, value):
        hash = self.hashFunction(key)
        if self.slots[hash] == None:
            self.slots[hash] = key
            self.data[hash] = value
        elif self.slots[hash] == key:  # key already assigned
            self.data[hash] = value  # replace old value
        else:
            hash = self.reHash(hash)
            while self.slots[hash] != None and self.slots[hash] != key:
                hash = self.reHash(hash)
            if self.slots[hash] == None:
                self.slots[hash] = key
                self.data[hash] = value
            elif self.slots[hash] == key:
                self.data[hash] = value

    def get(self, key):
        startHash = self.hashFunction(key)
        curHash = startHash
        stop = False
        if self.slots[curHash] == None:
            # not assigned key
            return None
        else:
            # correct key
            if self.slots[curHash] == key:
                return self.data[curHash]
            else:
                # wrong hash ,keep searching
                curHash = self.reHash(curHash)
                while (
                    self.slots[curHash] != None
                    and self.slots[curHash] != key
                    and stop == False
                ):
                    curHash = self.reHash(curHash)
                    if curHash == startHash:
                        stop = True
                        return None
                    if self.slots[curHash] == key:
                        return self.data[curHash]

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


a1 = hashTable()
a1.put(2, 33)
a1.put(3, 44)
a1.put(4, 55)
a1.put(2, 66)
a1.put(11, 86)
a1.put(12, 66)
a1.put(13, 66)
a1.put(14, 66)
a1.put(15, 66)
a1.put(16, 669)

a1[2] = 88

print(a1[16])

print(a1.data)
print(a1.slots, len(a1.slots))
print(a1.get(11))
print(a1.get(2))
