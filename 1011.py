from typing import List
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        mn = 0
        sm =0

        for i in weights:
            mn = max(mn, i)
            sm += i

        mn = max(sm//D, mn)
        s = mn
        e = sm
        minCap = float('inf')

        while s <= e:
            mid = (s+e)//2
            days = self.canShip(weights, mid)
            if days<=D:
                minCap = min(minCap, mid)
                e = mid-1
            else:
                s = mid+1

        return minCap

    def canShip(self, weights, limit):
        days = 0
        curr = 0

        for item in weights:
            if item+curr==limit:
                days+=1
                curr=0
            elif item+curr>kimit:
                days+=1
                curr =item
            else:
                curr += item
        return days if curr ==0 else days+1
