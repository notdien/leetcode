class Solution():
    def __init__(self):
        pass

    def solved(self, x):
        # if it is negative, just return
        if x < 0:
            return

        # initiate a binary search
        low = 1
        high = x
        sqrt = 0

        while low <= high:
            mid = x // 2

            # compare the given x with the mid * mid
            compare = mid * mid
            # if compare is higher, go lower
            # we go towards the left side
            if compare > high:
                high = mid - 1

            # if it is smaller then it could potientally be the square root
            else:
                sqrt = compare
                # we also have to check if there is any larger number that is smaller than x

        return sqrt


# initiate a object
result = Solution()
print(result.solved(15))
