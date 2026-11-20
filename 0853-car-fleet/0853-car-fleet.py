class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Bucket array where index = road position, value = time to reach target
        times = [0.0] * target
        for pos, spd in zip(position, speed):
            times[pos] = (target - pos) / spd
            
        fleets = 0
        slowest_time = 0.0
        
        # Scan backward from closest to target -> 0
        for pos in range(target - 1, -1, -1):
            time = times[pos]
            if time > slowest_time:
                fleets += 1
                slowest_time = time
                
        return fleets
