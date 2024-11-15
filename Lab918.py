# LAB 9.18
# Roberto Sanchez
# 041144901

def in_order(nums):
    if all(nums[i] >= nums[i + 1] for i in range(0, len(nums) - 1)):
        return True
    else:
        return False

# Type your code here.

if __name__ == '__main__':
    # Test out-of-order example
    nums1 = [5, 6, 7, 8, 3]
    if in_order(nums1):
        print('In descending order')
    else:
        print('Not in order')

    # Test in-order example
    nums2 = [10, 8, 7, 6, 5]
    if in_order(nums2):
        print('In descending order')
    else:
        print('Not in order')