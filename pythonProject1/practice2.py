a, b = input().split()

a = int(a)
b = int(b)

# 기본 if
if b > a:
    print("b > a")
elif a > b:
    print("a > b")
else:
    print("a = b")

# while - break
i = int(input())
while i <= 6:
    print(i)
    if i == 3:
        break
    i += 1


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break