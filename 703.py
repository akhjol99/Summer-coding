from typing import List
import heapq
class kthlargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for i in nums:
            if len(self.heap) < k:
                heapq.heappush(self.heap, i)
            else:
                if i > self.heap[0]:
                    heapq.heappushpop(self.heap, i)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            if val > self.heap[0]:
                heapq.heappushpop(self.heap, val)

        return self.heap[0]

k = 3
arr = [4, 5, 8, 2]
obj = kthlargest(k, arr)
n = obj.add(3)
print(n)
