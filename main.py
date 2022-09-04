import pyAES
import CodeAnalysis

# Pre Initiating Varaibles
Dev = 0 # Dev Mode Initiator
log_data = 0 # Log the detailed results (Might be huge file)

class LinkMode:
    
    if Dev == 0:
        # Non Dev Mode
        if log_data == 1:
            f0 = open('Results.log','w')
            f0.write("Results: \n\n")
            f0 = open('Results.log','a')
        else:
            f0 = open('/dev/null','w')
    else:
        # Dev mode
        f0 = open('output.log','w')

    def __init__(self, protocol, blocks):
        self.pr = CodeAnalysis.Profile()
        self.protocol = protocol
        self.frame_header = bytes(open("frame_header.txt", "r").read(), 'utf-8')
        self.plaintext = bytes(open("msg1.txt", "r").read(int(blocks)*16), 'utf-8')
        self.key = bytes(open("key.txt", "r").read(), 'utf-8')
        self.iv = bytes(open("iv.txt", "r").read(), 'utf-8')
        self.ivs = [b'\x82Q\xc0\x92\xa9\xc2\xfd\xeeP\xafhpu\x02\xe0\x00', b'\x90B\xb6Y\xa9Wb\xac{u\xfa\xc6\x9bv\x10_', b'Ec\x83\xc7\x91\xccX\xf3\x94\xab\x84Xz\xe2\xc5K', b'T$4\xe0\xe5\xb06\xa8\xcaEm!p\x17\x08\x9d', b'T`\x16\xd1\xc1\x1c\xbddo\x9c\x96ws\xe4l\xbb', b'V\x14{\x12\xc7cH\x88\xb5\x0b\x84\xe5\x00\xcaH\xf3', b'|\xb7e\x9a\xe9\x84r\x17?\x13\xd9j\xc0\xcfN\xf3', b'\x91\x8b\x9d2\x9f:\xc6\xa6\xac-\x86\x07\x18\xeeUT', b'\x01\x7f\x9a\xe5\xd0C\r%\x06\xa0\x84\xc1{\xea\xe1\x97', b'\xcbq<\x11<\x11"\xec\xa1[\xa54EG\x01M', b'CR\xa6\x96b#5\x892\x02\x9c\x9d\x1a\x00\xa1\xf3', b'\x8d\xf0\xc6\x10.G\x14\xc7\xbe\x15_!\xda\xee\x08\x8c', b'\xa0\xb1\x8f/)\xc1\xfc\x1f%\xe1Y\xe6\xdc&U\x0c', b'X\x7f`\x90m\xf2Q\x1c\x9am\xa7\x19\xe9\xadZ\xb6', b'&\x8d\xc4\xb5\x12\xfe\xf2\xb1\xf5S\x83\xbf\xc8\xa9\x92\x10', b'\x1aF\x02\xd0I\x1dC\xf6U\x94\x91R\x9a\xc4\xa7\x85', b'\x07\xf00K\x83Gh\xf9#Y\x1b\x11\xd1\x16v\x9a', b'?K\xac\xa3\x07\x90\r\n/\x7f\xd8V(\xe0z%', b"\xa2\xec\x15U\x03\xe2\xa83'\x82z\x8a\xac\x00\xeaU", b'\n\x0e\xa1\xf3i\xb917T\xcajC\x9bK\xcbr', b'\xeb\xe6I\xdcp\xad8\xd3\x85\x14\xc16\x8a\xe0y\x0f', b'D{\x9e@\x02\x0f\xc1\x00\xa3^\x12\x1d\x995eC', b'O\xbc1\x06z;\xbdJ\xe7\xc2\xff\x91\x06L\nv', b'\x1f\x02;\xd4\x1b\x15W\x91\x9b,\xa2"\x85t\x17\xf3', b'\xe8\x00\x8b.\xd9\xd9o\xb8 \x80x\xb68\x96\x92\xc9', b'\x01\xfb\x1c\xa3C\xf7\xae\xe9\x88\xa5\\-\xf6\xe6o\xcc', b'\xa9\xfe\t\x1d\x95=\xe8\xa8\xf3\xaa\xa0|\x10\xd2\xa9c', b'\xe3\x8bF\x87F\xdb\xa5];\xa2v\xd3\xcbH\xe3,', b"\xab\xc3\x15\x1bS\xbe\xc4?'\xfd\x87\xe5\xc1<\xf4\xf0", b'\x8ev`\xf2\x92\xab9\xc7vlqT\xe8x\x18B', b'W\x7fW\x9a\xd0}\xb0\xf6$\x99\xb9\n6\xec\x17u', b'\x1f\xa9\xb9YN\xaa\x19\t\xa9\xdc\xed\xd8\xa1\x93\xa5$', b'\xac\x81\xed\xf8\xfdj\x7fJ\x93"\x81~mV2\xca', b'\nu\x1eM\xea\xfa|\xd2c\x84\xfa@\x9fo\x0b\xa6', b'\xff\x9e\xdbb\x11\xbc7\xd3\xa4X\xe6i\x82\xe1uR', b"\xb7\x8b\xcf\xbef\xbf\x89'\xe0\x04}\x00\xb9@Q\xc1", b'\x96O@Z\x08H\t\xd8\x83E\xea\x8e\xed4*\xc6', b'\x03h\xf1\x94Y\xc3;E\xca\x05\xbfi\x89\x93(\xdd', b'\xe0\x18X \xd5\x04c\x13\x81\xaa0\xb4\x9d*\x02\xe1', b'\x86\x9a\xdd\xfb=\x0c\xd2\x08\xa5\x13\x01qD\xe4\x9f9', b'hk\xe2G8E\x97HQ\xac>\x1b\xb9\xee\xde\xcc', b'\xb9Z\x91A\xf7\xc7/\x19\x161\xadB\x87\xa2s\x97', b'\xdcMg+\xc9g\x0c\xc6\xb9m\xc22k\xac\xbd9', b'\x18\xcb\xa1\xf5_y\xa5\x86\xd5x\xcbV\xb9\x84\x07\xbc', b'x\xbaf\x83j\x89\xbbR\xfa\\x\x8c\xfeW\xbe\xbb', b'\xf2\x90y\xb9\xdag\x04%\xc2\xd4\x08\x07\xaft\n\xc7', b'\xa8\xe7+\xe84o\x9b\xcc\x7f#M\xe9\x9a\xf8\xa8\xb7', b'd6\xe9\x93\xb2\xadl\xee\xf1\xf7\x1a\\`m\xca\xd2', b'\xa6\x17\x1b\xbc\xec$\x1d\xd6\xba\x90%\x0f\xe1\x8dMi', b'Q\xa8 \x9c\xc2\xbc\xe8\n9\x04\xce\x99\xbc\xd4X\x19', b'\\\x888\xe61bP\x0b\x95&\xee\x04\x1e*\xf1\x12', b'c\xbf\x12\x16o\xd6\x05O\xd5\xbb\x9b\xe4\n=\xf6\x92', b'\x91\x01\xf9B\x92\xfd\x19\xbe\xd5\xab4\x93\xdf.\x969', b'\x90\x05W\xa5\x835\xc9Hd\xf4jc\r\xe2\xb3\\', b"\x82\x07\xfd\xd4\x8b'\x11\x83\r\xfbX\xdd(Wf\xbc", b'\xb6\xd4\xdc\xa0"\xef\x99\xf7\x89\xec\x18\xaf\xa0\xf2A\xfa', b'D\xb7D\x86\x92l\xfbd\x836kT\n\xa4\xf5\x16', b'\xaej\xa1u8\xb2|\xd5G\xff\xc5\x93\\\x8a\xd3\xbd', b'%Z?,H[D\xf3\xb0\x1c]9\xf6XP)', b'\xe4\x8bZ:\xf9D2\xeb\xa7\xffs,L\xf9nY', b'@\x944\xb0\xa1\xea\\\xfe\x10\xb7\xe8v!\x1a\x9f\xaa', b'G\x96\xa7\x00\xf9\x16\xef\x87:\xfb\x9f\xec_)L\xa3', b'.\x1f~o\xe3\xa7\x1f\xaf\x14_\x03\xf0\xa0\x18p\xd6', b'\xa9K\xbb\xd4_\xf2\xa4b\x8f\x93\xaf\x0f\xe3fU\xbd', b'\xbf\x9f\xc1p\xba\x80c8\t8(h\xd0\xd3\x95J', b'\xa3-b\x93\x0f\x9c\xaaN\x1e\x01gG\xf1\xf6\x83\x8b', b'\x82&\xcd\xef\x14\x1f\x8c\xd8|\x81 bqq\x94\x07', b'\xc2\xe9,Q=\xe5\xc2\x8b\x80\xdf\xa6\xbb\x88\xc9\xbf\xac', b'p\x8f\xd04\xc09\x18\xd5\x952#.\x9b\xec\xbe\xc2', b'\x8b\xfc\xf6E\xfa\xb7n\xc7H\x00!\xdf\xb9\xeaqY', b'\x0e0\xbeu~\x0e\xa0{\xf8\x0c\xc4\xdf\xd0\x88\xbc5', b'D}\xa3\xff\x0f\xcc\xed\x8f\xcf\xb5L\xfe\x97xK\xb8', b'm\xff. \x9b\xbe@\xc3\xba\x1c\xa0X\x8c\x802j', b'\xaa\xe6\xd1o\xe3#\xae\x13\xae\x92\x92\xf2\xb9\xd5\xb4\xa1', b'R\xf6/N\xbd\xdc\x9an\xfd`\xc1S\xa3\xb1\x9fV', b'\xaa\x84^\x1e\x8a\xc3\x15\xe4gcE\xd6\xa1q\x1bd', b'%\xbf@k\xb0\x9e1\xbb\xec\x14fWl\xb8\x86<', b'\x99b/,y\xa4\xb0\xb9I,TP:3]\x9a', b'@\xc9\x83#\x08\x83F\x14\xeb\xb3sE\xd0\xfe-\xfa', b'S\x18\x9a7\x99c\xd2\x11\x0b\xe6b\xd5\x945\x00\xff', b'\xee\xe23\x1b\xc3r}\xa3S{\xb5\xc5.\xb1\xdaB', b'\xc0\xa60\x98\xaeK\x12_\xc7z\xb0\xd9\xb8\xb3\xbc\xbf', b'\x95~\x98\xb6\x19hc\x86\xcbz`\xcf\xb0\xaa\x82g', b'\x87O\x93G\xee\xd2&\xcc\xc3\xff\x80\xaa]\x8b\x0b\xfc', b"M\x9c\xe3\xd1\x1c\xf9\x82\xc6^t\x00\xb5\x17'\xe20", b'\x08J\xb0\x8bcT\xef\x96k\xfb\xa7\xb8,\x9f\xeb\xd0', b'\xa5\xda\xe8\x17\x9c\x02\x8f\xe2sK\xd2\x19\xad\x81\xe0/', b'\xe8\x0c=\x92X\x9e\xd9\x0e\x7f)\x8a{\x15.J\xca', b'\x1b\xf7\x7f\x9e\xc2\xb3\xf2\xe8\xfafF\x01}k@\x06', b'\xee\xb0\x17\x00O>\xc8\x97\xdd\xa2l\xf5w\xba\x84\x18', b'\x13\xfa\xca\xfe\x90r:\xb8\xccc\xad\x8d\x9b@>\xf3', b'\x01\x84[bA:\xd4\xaa\xb5k8Z\x99"v\xb8', b'e\xa7t\xf6r\x91\tI|OD\xe2?\xc9\xf5\xf1', b'#|\xb94\xe5\x1b \xdc#\xbdC\xed\x9b\xa1Oi', b'\x19\xc7\xf6\xc2\x15M\xbc:D\xe2\x01\xccJ(\x0f\x9f', b'2\xb1\xa6X&_\xd4\xae\xf2\nE\xbb\x87=\x1d\xeb', b'\x10\x1cz\xf2LZ\xe9IMb\xd3\xc7\x8e\xc0\x9b\x12', b'\x90%\xb2F\x0b\x81"\x0b\xc2\\\x9f\xd9\xd9\x80\xf3\xf4', b'\xd0\x11Y\xdf*\xc3j\xfd\xf1\xdc\xc2\xa6\x02\xee\xff\xe2', b'\x8c\x88\xbe\xb3,\xf2\x91\xa8[\xc0\x93.\xf6\x17B\xe5', b'\xc4\x14 \xc07\x9b\xb5\xc7b\t\xdc#\x05\xa0\xadM', b'\xb2t\xac\xf0\xc9\xd0\xfe4G\xdf\x90$\x98\x98\xb9]']
        self.block_length = float.__ceil__(len(self.plaintext)/16)
        self.entropy_pt = CodeAnalysis.entropy(self.plaintext)
        # Console logging
        print("Block Length: ", self.block_length, file = self.f0)
        print("Protocol: " + self.protocol, file=self.f0)
        # print(f"IV : {self.iv.decode()}", file=self.f0)
        print(f"key: {self.key.decode()}", file=self.f0)
        print(f"Plain Text : {self.plaintext.decode()}", file=self.f0)
        print("Entropy of PlainText: ", self.entropy_pt, file = self.f0)

    # Encryption
    def encrypt(self):
        def protocal_encrypt():
            if self.protocol == "ccmp":
                self.ciphertext, self.smic = pyAES.AES(self.key, self.ivs).encrypt_ccmp(self.frame_header, self.plaintext)
            elif self.protocol == "gcmp":
                self.ciphertext, self.smic = pyAES.AES(self.key, self.ivs).encrypt_gcmp(self.frame_header, self.plaintext)
        self.pr.enable()
        protocal_encrypt()
        self.pr.disable()
        self.entropy_ct = CodeAnalysis.entropy(self.ciphertext)
        self.entropy_mic = CodeAnalysis.entropy(self.smic)
        self.encryption_time = CodeAnalysis.get_exectime(self.pr)
        self.cpuE = CodeAnalysis.get_cpu(self.pr)
        self.ramE = CodeAnalysis.get_ram(protocal_encrypt)
        # Console logging
        print(f"Cipher text: {str(self.ciphertext)}", file=self.f0)
        print(f"SOURCE MIC: {str(self.smic)}", file=self.f0)
        print("Entropy of CipherText: ", self.entropy_ct, file=self.f0)
        print("Entropy of MIC  : ", self.entropy_mic, file=self.f0)
        print("Encryption Time   : ", str(self.encryption_time) + " ms", file=self.f0)
        print("Encryption RAM Usage: ", str(self.ramE) + " MiB", file=self.f0)
        print("Encryption CPU sys: ", str(self.cpuE) + "", file=self.f0)

    # Decryption
    def decrypt(self):
        def protocal_decrypt():
            if self.protocol == "ccmp":
                self.plaintext, self.rmic = pyAES.AES(self.key, self.ivs).decrypt_ccmp(self.frame_header, self.ciphertext)
            elif self.protocol == "gcmp":
                self.plaintext, self.rmic = pyAES.AES(self.key, self.ivs).decrypt_gcmp(self.frame_header, self.ciphertext)      
        self.pr.enable()
        protocal_decrypt()
        self.pr.disable()
        self.decryption_time = CodeAnalysis.get_exectime(self.pr)
        self.cpuD = CodeAnalysis.get_cpu(self.pr)
        self.ramD = CodeAnalysis.get_ram(protocal_decrypt)
        # Console logging
        if self.rmic == self.smic:
            print(f"Decrypted Message: {self.plaintext.decode()}", file=self.f0)
            print(f"DESTINATION MIC: {str(self.rmic)}", file=self.f0)
            print("Decryption Time: ", str(self.decryption_time) + " ms", file=self.f0)
            print("Decryption RAM Usage: ", str(self.ramD) + " MiB", file=self.f0)
            print("Decryption CPU sys: ", str(self.cpuD) + "", file=self.f0)
        else:
            print("Integrity Check Faild !")
            exit()
        print("", file=self.f0)

