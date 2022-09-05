import pyAES
from pyCodeAanlysis import CodeAnalysis
pr = CodeAnalysis.Profile()
ps = CodeAnalysis.Profile()

txt = b'Hello World'
print(str(txt))
print(len(txt))
pr.enable()
pad = pyAES.pad(txt)
pr.disable()
print(str(pad))
print(len(pad))
ps.enable()
txt_new = pyAES.unpad(pad)
ps.disable()
print(str(txt_new))
print(CodeAnalysis.get_exectime(pr)*1000)
print(CodeAnalysis.get_exectime(ps)*1000)