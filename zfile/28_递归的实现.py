# n! =1*2*3...*(n-1)*n
def jiecheng(n):
    result = 1
    for temp in range(1, n + 1):
        result = result * temp
    return result


print(jiecheng(4))

def digui(num):
    if num == 1:
        return num
    return num * digui(num - 1)


print(digui(4))
