print(1)
print(-2)
print(3.14)

print(1 + 2)

print((1+3)*3)

# 제곱
print(5 ** 2)

# 몫
print(5 // 2)

# 나머지
print(5 % 2)

print('내 이름은 "최진"입니다.')
a = '안녕'
print('ㅋㅋ' + a)
print('ㅋㅋㅋㅋ' + a)
print('ㅋㅋ'*3)
print('빨' + '주' + '노' + '초' + '파' + '남' + '보')

count = 0
print(count + 1)
# 변수는 값 저장 or 값에 이름을 부여하는 것이다!


coffe = 4100
juice = 4600
tea = 3900

print(coffe*3 + juice*2 + tea*1)
print(coffe*4 + juice*3 + tea*3)
print(coffe*1 + juice*1 + tea*2)

# 실습
print(3 + 1 - 2)
print(3 - 1 + 2)
print(3 * 1 - 2)
num1 = 9
num2 = 2
print(num1 // num2)
print(num1 % num2)
print(8.5 // 2)
print('말랑' *2)

# list
# .append()

list1 = []
list1.append('1번')
print(list1)
list1.append('2번')
print(list1)
list1.insert(0, '0번')
print(list1)

print(list1[0])

del list1[0]
print(list1)

candies = ['딸기', '레몬', '수박', '박하', '우유']
candies.append('콜라')
candies.append('포도')
print(candies)

del candies[3]
print(candies)
print(candies[1:3]) # 1번 , 2번 인덱스를 가져옴
print('고양이는 ', candies[0])
print('오리는 ', candies[1])
dodo = candies[3:6]
print('도도는', dodo)

animals = ['고양이', '오리', '도도새']
animals.sort()
print(animals)
animals.sort(reverse = True)
print(animals)

print(animals.count('고양이'))

nums = [1,3]
nums[1] = 2
nums.append(3)
nums.insert(3, 4)
print(nums)


for num in range(3):
    print('hello', num)

for nums in [0,1,2]:
    print(nums)

test = ['1번', '2번', '3번']

for num1 in test:
    print(num1)

players = ['공작부인', '흰 토끼', '하트잭', '모자장수']

for player in players:
    print(player, '나가라!')

for letter in '국회도서관':
    print(letter)

for x in range (2, 10):
    for y in range(1, 10):  # 시작 1, 끝 9
        print(x, 'x', y, '=', x * y)

roses = ['하얀장미', '하얀장미', '하얀장미']
for i in range(3):
    roses[i] = '빨간장미'
print(roses)

