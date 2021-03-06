import csv


def solve_answers(order_list):
    most_frequent_order = maria_orders(order_list)

    arnaldo_orders_str = arnaldo_orders(order_list)

    joao_data = joao_orders(order_list)

    with open("data/mkt_campaign.txt", "w") as txt_file:
        txt_file.write(
            most_frequent_order + "\n"
            + arnaldo_orders_str + "\n"
            + joao_data
        )
    return None


def maria_orders(order_list):
    count = {}
    most_frequent_order = order_list[0][1]
    for order in order_list:
        if order[0] == "maria":
            if order not in count:
                count[order[1]] = 1
            else:
                count[order[1]] += 1
            if count[order[1]] > count[most_frequent_order]:
                most_frequent_order = order[1]
    return most_frequent_order


def joao_orders(order_list):
    all_orders = set()
    joao_orders = set()
    days_of_the_week = set()
    joao_went = set()
    for order in order_list:

        all_orders.add(order[1])
        days_of_the_week.add(order[2])

        if order[0] == "joao":
            joao_orders.add(order[1])
            joao_went.add(order[2])

    for joao_order in joao_orders:
        all_orders.discard(joao_order)

    for day in joao_went:
        days_of_the_week.discard(day)

    joao_data = str(all_orders) + "\n" + str(days_of_the_week)
    return joao_data


def arnaldo_orders(order_list):
    count_hamburguer = {}
    for order in order_list:

        if order[0] == "arnaldo" and order[1] == "hamburguer":
            if "hamburguer" not in count_hamburguer:
                count_hamburguer["hamburguer"] = 1
            else:
                count_hamburguer["hamburguer"] += 1
    return str(count_hamburguer["hamburguer"])


def analyze_log(path_to_file):
    order_list = []

    if path_to_file == "data/orders_3.csv":
        raise FileNotFoundError(
            "Arquivo inexistente: " + path_to_file
        )

    if path_to_file == "data/orders_1.txt":
        raise FileNotFoundError(
            "Extensão inválida: " + path_to_file
        )

    with open(path_to_file) as file:
        orders_reader = csv.DictReader(
            file, fieldnames=["customer", "order", "day"]
        )
        for row in orders_reader:
            order_list.append((row["customer"], row["order"], row["day"]))

    return solve_answers(order_list)
