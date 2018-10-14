# サンプル
print("hello world!")
sum1 = 2 + 3
if sum1 is not (int):
    print(sum1)


# どうしたってこのままではおわれない。
def Add13(data):
    """
    
    """
    data += 13
    return data


if sum1 < 14:
    sum2 = Add13(sum1)
    print(sum2)
if sum2 > 4:
    print(sum2.__abs__)

ans = float(input("input number you like"))
print("you input {}".format(ans))
