import hashlib
import pyAES
import cProfile
from pyCodeAanlysis import CodeAnalysis

paes = cProfile.Profile()
pmd5 = cProfile.Profile()
pxor = cProfile.Profile()

def md5hash(any):
    return bytes(hashlib.md5(str(any).encode()).hexdigest()[16:], 'utf-8')

key = bytes("e47ac129b920f0ed", 'utf-8')
iv = bytes("e47ac129b920f0ed", 'utf-8')
msg = bytes("the quick browns", 'utf-8')

paes.enable()
hash1 = pyAES.AES(key, iv).encrypt_aes(msg)
paes.disable()
pmd5.enable()
hash2 = md5hash(msg)
pmd5.disable()
pxor.enable()
hash3 = pyAES.xor_bytes(key, msg)
pxor.disable()

class data:
    def __init__(self, hash1, hash2, hash3):
        self.hash1 = hash1
        self.hash2 = hash2
        self.hash3 = hash3
d = []
n = int(input("Enter number of iterations: "))
for i in range(n):
    d.append(data(CodeAnalysis.get_exectime(paes)*1000, CodeAnalysis.get_exectime(pmd5)*1000, CodeAnalysis.get_exectime(pxor)*1000))

h1_avg = 0
h2_avg = 0
h3_avg = 0

for i in range(n):
    h1_avg = h1_avg + d[i].hash1
    h2_avg = h2_avg + d[i].hash2
    h3_avg = h3_avg + d[i].hash3

print("Average AES time: " + str(h1_avg/n))
print("Average MD5 time: " + str(h2_avg/n))
print("Average XOR time: " + str(h3_avg/n))

