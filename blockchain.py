import hashlib
import copy

def hashGenerator(data):
    result = hashlib.sha256(data.encode())
    return result.hexdigest()

class Block:
    def __init__(self, Block_No, data, hash, prev_hash):
        self.Block_No = Block_No
        self.data = data
        self.hash = hash
        self.prev_hash = prev_hash

class Blockchain:
    def __init__(self):
        hashStart = hashGenerator('gen_hash')

        genesis = Block(0, 'gen-data', hashStart, '0' * 70)
        self.chain = [genesis]
        self.backup_chain = copy.deepcopy(self.chain)

    def add_block(self, data):
        Block_No = len(self.chain)
        prev_hash = self.chain[-1].hash
        hash = hashGenerator(data + prev_hash)
        block = Block(Block_No, data, hash, prev_hash)
        self.chain.append(block)
        self.backup_chain.append(copy.deepcopy(block))

    def verify(self):
        for i in range(len(self.chain)):
            if self.chain[i].hash != self.backup_chain[i].hash:
                print("***********************************")
                print(f"!!! Data tempered at block {i} !!!")
                print("***********************************")
                return i
        
        for i in range(len(self.chain)):
            if self.chain[i].hash == self.backup_chain[i].hash:
                print("###############")
                print("---------------")
                print("Data is Secure")
                print("---------------")
                print("###############")
                return True


bc = Blockchain()

def function1():
    datab = input('Enter the data : ')
    bc.add_block(datab)

def function2():
    for block in bc.chain:
        print(block.__dict__)

def function3():
    n = int(input('Block No. : '))
    m = input('New data : ')
    bc.chain[n].data = m
    for i in range(n, len(bc.chain)):
        if i == 0:
            prev_hash = bc.chain[i].prev_hash
        else:
            prev_hash = bc.chain[i-1].hash
        data = bc.chain[i].data
        new_hash = hashGenerator(data + prev_hash)
        bc.chain[i].hash = new_hash
        bc.chain[i].prev_hash = prev_hash

def function4():
    bc.verify()

def default():
    print("Invalid input")

switcher = {
    1: function1,
    2: function2,
    3: function3,
    4: function4
}

while True:
    print("Menu")
    print("1. Add block")
    print("2. Print block")
    print("3. Change data")
    print("4. Verify blockchain")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 5:
        break
    func = switcher.get(choice, default)
    func()
