test = (1,)
print(type(test))

test2 = (1)
print(type(test2))

clover = ('클로버', '하트', '네잎클로버')
print(clover[0])

color = 'red', 'blue', 'white'

black = 255, 255, 255 #패킹
r, g, b = black #언패킹
print('R', r, 'G', g, 'B', b)


dodo = '박하맛'
alice = '딸기맛'
print('dodo', dodo, 'alice', alice)
dodo, alice = alice, dodo
print('dodo', dodo, 'alice', alice)

