# currently missing some other important keystrokes
# FORMAT is first two bytes are MODIFIER keys, 0x00XXXXXX means whatever you send had no modifier keys
# 0xXX580000 is ENTER for example, with 0xE2580000 it'd be ENTER with ALT

class keyboardDevice:
    NULL_CHAR = chr(0)
    rel_seq = NULL_CHAR*8
    def write_report(self,report):
        with open('/dev/hidg0', 'rb+') as fd:
            print(report.encode())
            fd.write(report.encode())
    def release(self):
        with open('/dev/hidg0', 'rb+') as fd:
            fd.write(self.rel_seq.encode())
    # a would be NULL_CHAR*2 + chr()
    def char_to_reports(self,char):
        NULL_CHAR = self.NULL_CHAR
        c=ord(char)
        if c>=97 and c<=122:#lower
            return(NULL_CHAR*2+chr(c-93)+NULL_CHAR*5)
        elif c>=65 and c<=90:#upper
            return(chr(32)+NULL_CHAR+chr(c-61)+NULL_CHAR*5)
        elif c>=49 and c<=57:#1-9
            return(NULL_CHAR*2+chr(c-19)+NULL_CHAR*5)
        elif c=='0':
            return(NULL_CHAR*2+chr(39)+NULL_CHAR*5)
        elif char=='\n': #or you can do c == 10
            return(NULL_CHAR*2+chr(40)+NULL_CHAR*5)
        elif c=='&':
            return(chr(32)+NULL_CHAR+chr(36)+NULL_CHAR*5)
        elif c==32: #whitespace, do print(ord(' ')) to check what whitespace c=ord(char) does
            return(NULL_CHAR*2+chr(44)+NULL_CHAR*5)
        
        #print(c)
        #continue
    def sendString(self,string):
        NULL_CHAR = self.NULL_CHAR
        for c in string:
            print("Sending "+c+"...")
            self.write_report(self.char_to_reports(c))
            self.release()
    def sendCTRL(self):
        NULL_CHAR = self.NULL_CHAR
        self.write_report(chr(1)+NULL_CHAR*7)

    def sendALT(self):
        NULL_CHAR = self.NULL_CHAR
        self.write_report(chr(4)+NULL_CHAR*7)
        self.release()
    def sendENTER(self):
        NULL_CHAR = self.NULL_CHAR
        self.write_report(NULL_CHAR*2+chr(40)+NULL_CHAR*5)
        self.release()
    # Function keys 3A to 45
    def sendFunction(self,x):
        if x>=1 and x<=12:
            NULL_CHAR = self.NULL_CHAR
            self.write_report(NULL_CHAR*2+chr(57+x)+NULL_CHAR*5)
            self.release()
        else:
            print("Invalid function key!")
    def sendSPACE(self):
        NULL_CHAR = self.NULL_CHAR
        self.write_report(NULL_CHAR*2+chr(44)+NULL_CHAR*5)
        self.release()
    def sendCAPS(self):
        NULL_CHAR = self.NULL_CHAR
        self.write_report(NULL_CHAR*2+chr(57)+NULL_CHAR*5)
        self.release()
    def sendESC(self):
        NULL_CHAR = self.NULL_CHAR
        self.write_report(NULL_CHAR*2+chr(41)+NULL_CHAR*5)
        self.release()
    def sendTAB(self):
        NULL_CHAR = self.NULL_CHAR
        self.write_report(NULL_CHAR*2+chr(43)+NULL_CHAR*5)
        self.release()
    def sendALTTAB(self):
        NULL_CHAR = self.NULL_CHAR   
        self.write_report(chr(14)+chr(2)+chr(43)+NULL_CHAR*5)
        self.release()
    def sendBACKSPACE(self,n):
        NULL_CHAR = self.NULL_CHAR
        for i in range(n):
            self.write_report(NULL_CHAR*2+chr(42)+NULL_CHAR*5)
            self.release()
    def sendDEL(self,n):
        NULL_CHAR = self.NULL_CHAR
        for i in range(n):
            self.write_report(NULL_CHAR*2+chr(76)+NULL_CHAR*5)
            self.release()
    def sendALTFunction(self,x):
        if x>=1 and x<=12:
            NULL_CHAR = self.NULL_CHAR
            self.write_report(chr(14)+chr(2)+chr(57+x)+NULL_CHAR*5)
            self.release()
        else:
            print("Invalid function key!")
