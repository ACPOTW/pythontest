# " 3.2. Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# Example1
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Constraints:
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106"

# 递归
def GetS(nums1, m, nums2, n, k):
    # n1列最后一个数小于n2列的中间数
    if m >= len(nums1):
        return int(nums2[n+k-1])
    if n >= len(nums2):
        return int(nums1[m+k-1])
    # k=1说明排好序后第一个数就是要取的
    if k == 1:
        return int(min(nums1[m], nums2[n]))

    # 比较的下标
    x1 = m + int(k/2) - 1
    x2 = n + int(k/2) - 1

    nums1_max = None
    nums2_max = None
    # 防止下标越界
    if x1 < len(nums1):
        nums1_max = int(nums1[x1])
    if x2 < len(nums2):
        nums2_max = int(nums2[x2])

    if nums1_max > nums2_max:
        return GetS(nums1, m, nums2, n+int(k/2), k-int(k/2))
    return GetS(nums1, m+int(k/2), nums2, n, k-int(k/2))


if __name__ == '__main__':
    nums1_str = input("nums1=")
    nums2_str = input("nums2=")

    nums1_list = nums1_str.replace('[', '').replace(']', '').split(',')
    nums2_list = nums2_str.replace('[', '').replace(']', '').split(',')

    AllLen = len(nums1_list)+len(nums2_list)
    if AllLen % 2 == 0:
        result = (GetS(nums1_list, 0, nums2_list, 0, int(AllLen/2)) + GetS(nums1_list, 0, nums2_list, 0, int(AllLen/2) + 1))/2
    else:
        # k为第几个数，当为奇数时需+1
        result = GetS(nums1_list, 0, nums2_list, 0, int((AllLen+1)/2))

    print(result)

