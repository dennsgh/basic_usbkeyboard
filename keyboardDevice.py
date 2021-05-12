# currently missing some other important keystrokes
# SHIFT is apparently a modifier instead of an actualy keystroke
# Function keys F1 to F12?
# Enter/Return?

class keyboardDevice:
    NULL_CHAR = chr(0)
    rel_seq = NULL_CHAR*8
    def write_report(self,report):
        with open('/dev/hidg0', 'rb+') as fd:
            fd.write(report.encode())
    def release(self):
        with open('/dev/hidg0', 'rb+') as fd:
            fd.write(self.rel_seq.encode())

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
        elif c=='\n':
            return(NULL_CHAR*2+chr(40)+NULL_CHAR*5)
        elif c=='&':
            return(chr(32)+NULL_CHAR+chr(36)+NULL_CHAR*5)
        
        #print(c)
        #continue
    def sendString(self,string):
        for c in string:
            self.write_report(self.char_to_reports(c))
            self.release()
    def sendCTRL():
        write_report(chr(1)+NULL_CHAR*7)
        self.release()