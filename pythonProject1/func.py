def test_func():
    print('함수 테스트 입니다.')

test_func()


def add(num1, num2):
    return num1 + num2

print(add(1,2))


def multi(num1, num2):
    return num1 + num2, num1 * num2

print(multi(1,2))


def judge_cards(name):
    for i in range(1,4):
        print(name, i,'유죄!')

judge_cards('하트')
judge_cards('클로버')
judge_cards('스페이드')

import random

animals = ('dog','cat','rat')
cards = ('하트','스페이드','클로버')

def random_func():
    print(random.choice(animals))
    print(random.sample(animals,2))
    print(random.randint(1,10))
    print(random.choice(cards),'유죄!')

random_func()
