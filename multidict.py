import operator

class Multibag():
    def __init__(self):
        self.d = dict()

    def put(self, key1, key2):
        if key1 not in self.d:
            sec = dict()
            sec[key2] = 1
            self.d[key1] = sec
        else:
            sec = self.d[key1]
            if key2 in sec:
                sec[key2] = (sec[key2]+1)
            else:
                sec[key2] = 1

    def put_orders(self, orders):
        """ Adds a list of orders, each order is a tuple with the id of the buyed products
        sample: orders = [(1, 2, 3), (1, 2), (2, 3, 4), (2, 3, 5), (1, 2, 5), (1,6)]
        """
        for order in orders:
            for i in range(0, len(order) - 1):
                for j in range(i + 1, len(order)):
                    self.put(order[i], order[j])


    def sugestions(self, key1):
        sec = self.d[key1]
        sorted_x = sorted(sec.items(), key=operator.itemgetter(1), reverse=True)
        #just product ids - res = [x[1] for x in sorted_x]
        return sorted_x
