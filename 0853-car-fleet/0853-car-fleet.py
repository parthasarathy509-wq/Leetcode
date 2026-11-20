class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        slowest_time = 0.0
        
        # Sorts integer indices directly in C without building (pos, spd) tuples
        for i in sorted(range(len(position)), key=position.__getitem__, reverse=True):
            time = (target - position[i]) / speed[i]
            if time > slowest_time:
                fleets += 1
                slowest_time = time
                
        return fleets
