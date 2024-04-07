class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numbers = []
        for idx, val in enumerate(nums):
            numbers.append((idx, val))
        numbers.sort(key=lambda x: x[1])

        a, b = 0, len(nums) - 1
        total = numbers[a][1] + numbers[b][1]
        while total != target:
            if total > target:
                b -= 1
            elif total < target:
                a += 1
            total = numbers[a][1] + numbers[b][1]

        return [numbers[a][0], numbers[b][0]]