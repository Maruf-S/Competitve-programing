class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        cur_plant_time = 0
        res = 0
        for gt, pt in sorted(zip(growTime, plantTime))[::-1]:
            cur_plant_time += pt
            res = max(res, cur_plant_time + gt)
        return res