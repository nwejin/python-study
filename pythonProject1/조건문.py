if True:
    print('true')

score = 30
if score > 80:
    print('A')
elif score > 50:
    print('B')
else:
    print('fail')

ages = [22, 21, 17, 32, 4, 28, 19, 8]
total_price = 0

for i in ages:
    if i >=20:
        total_price = total_price + 8000
    elif i >= 10:
        total_price = total_price + 5000
    else:
        total_price = total_price + 2500
print('입장료는', total_price, '원 입니다.')

game = 12
avg = 23
if game >= 10 and avg >= 20:
    print('mvp!!')

suspects=[['거위','새','암컷'], ['푸들','개','수컷'],['비글','개','암컷']]
print(suspects[0][0])
for suspect in suspects:
    print(suspect)
    if suspect[1] == '개' and suspect[2] == '암컷':
        print('범인은', suspect[0], '입니다')

print('0~2 까지 수 중 하나를 입력해주세요!')
rps = ['가위', '바위', '보']
a, b = map(int, input().split())

player = rps[a]
computer = rps[b]
print('player1:', player,' & ','player2:',computer)

if player == '가위' and computer == '가위':
    print('draw')
elif player == '가위' and computer == '바위':
    print('player2 win!')
elif player == '가위' and computer == '보':
    print('player1 win!')
elif player == '바위' and computer == '가위':
    print('player1 win!')
elif player == '바위' and computer == '바위':
    print('draw!')
elif player == '바위' and computer == '보':
    print('player2 win!')
elif player == '보' and computer == '가위':
    print('player2 win!')
elif player == '보' and computer == '바위':
    print('player1 win!')
elif player == '보' and computer == '보':
    print('draw!')

