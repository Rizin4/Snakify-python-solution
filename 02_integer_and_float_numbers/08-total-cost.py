A = int(input())
B = int(input())
N = int(input())

cent = ((A * 100) + B) * N
dollar = cent // 100
cent = cent % 100
print(str(dollar) + " " + str(cent))
