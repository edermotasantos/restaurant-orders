import csv


def least_busy_day(order_list):
    count = {}
    least_busy = order_list[0][2]
    for order in order_list:
        if order[2] not in count:
            count[order[2]] = 1
        else:
            count[order[2]] += 1
        if count[order[2]] < count[least_busy]:
            least_busy = order[2]
    return least_busy


def busiest_day(order_list):
    count = {}
    most_busy = order_list[0][2]
    for order in order_list:
        if order[2] not in count:
            count[order[2]] = 1
        else:
            count[order[2]] += 1
        if count[order[2]] > count[most_busy]:
            most_busy = order[2]
    return most_busy


def days_never_visited_per_customer(order_list, customer):
    days_of_the_week = set()
    customer_went = set()
    for order in order_list:

        days_of_the_week.add(order[2])

        if order[0] == customer:
            customer_went.add(order[2])

    for day in customer_went:
        days_of_the_week.discard(day)

    customer_data = days_of_the_week
    return customer_data


def never_ordered_per_customer(order_list, customer):
    all_orders = set()
    customer_orders = set()
    for order in order_list:

        all_orders.add(order[1])

        if order[0] == customer:
            customer_orders.add(order[1])

    for customer_order in customer_orders:
        all_orders.discard(customer_order)

    customer_data = all_orders
    return customer_data


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
        return len(self.order_list)

    def add_new_order(self, customer, order, day):
        self.order_list.append((customer, order, day))

    def get_most_ordered_dish_per_customer(self, customer):
        order_list = analyze_log("data/orders_1.csv")
        orders = most_ordered_dish(order_list, customer)
        return orders

    def get_never_ordered_per_customer(self, customer):
        order_list = analyze_log("data/orders_1.csv")
        never_ordered = never_ordered_per_customer(order_list, customer)
        return never_ordered

    def get_days_never_visited_per_customer(self, customer):
        order_list = analyze_log("data/orders_1.csv")
        never_visited = days_never_visited_per_customer(
            order_list, customer
        )
        self.order_list.clear()
        return never_visited

    def get_busiest_day(self):
        the_busiest_day = busiest_day(self.order_list)
        return the_busiest_day

    def get_least_busy_day(self):
        the_least_busy_day = least_busy_day(self.order_list)
        return the_least_busy_day
