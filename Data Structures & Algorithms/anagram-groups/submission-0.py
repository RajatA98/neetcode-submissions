class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        temp = []
        v = []
        #go through the list of strings
        for i in range(len(strs)):
            #sort each string
            if strs[i] in v:
                continue
            s_w = sorted(strs[i])
            #create a list of matching anagrams to this string
            temp.append(strs[i])
            v.append(strs[i])
            for j in range(i+1,len(strs)):
                s2 = sorted(strs[j])
                if s_w == s2:
                    temp.append(strs[j])
                    v.append(strs[j])

            #append answer
            ans.append(temp)
            #clear temp
            temp = [] 
        return ans

        


        