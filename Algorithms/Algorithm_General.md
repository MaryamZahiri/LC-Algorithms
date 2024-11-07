## Gready Algorithm 
1. The greedy strategy is to always add characters to the current partition as long as they don't repeat/or tasks is not overlapped
2. If a character repeats/overlapped, you complete the partition and start a new one, ensuring each partition only contains unique characters

1. Local optimality: Add characters to the partition (set) as long as they are unique.
2. Global optimality: When a duplicate is found, complete the current partition and start a new one immediately.