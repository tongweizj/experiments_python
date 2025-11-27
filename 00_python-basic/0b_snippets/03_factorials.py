# Factorials 阶乘
# 0! = 1 (yes! it's true)
# 1! = 1
# 2! = 1 * 2
# 3! = 1 * 2 * 3
# 4! = 1 * 2 * 3 * 4
# :
# :
# n! = 1 * 2 * 3 * 4 * ... * n-1 * n


def factorial_function(n):
    # 异常处理
    if n < 0:
        return None
    # 特殊情况
    if n < 2:
        return 1
    # 正常逻辑
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product
 
# testing
for n in range(1, 6): 
    print(n, factorial_function(n))

# 优化
# 1. 代码完整，有异常、特殊情况处理，也有测试模块