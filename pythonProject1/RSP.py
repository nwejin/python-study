import random

while True:
    a = input('0~2 까지 수 중 하나를 입력해주세요! (게임 종료를 희망하면 끝을 입력해주세요)')
    rps = ['가위', '바위', '보']

    if a == '끝':
        break
    elif a not in ['0', '1', '2']:
        print('0, 1, 2, 끝 중에서 입력해주세요!')
        continue

    player = rps[int(a)]
    computer = random.choice(rps)

    print('player1:', player, ' & ', 'computer:', computer)

    if player == computer:
        print('draw')
    elif player == '가위':
        if computer == '바위':
            print('computer win')
        else:
            print('player win!')
    elif player == '바위':
        if computer == '보':
            print('computer win')
        else:
            print('player win!')
    elif player == '보':
        if computer == '가위':
            print('computer win')
        else:
            print('player win!')


# if player == '가위' and computer == '가위':
#     print('draw')
# elif player == '가위' and computer == '바위':
#     print('player2 win!')
# elif player == '가위' and computer == '보':
#     print('player1 win!')
# elif player == '바위' and computer == '가위':
#     print('player1 win!')
# elif player == '바위' and computer == '바위':
#     print('draw!')
# elif player == '바위' and computer == '보':
#     print('player2 win!')
# elif player == '보' and computer == '가위':
#     print('player2 win!')
# elif player == '보' and computer == '바위':
#     print('player1 win!')
# elif player == '보' and computer == '보':
#     print('draw!')