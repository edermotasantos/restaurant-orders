import csv


def most_ordered_dish(order_list, customer):
    count = {}
    for order in order_list:
        most_frequent_order = order[1]
        if order[0] == customer:
            if order not in count:
                count[order[1]] = 1
            else:
                count[order[1]] += 1
            if count[order[1]] > count[most_frequent_order]:
                most_frequent_order = order[1]
    return most_frequent_order


def analyze_log(path_to_file):
    order_list = []
        
    with open(path_to_file) as file:
        orders_reader = csv.DictReader(
            file, fieldnames=["customer", "order", "day"]
        )
        for row in orders_reader:
            order_list.append((row["customer"], row["order"], row["day"]))

    return order_list

class TrackOrders:
    # aqui deve expor a quantidade de estoque
    order_list = []
    def __len__(self):
        self.data = self.order_list
        return len(self.data)

    def add_new_order(self, customer, order, day):
       self.order_list.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        order_list = analyze_log("data/orders_1.csv")
        orders = most_ordered_dish(order_list, customer)
        return orders

    def get_never_ordered_per_customer(self, customer):
        pass

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
