jin = {'이름': '최진', '나이': 28}
print(jin)
jin['거주지'] = '대방역'
print(jin)

print(jin['이름'])
jin['나이'] = 29
print(jin['나이'])
print(jin.get('나이'))
del jin['거주지']
print(jin)

order = {'스페이드1': '비빔라면', '다이아2': '매운라면'}
print('주문 1:', order)
order['클로버3'] = '카레라면'
print('주문 2:', order)
order['다이아2'] = '짜장라면'
print('주문 3:', order)
del order['스페이드1']
print('주문 4:', order)

import random

rps = ['가위','바위','보']

result = {
    ('가위', '보'): True,
    ('가위', '바위'): False,
    ('바위', '가위'): True,
    ('바위', '보'): False,
    ('보', '바위'): True,
    ('보', '가위'): False,
}

while True:
    player = input('가위/바위/보/끝: ')
    computer = random.choice(rps)

    if player == '끝':
        break
    print(player, computer)

    if player == computer:
        print('draw!')
    elif result[(player, computer)]:
        print('win!')
    else:
        print('lose')
