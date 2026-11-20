class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        fleet=[]
        cars=sorted(zip(position,speed),reverse=True)
        for pos,spd in sorted(zip(position,speed),reverse=True):
            time =(target-pos)/spd
            if not fleet or time>fleet[-1]:
                fleet.append(time)
        return len(fleet)