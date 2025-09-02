# https://leetcode.com/problems/time-based-key-value-store/
class TimeMap:

    def __init__(self):
        self.cache = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.cache: self.cache[key] = []
        self.cache[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        pair = self.cache.get(key, [])
        left, right = 0, len(pair) - 1
        res = -1
        while left <= right:
            mid = left + (right - left) // 2
            pre_time = pair[mid][1]

            if pre_time <= timestamp: 
                res = mid
                left = mid + 1
            else: right = mid - 1 
            
        return pair[res][0] if res != -1 else ""

"""
["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
{
    foo: [(bar, 1), (bar2, 4)]
}
pre = 1, 4
1 < 3 -> bar
4 < 5 -> bar2

1,4
  l 
  r
m
"""
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)