class Solution():
    def __init__(self):
        pass

    def solved(self, x):
        # initiate a binary search
        low = 1
        high = x

        # we need a variable to store our return value
        sqrt = x

        while low <= high:
            # if we just do low+high/2, the low+high = 3,000,000,001, which will result in overflow error
            mid = int(low + (high-low)/2)
            print(mid)

            # if we get a case of 2x2 = 4, then we just return 2
            if mid*mid == x:
                return mid
            # if comparison is higher, go lower
            # we go towards the left side
            elif mid*mid > x:
                high = mid - 1
            # if it is comparison is smaller, it might be the correct answer
            else:
                sqrt = mid
                # checks to make sure if there are no numbers bigger that could be sqrt root
                # if there is - repeats loop
                # otherwise we just return sqrt
                low = mid + 1

        return sqrt


# initiate a object
result = Solution()
print(result.solved(9))
