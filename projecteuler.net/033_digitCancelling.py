# need improvement
import math

nums = 1
denoms = 1

for denominator in range(10, 100):
    for numerator in range(10, denominator):
        if denominator % 10 == 0 or numerator % 10 == 0:
            # "or" cause you cannot leave "0" in num or denom after cancelling
            continue
        elif numerator == denominator:
            # 1 is not less than 1
            continue
        else:
            a = numerator // 10
            b = numerator % 10
            c = denominator // 10
            d = denominator % 10
            # ifs can be done better
            if a == c:
                if numerator / denominator == b / d:
                    nums *= b
                    denoms *= d
            elif a == d:
                if numerator / denominator == b / c:
                    denoms *= c
                    nums *= b
            elif b == c:
                if numerator / denominator == a / d:
                    nums *= a
                    denoms *= d
            elif b == d:
                if numerator / denominator == a / c:
                    nums *= a
                    denoms *= c

print(denoms // math.gcd(nums, denoms))
