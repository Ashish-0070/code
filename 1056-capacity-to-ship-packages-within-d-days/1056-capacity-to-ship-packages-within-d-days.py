class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def canShip(capacity):
            curr_weight = 0
            required_days = 1
            for w in weights:
                if curr_weight + w > capacity:
                    required_days += 1
                    curr_weight = 0
                curr_weight += w
            return required_days <= days

        left, right = max(weights), sum(weights)

        while left < right:
            mid = (left + right) // 2
            if canShip(mid):
                right = mid
            else:
                left = mid + 1

        return left

        