# 사칙연산계산기
# 2016244037 김광용

a = int(input('첫번째 피연산자를 입력해주세요 >> '))
b = int(input('두번째 피연산자를 입력해주세요 >> '))

print("\n\n ---- 결과 ----\n\n")
result = a + b
print(result)
print(a, '+', b, '=', result)
print("%d + %d = %d\n" % (a, b, result))
result = a - b
print(a, '-', b, '=', result)
print("%d - %d = %d\n" % (a, b, result))
result = a * b
print(a, '*', b, '=', result)
print("%d * %d = %d\n" % (a, b, result))
result = a / b
print(a, '/', b, '=', result)
print("%d / %d = %f\n" % (a, b, result))
