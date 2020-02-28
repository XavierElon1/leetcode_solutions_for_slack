#Solution by dannyhp

def searchRange(self, nums: List[int], target: int) -> List[int]:
    # Algorithm must be in O(log n) ==> binary search.
    if len(nums) < 1:
        return [-1, -1]
    firstPosition = self.binarySearch(nums, target, True)
    if firstPosition == -1:
        return [-1, -1]
    else:
        return [firstPosition, self.binarySearch(nums, target, False)]
def binarySearch(self, nums: List[int], key: int, findFirst: bool) -> int:
    # Assumes list is in ascending order.
    index = -1
    left, right = 0, len(nums) - 1
    while left <= right:
        middle = left + ((right - left) // 2)
        if nums[middle] == key:
            index = middle
            if findFirst:
                right = middle -1
            else:
                left = middle + 1
        elif nums[middle] < key:
            left = middle + 1
        elif nums[middle] > key:
            right = middle - 1
    return index
