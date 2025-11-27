# def is_a_triangle(a, b, c):
#     if a + b <= c or b + c <= a or c + a <= b:
#         return False
#     return True

# 利用缩小逻辑范围，讲代码简化
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

# unit test block
a = float(input('Enter the first side\'s length: '))
b = float(input('Enter the second side\'s length: '))
c = float(input('Enter the third side\'s length: '))

if is_a_triangle(a, b, c):
    print('Yes, it can be a triangle.')
else:
    print('No, it can\'t be a triangle.')

# 是否直角三角形
def is_a_right_triangle(a, b, c):
    # 异常处理
    if not is_a_triangle(a, b, c):
        return False
    # 验证直角三角形
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
print(is_a_right_triangle(5, 3, 4))
print(is_a_right_triangle(1, 3, 4))


# 三角形面积计算公式
def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5
 
 
def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)
 
 
print(area_of_triangle(1., 1., 2. ** .5))