# TODO: quick select
from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        bucket_list = [[] for _ in range(max(freq.values()) + 1)]
        for num, freq in freq.items():
            bucket_list[freq].append(num)

        res = []
        for index in range(len(bucket_list) - 1, 0, -1):
            for num in bucket_list[index]:
                res.append(num)
                if len(res) == k: return res
        
        return res

    '''
    [1,1,1,2,2,3]
    1:3
    2:2
    3:1

    [[],[3],[2],[1]]
    [[1],[2],[3]]
    res
    [1,2]
    '''
    def top_k_frequent(self, nums, k):
        # Count frequencies
        freq = Counter(nums)
        # Sort items by frequency descending
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        # Take top k elements
        return [item[0] for item in sorted_items[:k]]

    # Example usage:
    # nums = [1,1,1,2,2,3]
    # k = 2
    # print(top_k_frequent(nums, k))  # Output: [1, 2]

    # write min heap code
    def top_k_frequent_min_heap(self, nums, k):
        from heapq import heappush, heappop
        freq = Counter(nums)
        min_heap = []
        
        for num, count in freq.items():
            heappush(min_heap, (count, num))
            if len(min_heap) > k:
                heappop(min_heap)
        
        return [num for count, num in min_heap]
    
