fee_percentage = 0.0015


def bss_computation(price_1, price_2, price_3):
    net_total_1 = 1
    total_1 = net_total_1 / (1 + fee_percentage)
    amount_1 = total_1 / price_1
    amount_2 = amount_1
    total_2 = amount_2 * price_2
    net_total_2 = total_2 * (1 - fee_percentage)
    amount_3 = net_total_2
    total_3 = amount_3 * price_3
    net_total_3 = total_3 * (1 - fee_percentage)
    percent_change = (net_total_3 / net_total_1) - 1
    return [percent_change]


def bss_light_eval(path):
    price_1 = float(path[0][5])
    price_2 = float(path[1][4])
    price_3 = float(path[2][4])
    return bss_computation(price_1, price_2, price_3)


def weighted_avg(to_be_weighted):
    tot_value = 0.0
    for item in to_be_weighted:
        tot_value += item[1]
    tot_price = 0.0
    for item in to_be_weighted:
        item_weight = item[1] / tot_value
        weighted_item_price = item[0] * item_weight
        tot_price += weighted_item_price
    return tot_price


def book_weighting(base_currency_code, book, min_tot_quantity):
    min_orders = {'BTC': 0.0001, 'DOGE': 0.0001, 'ETH': 0.0001, 'ETC': 0.0001, 'LTC': 0.0001}
    active_orders = []
    min_tot_base_value = min_orders[base_currency_code]
    cur_tot_base_value = 0
    cur_tot_quantity = 0
    cur_depth = 0
    quantity_first_flag = False
    for order in book:
        cur_depth += 1
        order_price = float(order[0])
        order_quantity = float(order[1])
        order_base_value = order_price * order_quantity
        # print(str(cur_tot_base_value) + ' ' + str(cur_tot_quantity))
        if ((cur_tot_base_value + order_base_value) >= min_tot_base_value) and ((cur_tot_quantity + order_quantity) >= min_tot_quantity):
            if quantity_first_flag:
                order_base_value = min_tot_base_value - cur_tot_base_value
            elif min_tot_quantity != 0:
                order_base_value = (min_tot_quantity - cur_tot_quantity) * order_price
            else:
                order_base_value = min_tot_base_value - cur_tot_base_value
            active_orders.append([order_price, order_base_value])
            # print('last active order! ' + str([order_price, order_base_value]))
            break
        if ((cur_tot_quantity + order_quantity) >= min_tot_quantity):
            quantity_first_flag =  True
        cur_tot_base_value += order_base_value
        cur_tot_quantity += order_quantity
        active_orders.append([order_price, order_base_value])
    # print(active_orders)
    weighted_price = weighted_avg(active_orders)
    # print(weighted_price)
    return weighted_price


def variable_min_base_value_weighting(base_currency_code, book, min_tot_base_value):
    min_orders = {'BTC': 0.0001, 'DOGE': 0.0001, 'ETH': 0.0001, 'ETC': 0.0001, 'LTC': 0.0001}
    if min_tot_base_value < 0.0001:
        min_tot_base_value = min_orders[base_currency_code]
    active_orders = []
    cur_tot_base_value = 0
    cur_tot_quantity = 0
    cur_depth = 0
    for order in book:
        cur_depth += 1
        order_price = float(order[0])
        order_quantity = float(order[1])
        order_base_value = order_price * order_quantity
        if cur_tot_base_value + order_base_value >= min_tot_base_value:
            order_base_value = min_tot_base_value - cur_tot_base_value
            active_orders.append([order_price, order_base_value])
            break
        cur_tot_base_value += order_base_value
        cur_tot_quantity += order_quantity
        active_orders.append([order_price, order_base_value])
    weighted_price = weighted_avg(active_orders)
    return weighted_price


def bss_deep_eval(path, book1, book2, book3):
    weighted_prices = []
    weighted_prices.append(book_weighting(path[0][2], book1, 0))
    # print('end-1')
    book2_min_quantity = (.0001 / (1 + fee_percentage)) / weighted_prices[0]
    weighted_prices.append(book_weighting(path[1][2], book2, book2_min_quantity))
    # print('end-2')
    book3_min_quantity = (weighted_prices[1] * book2_min_quantity) * (1 - fee_percentage)
    weighted_prices.append(book_weighting(path[2][2], book3, book3_min_quantity))
    min_quantities = [0, book2_min_quantity, book3_min_quantity]
    percent_change = bss_computation(weighted_prices[0], weighted_prices[1], weighted_prices[2])
    return [percent_change, weighted_prices]


def bbs_computation(price_1, price_2, price_3):
    net_total_1 = 1
    total_1 = 1 / (1 + fee_percentage)
    amount_1 = total_1 / price_1
    net_total_2 = amount_1
    total_2 = net_total_2 / (1 + fee_percentage)
    amount_2 = total_2 / price_2
    amount_3 = amount_2
    total_3 = amount_3 * price_3
    net_total_3 = total_3 * (1 - fee_percentage)
    percent_change = (net_total_3 / net_total_1) - 1
    return [percent_change]


def bbs_light_eval(path):
    price_1 = float(path[0][5])
    price_2 = float(path[1][5])
    price_3 = float(path[2][4])
    return bbs_computation(price_1, price_2, price_3)


def bbs_deep_eval(path, book1, book2, book3):
    weighted_prices = []
    weighted_prices.append(book_weighting(path[0][2], book1, 0.0001))
    book2_min_tot_base_value = (.0001 / (1 + fee_percentage)) / weighted_prices[0]
    weighted_prices.append(variable_min_base_value_weighting(path[1][2], book2, book2_min_tot_base_value))
    book3_min_quantity = book2_min_tot_base_value / weighted_prices[1]
    weighted_prices.append(book_weighting(path[2][2], book3, book3_min_quantity))
    percent_change = bbs_computation(weighted_prices[0], weighted_prices[1], weighted_prices[2])
    return [percent_change, weighted_prices]






