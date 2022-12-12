''' Options for solving the problem of creating the sum of a sequence '''

def chain_sum(num):
    res = num
    def warp(num_2=None):
        nonlocal res
        if num_2 == None:
            return res
        res += num_2
        return warp
    return warp


def chain_sum_v2(num):
    res = num
    def warp(num_2=None):
        nonlocal res
        try:
            num_2 = int(num_2)
        except TypeError:
            return res
        res += num_2
        return warp
    return warp


def chain_sum_v3(num):

    def warp(num_2=None):

        def inner():
            warp.res += num_2
            return warp

        switch = {
            type(None): lambda: warp.res,
            int: inner
        }

        return switch[type(num_2)]()
    warp.res = num
    return warp


class ChainSum:
    def __init__(self, num):
        self.num = num

    def __call__(self, val=0):
        return ChainSum(self.num + val)

    def __str__(self):
        return str(self.num)


class ChainSumV2(int):
    def __call__(self, val=0):
        return ChainSumV2(self + val)

print(ChainSumV2(5)) # 5
print(ChainSumV2(5)(2)) # 7
print(ChainSum(5)(2)(-10)) # -3