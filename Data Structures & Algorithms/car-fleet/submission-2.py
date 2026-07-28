class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #let's stort the cars by closest to furthest from target
        #create a merged list 

        cars = []

        for p, s in zip(position, speed):
            cars.append((p,s))

        cars.sort(reverse=True)

        #travese through the cars on the highway
        #calculate fleets by seeing if cars behind will catch up

        #push each fleet to stack until cars reach target

        stack = []

        for c in cars:
            #calculate time it takes for current car to reach target
            time = (target - c[0])/c[1]

            stack.append(time) #car in front is bottom of stack

            #check if car behind is faster than car infront
            #merge to car in front

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                #fleet is formed
        
        return len(stack)

            
            
            
                

        