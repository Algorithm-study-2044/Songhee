a, b, e, c, d, f = list(map(int, input().split()))

D = a*d-b*c
x = ( d*e-b*f)//D
y = (-c*e+a*f)//D # int((분자)/D) 가 정확하지 않은 이유?

print(f'{x} {y}')