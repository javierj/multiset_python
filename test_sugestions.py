from multidict import Multibag

# Products are tuples of elements ids:

orders = [(1, 2, 3), (1, 2), (2, 3, 4), (2, 3, 5), (1, 2, 5), (1,6)]


mb = Multibag()
mb.put_orders(orders)

sug_1 = mb.sugestions(1)
print(sug_1)
sug_2 = mb.sugestions(2)
print(sug_2)

