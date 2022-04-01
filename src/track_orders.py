class TrackOrders:
    # aqui deve expor a quantidade de estoque
    order_list = []
    def __len__(self):
        self.data = self.order_list
        return len(self.data)

    def add_new_order(self, customer, order, day):
       self.order_list.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        pass

    def get_never_ordered_per_customer(self, customer):
        pass

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
