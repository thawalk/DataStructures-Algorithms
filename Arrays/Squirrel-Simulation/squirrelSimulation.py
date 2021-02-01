class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        total_dist = 0
        d = float("-inf")
        for nut in nuts:
            total_dist += (self.distance(nut, tree) * 2)
            d = max(d, self.distance(nut, tree) - self.distance(nut, squirrel))
        return total_dist - d
    
    def distance(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])