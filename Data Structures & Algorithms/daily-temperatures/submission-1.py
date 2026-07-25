class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #let's initialize result array 0 counts 
        result = [0] * len(temperatures)
        #we can use a stack 
        stack = []
        #Traverse through the temps
        

        for i, temp in enumerate(temperatures):
           
           #solve for current temp
            while stack and temp > stack[-1][0]:
                top = stack.pop()
                result[top[1]] = i - top[1]

            #push cur temp to solve for

            stack.append((temp,i))
            
            

        return result

            