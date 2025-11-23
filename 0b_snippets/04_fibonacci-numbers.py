# Fibonacci numbers
# 一个数等序列前2个数之和
# fib_1 = 1 
# fib_2 = 1 
# fib_3 = 1 + 1 = 2 
# fib_4 = 1 + 2 = 3 
# fib_5 = 2 + 3 = 5 
# fib_6 = 3 + 5 = 8 
# fib_7 = 5 + 8 = 13
# fib_n = fin_n-2 + fin_n-1

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    # 用for 循环简单直观的复述了算法描述
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(1, 10):  # testing
    print(n, "->", fib(n))

