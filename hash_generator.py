import pyLinkSec

# Generate IVS
iv = bytes(open("iv.txt", "r").read(), 'utf-8')
key = bytes(open("key.txt", "r").read(), 'utf-8')
ivs = [pyLinkSec.AES(key, []).encrypt_aes(iv)]
for i in range(100):
    ivi = iv[0:12] + bytes(str(i).zfill(4), 'utf-8')
    ivs.append(pyLinkSec.AES(key, ivs).encrypt_aes(ivi))
ivs.append(pyLinkSec.md5hash(iv)) # -1

f = open("ivs.txt", "w")
print(ivs, file=f)
f.close()
print(open("ivs.txt", "r").read())
print("Lenght of ivs: ", len(ivs))

