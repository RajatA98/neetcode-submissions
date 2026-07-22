class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #look at curtemp
        #keep traversing temp while temp <= cur 
        #keep that count
        #perform for all temp O(n2)
        result = [0] * len(temperatures)
        for i,t in enumerate(temperatures):
            j = i+1
            count = 0
            flag = False
            while j < len(temperatures):
                count += 1
                if temperatures[j] > t:
                    flag = True
                    break
                j += 1

            if flag == False:
                count = 0
            result[i] = count
        return result

        