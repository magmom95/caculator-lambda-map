def add(a, b): return a+b


def substract(a, b): return a-b


def multiply(a, b): return a*b


def divide(a, b): return a/b


a, b = map(int, input("숫자를 입력하세요 ").split())
result = add(a, b)
print("덧셈 결과는 %d 입니다." % result)
result1 = substract(a, b)
print("뺀 결과는 %d 입니다." % result1)
result2 = multiply(a, b)
print("곱셈 결과는 %d 입니다." % result2)
result3 = divide(a, b)
print("나눈 결과는 %d 입니다." % result3)
