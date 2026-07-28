class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #traverse through the temperatures
        #solve for current temp and day check how many days until temp is greater store in result
        #o(n2)
        #O(n)
        #at cur temp check if it greater than temp of previous day
        #if yes take current day - previous day if not start a new streak
        #stack to keep track of unsolved days

        stack = []

        result = [0] * len(temperatures) #defaulting result to 0

        for i, t in enumerate(temperatures):
            #solve for current temp
            while stack and t > stack[-1][0]:
                result[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            
            #curent temp

            stack.append((t,i))

    
        return result
                
        