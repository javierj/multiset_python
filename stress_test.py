from multidict import Multibag
import random

# Products are tuples of elements ids:

orders = []
ordersnum = 5000000
ordersize = 5
topproduct = 1000

for i in range(0, ordersnum):
    order = []
    for j in range(0, ordersize):
        order.append(random.randint(0, topproduct))
    if (i % 1000) == 0:
        print(len(orders))
    orders.append(order)

print("Orders done: ", len(orders))



mb = Multibag()
mb.put_orders(orders)

sug_1 = mb.sugestions(1)
print(sug_1)
sug_2 = mb.sugestions(2)
print(sug_2)
