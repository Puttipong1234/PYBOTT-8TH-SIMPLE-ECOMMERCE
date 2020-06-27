# result ค่า X 
# a^2 + 2ab + b^2 + c + d = x

# a = 5
# b = 7
# c = 10
# d = 2

# result1 = a*a
# result2 = 2*a*b
# result3 = b*b
# res = result1+result2+result3+c+d

# print(res)

def solve_equation(a,b,c,d=2):
    result1 = a*a
    result2 = 3*a*b
    result3 = b*b
    res = result1+result2+result3+c+d
    print(res)
    return res

ผลลัพธ์1 = solve_equation(a=5,b=7,c=10)
ผลลัพธ์2 = solve_equation(a=15,b=70,c=100,d=25)