def dev_protocol(protocol):
    if protocol == 1:
        print(" ")
        print("[#] CCMP Mode selected !")
        print(" ")
        protocol = "ccmp"
        ccmp = LinkMode(protocol, int(input("Enter Block Length: ")))
        ccmp.encrypt()
        ccmp.decrypt()
        del ccmp
        print(" ")
        print("[#] COMPILATION SUCCESSFUL: Check output.log for the Results.")

    elif protocol == 2:
        print(" ")
        print("[#] GCMP Mode selected !")
        print(" ")
        protocol = "gcmp"
        gcmp = LinkMode(protocol, int(input("Enter Block Length: ")))
        gcmp.encrypt()
        gcmp.decrypt()
        del gcmp
        print(" ")
        print("[#] COMPILATION SUCCESSFUL: Check output.log for the Results.")
    else:
        print("[!] Invalid option !")

def main():
    if Dev == 1:
        print(" ")
        print("[#] In Dev Mode ...")
        print(" ")
        print("1> CCMP")
        print("2> GCMP")
        print(" ")
        dev_protocol(int(input("Choose Mode: ")))
    else:
        f1 = open("Results_Optimized.csv", "w")
        f1.write("Block Length,Entropy Plain Text,Entropy Cipher Text,CCMP Entropy MIC,CCMP Encryption Time,CCMP Encryption RAM,CCMP Encryption CPU,CCMP Decryption Time,CCMP Decryption RAM,CCMP Decryption CPU,GCMP Entropy MIC,GCMP Encryption Time,GCMP Encryption RAM,GCMP Encryption CPU,GCMP Decryption Time,GCMP Decryption RAM,GCMP Decryption CPU\n")
        print("")
        for i in range(0, int(input("Enter No. of Blocks: "))):
            print("")
            print("[#] Running block: ", i+1)
            protocol = "ccmp"
            ccmp = LinkMode(protocol, i+1)
            ccmp.encrypt()
            ccmp.decrypt()
            f1.write(f"{ccmp.block_length},{ccmp.entropy_pt},{ccmp.entropy_ct},{ccmp.entropy_mic},{ccmp.encryption_time},{ccmp.ramE},{ccmp.cpuE},{ccmp.decryption_time},{ccmp.ramD},{ccmp.cpuD},")
            del ccmp
            protocol = "gcmp"
            gcmp = LinkMode(protocol, i+1)
            gcmp.encrypt()
            gcmp.decrypt()
            f1.write(f"{gcmp.entropy_mic},{gcmp.encryption_time},{gcmp.ramE},{gcmp.cpuE},{gcmp.decryption_time},{gcmp.ramD},{gcmp.cpuD}\n")
            del gcmp
        print("")
        print("[#] COMPILATION SUCCESSFUL: Check Results.csv and Results.log files for the output.")
        print("")

if __name__ == "__main__":
    main()