## Binary Search
### Time Complexity:
O(log n)
### Algo
- mid = l + ((r - l)//2) better than r + l // 2 (overflow for 2 ^ 32 bits)
- l, r = 0, len(n) - 1 search left and right
- Most comparison by pointers:
    - l = mid + 1
    - r = mid - 1