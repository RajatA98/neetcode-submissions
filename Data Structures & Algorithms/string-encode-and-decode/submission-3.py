class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        #encode using length 
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        return "".join(res)
            


    def decode(self, s: str) -> List[str]:
        #read first char to get length of first string
        #slice the word then look at next lenght 
        #repeat until s is fully read through
        i = 0
        decoded_strs = []
        len_w = ""
        while i < len(s):
            if s[i] == '#':
                print(len_w)
                decoded_strs.append(s[i+1:i+1+int(len_w)])
                i = i+1+int(len_w)
                len_w = ""
            else:
                len_w += s[i]
                i += 1
        return decoded_strs
            
        
            
             
            


            
            
