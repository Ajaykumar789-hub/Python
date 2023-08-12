#BST


def searchInsert(nums, target: int) -> int:
    low,high=0,len(nums)-1
    if high<low:
        return None
    mid=(low+high)//2
    if nums[mid]==target:
        return mid
    elif target <nums[mid]:
        return mid-1
    else:
        return mid+1

nums=[1,3,5,6]

searchInsert(nums,2)