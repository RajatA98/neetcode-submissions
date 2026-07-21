class Solution:

    def encode(self, strs: List[str]) -> str:
        #encode using length of str 
        encoded = []
        for s in strs:
            encoded.append(str(len(s)))
            #adding # delimiter 
            encoded.append('#')
            encoded.append(s)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        #travese the chars until #
        #store that number and read those many charters until end of string 
        decoded = []
        #read chars until #
        #that will be the size of string
        #slice the string of that size
        i = 0
        while i < len(s):
            num = ""
            while s[i] != '#':
                num += s[i]
                i+=1
            size = int(num)
            decoded.append(s[i+1:i+size+1])
            i += size + 1

        return decoded


    
            


