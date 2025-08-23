from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        times = [(target - p)/s for p, s in cars[::-1]]
        fleet = 1
        last_time = times[0]
        for time in times:
            # skip the faster and equal
            if time <= last_time: continue
            # extend slower greater by new fleet
            last_time = time
            fleet += 1
        return fleet

    def carFleetStack(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        stack = []
        # start from closest distance because it is not effected by previous one but other prev is depend on that
        for p, s in cars[::-1]:
            cur_time = (target - p) / s
            # skip or merge if faster (less time) or equal than the closest distance
            if stack and stack[-1] >= cur_time: continue
            # extend if it is slower (greater time)
            stack.append(cur_time)
        return len(stack)
    """
    T: O(nlogn) S: O(n)
    """
"""
[1] -> count 1


0,3,5,8,10
1,3,1,4,2
12,3,7,1,1
i
monotonic increasing
end position
[1]
[1]
[1,7,12]
extend: greater
shrink or ignore: == or less -> 2nd fast and merge by greater


"""