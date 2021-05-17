# currently missing some other important keystrokes
# FORMAT is first two bytes are MODIFIER keys, 0x00XXXXXX means whatever you send had no modifier keys
# 0xXX580000 is ENTER for example, with 0xE2580000 it'd be ENTER with ALT
NULL_CHAR = chr(0)
modiDict = {"ctrl": chr(1)+NULL_CHAR, 
            "alt": chr(4)+NULL_CHAR,
            "shift": chr(2)+NULL_CHAR, 
            "ctrl alt": chr(5)+NULL_CHAR, 
            "alt ctrl": chr(5)+NULL_CHAR,
            "shift ctrl": chr(3)+NULL_CHAR,
            "ctrl shift": chr(3)+NULL_CHAR, 
            "alt shift": chr(6)+NULL_CHAR,
            "shift alt": chr(6)+NULL_CHAR,
            "ctrl shift esc": chr(7)+NULL_CHAR,
            "ctrl alt shift": chr(7)+NULL_CHAR,
            "alt shift ctrl": chr(7)+NULL_CHAR, 
            "alt ctrl shift": chr(7)+NULL_CHAR, 
            "shift alt ctrl": chr(7)+NULL_CHAR, 
            "shift ctrl alt": chr(7)+NULL_CHAR, 
}
# if key is not dictionary - > send individual keys (like ctrl c)
keyDict = { "del": (NULL_CHAR+chr(76)+NULL_CHAR*5),
            "esc": (chr(41)+NULL_CHAR*5),
            "enter": (chr(40)+NULL_CHAR*5),
            "backspace":(chr(42)+NULL_CHAR*5),
            "f1":(chr(58)+NULL_CHAR*5), 
            "f2":(chr(59)+NULL_CHAR*5),
            "f3":(chr(60)+NULL_CHAR*5),
            "f4":(chr(61)+NULL_CHAR*5),
            "f5":(chr(62)+NULL_CHAR*5),
            "f6":(chr(63)+NULL_CHAR*5),
            "f7":(chr(64)+NULL_CHAR*5),
            "f8":(chr(65)+NULL_CHAR*5),
            "f9":(chr(66)+NULL_CHAR*5),
            "f10":(chr(67)+NULL_CHAR*5),
            "f11":(chr(68)+NULL_CHAR*5),
            "f12":(chr(69)+NULL_CHAR*5),
            "tab":(chr(43)+NULL_CHAR*5),
            "capslock":(chr(57)+NULL_CHAR*5),
            "ctrl": (chr(1)+NULL_CHAR*7),
            "alt": (chr(4)+NULL_CHAR*7),
            "shift":(chr(2)+NULL_CHAR*7),
            "ctrl alt": (chr(5)+NULL_CHAR*7),
            "alt ctrl": (chr(5)+NULL_CHAR*7),
            "shift ctrl": chr(3)+NULL_CHAR*7,
            "ctrl shift": chr(3)+NULL_CHAR*7, 
            "alt shift": chr(6)+NULL_CHAR*7,
            "shift alt": chr(6)+NULL_CHAR*7,
            "ctrl shift alt": chr(7)+NULL_CHAR*7,
            "ctrl alt shift": chr(7)+NULL_CHAR*7,
            "alt shift ctrl": chr(7)+NULL_CHAR*7, 
            "alt ctrl shift": chr(7)+NULL_CHAR*7, 
            "shift alt ctrl": chr(7)+NULL_CHAR*7, 
            "shift ctrl alt": chr(7)+NULL_CHAR*7, 
}

class keyboardDevice:
    NULL_CHAR = chr(0)
    rel_seq = NULL_CHAR*8
    
    def __write_report(self,report):
        with open('/dev/hidg0', 'rb+') as fd:
            print(report.encode())
            fd.write(report.encode())
    def __release(self):
        with open('/dev/hidg0', 'rb+') as fd:
            fd.write(self.rel_seq.encode())
    # a would be NULL_CHAR*2 + chr()
    def __char_to_reports(self,char):
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
    def __char_to_reports_NO_MODIFIER(self,char):
        NULL_CHAR = self.NULL_CHAR
        c=ord(char)
        if c>=97 and c<=122:#lower
            return(chr(c-93)+NULL_CHAR*5)
        elif c>=49 and c<=57:#1-9
            return(chr(c-19)+NULL_CHAR*5)
        elif c=='0':
            return(chr(39)+NULL_CHAR*5)
        elif char=='\n': #or you can do c == 10
            return(chr(40)+NULL_CHAR*5)
        elif c=='&':
            return(chr(32)+NULL_CHAR+chr(36)+NULL_CHAR*5)
        elif c==32: #whitespace, do print(ord(' ')) to check what whitespace c=ord(char) does
            return(chr(44)+NULL_CHAR*5)
        
        #print(c)
        #continue
    def sendString(self,string):
        NULL_CHAR = self.NULL_CHAR
        for c in string:
            print("Sending "+c+"...")
            self.__write_report(self.__char_to_reports(c))
            self.__release()

    def sendKey(self,keystr,modifier=None):
        NULL_CHAR = self.NULL_CHAR
        KEY_CHAR = NULL_CHAR*6
        keystr = keystr.lower()


        if modifier is None:
            MODI_CHAR = NULL_CHAR*2
        elif isinstance(modifier, str) :
            modifier = modifier.lower()
            MODI_CHAR = modiDict.get(modifier)
        else:
            print("Invalid modifier!")
            return

        
        if isinstance(keystr, str):
            if keystr in modiDict:
                KEY_CHAR = keyDict.get(keystr)
                self.__write_report(KEY_CHAR) #FIX IN DICTIONARY
                self.__release()
            else:
                if keystr in keyDict:
                    print("Sending "+modifier+"+"+keystr+"...")
                    KEY_CHAR = keyDict.get(keystr)
                    self.__write_report(MODI_CHAR+KEY_CHAR)
                    self.__release()
                else:
                    for c in keystr:
                        print("Sending "+modifier+"+"+c+"...")
                        KEY_CHAR = self.char_to_reports_NO_MODIFIER(c)
                        self.__write_report(MODI_CHAR+KEY_CHAR)
                        self.__release()
        else:
            print("Argument is not a string!")
            return

k=keyboardDevice()
k.sendKey("tab","alt")