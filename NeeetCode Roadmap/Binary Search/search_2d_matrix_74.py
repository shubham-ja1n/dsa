import math

def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    l, r =0, len(matrix) - 1

    while l<r:
        mid = math.ceil((l+r) / 2)

        if matrix[mid][0] == target:
            return True
        elif matrix[mid][0] > target:
            r = mid -1
        else:
            l = mid
    row_no = min(l,r)

    l, r = 0, len(matrix[0])-1

    while l<=r:
        mid = math.ceil((l+r) / 2)

        if matrix[row_no][mid] == target:
            return True
        elif matrix[row_no][mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    
    return False