# for num in range(3):
#     print('안녕 거북이', num)

nums = 0
while nums < 3:
    print('안녕 거북이', nums)
    nums = nums + 1

run = 1
while run <= 5:
    print (run, '바퀴')
    run = run + 1
print('종료!')
#
# name = input('name? :')
# print(name, 'hi!')
#

# answer = ''
# while answer != '런던':
#     answer = input('영국의 수도는 어디일까요? : ')
# print('정답!')


# count = 0
# while count < 3:
#     count = count + 1
#     if count == 2:
#         # continue
#         break
#     print(count)


while True:
    answer = input('런던, 파리, 서울 중 영국의 수도는 어디일까요? :')
    if answer == '런던':
        print('정답입니다!')
        break
    elif answer == '파리':
        print('파리는 프랑스의 수도입니다.')
    elif answer == '서울':
        print('서울은 대한민국의 수도입니다.')
    else:
        print('보기 중에서 골라주세요')

