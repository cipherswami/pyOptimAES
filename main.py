import pyAES
from pyCodeAanlysis import CodeAnalysis

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
        self.penc = CodeAnalysis.Profile()
        self.pdec = CodeAnalysis.Profile()
        self.protocol = protocol
        self.frame_header = bytes(open("frame_header.txt", "r").read(), 'utf-8')
        self.plaintext = bytes(open("msg1.txt", "r").read(int(blocks)*16), 'utf-8')
        self.key = bytes(open("key.txt", "r").read(), 'utf-8')
        self.iv = bytes(open("iv.txt", "r").read(), 'utf-8')
        self.block_length = float.__ceil__(len(self.plaintext)/16)
        self.entropy_pt = CodeAnalysis.entropy(self.plaintext)
        # Console logging
        print("Block Length: ", self.block_length, file = self.f0)
        print("Protocol: " + self.protocol, file=self.f0)
        print(f"IV : {self.iv.decode()}", file=self.f0)
        print(f"key: {self.key.decode()}", file=self.f0)
        print(f"Plain Text : {self.plaintext.decode()}", file=self.f0)
        print("Entropy of PlainText: ", self.entropy_pt, file = self.f0)

    # Encryption
    def encrypt(self):
        def protocal_encrypt():
            if self.protocol == "ccmp":
                self.ciphertext, self.smic = pyAES.AES(self.key, self.iv).encrypt_ccmp(self.frame_header, self.plaintext)
            elif self.protocol == "gcmp":
                self.ciphertext, self.smic = pyAES.AES(self.key, self.iv).encrypt_gcmp(self.frame_header, self.plaintext)
        self.penc.enable()
        protocal_encrypt()
        self.penc.disable()
        self.entropy_ct = CodeAnalysis.entropy(self.ciphertext)
        self.entropy_mic = CodeAnalysis.entropy(self.smic)
        self.encryption_time = CodeAnalysis.get_exectime(self.penc)
        self.cpuE = CodeAnalysis.get_cpu(self.penc)
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
                self.plaintext, self.rmic = pyAES.AES(self.key, self.iv).decrypt_ccmp(self.frame_header, self.ciphertext)
            elif self.protocol == "gcmp":
                self.plaintext, self.rmic = pyAES.AES(self.key, self.iv).decrypt_gcmp(self.frame_header, self.ciphertext)      
        self.pdec.enable()
        protocal_decrypt()
        self.pdec.disable()
        self.decryption_time = CodeAnalysis.get_exectime(self.pdec)
        self.cpuD = CodeAnalysis.get_cpu(self.pdec)
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
        f1 = open("Results_ieee.csv", "w")
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