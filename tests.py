import pyAES
from pyCodeAanlysis import CodeAnalysis
pr = CodeAnalysis.Profile()


frame_header = bytes(open("frame_header.txt", "r").read(), 'utf-8')
plaintext = bytes(open("msg1.txt", "r").read(int(100)*16), 'utf-8')
key = bytes(open("key.txt", "r").read(), 'utf-8')
iv = bytes(open("iv.txt", "r").read(), 'utf-8')

pr.enable()
ciphertext, smic = pyAES.AES(key, iv).encrypt_gcmp(frame_header, plaintext)
pr.disable()

print(CodeAnalysis.get_exectime(pr)*1000)

pr.enable()
plaintext, rmic = pyAES.AES(key, iv).decrypt_gcmp(frame_header, ciphertext)
pr.disable()

print(CodeAnalysis.get_exectime(pr)*1000)