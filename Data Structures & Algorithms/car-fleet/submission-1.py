class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #let's start by sorting the cars by position
        cars = []

        for p,s in zip(position, speed):
            cars.append((p,s))

        #sort from closest to target 
        cars.sort(reverse=True)

        #calculate how long each car would take to rach the target
        #compare the curent time to previous we will use a stack for this
        #if the time is <= then it is fleet and we can merge the 2
        #else new fleet

        stack = []

        for c in cars:
            time = (target - c[0])/c[1]
            
            stack.append(time)
            
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)








                



            