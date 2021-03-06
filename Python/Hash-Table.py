#hash table using linear probing
#for auto resizing: double in size whenever load factor approaches 1, decrease by half whenever load factor is 1/4
class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def __setitem__(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            #replaces the data if the keys are the same
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace
            #if not none, i.e. hash value exists, and the hashvalue is not equal to the key. i.e. a collision
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))
                self.slots[nextslot] = key
                self.data[nextslot] = data

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def __getitem__(self, key):
        startslot = self.hashfunction(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                data = self.data[position]
                found = True
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __len__(self):
        len = 11
        for element in self.data:
            if element == None:
                len -= 1
        return len

    def __contains__(self, val):
        for element in self.data:
            if element == val:
                return True
        return False

    def __str__(self):
        s = ''
        for x in range(len(self.slots)):
            if self.slots[x]:
                s += '{}: {}, '.format(self.slots[x], self.data[x])
        return s
H=HashTable()
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
#H[9]="asdf"
print(H)