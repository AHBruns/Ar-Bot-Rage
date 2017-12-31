

# markets come in with the following in this order
#    - market id
#    - asset code
#    - base currency code
#    - activity
#    - bid price
#    - ask price

# base currencies come in with the following in this order
#    - currency id
#    - base currency code


def group_markets(markets, base_currencies):
    sorted_markets = []
    for base_currency in base_currencies:
        temp = []
        for market in markets:
            if base_currency[1] == market[2]:
                temp.append(market)
        sorted_markets.append(temp)
    return sorted_markets


def connect(grouped_markets):
    i = 0
    for group in grouped_markets:  # finds which group is btc based because I only trade BTC -> BTC
        if group[0][2] == "BTC":
            btc_index = i
        i += 1
    btc_markets = grouped_markets[btc_index]
    grouped_markets.pop(btc_index)
    other_markets = []
    for market_group  in grouped_markets:
        other_markets += market_group
    paths = []
    for market1 in btc_markets:
        waypoint_1 = [market1]  # buy
        # print(waypoint_1)
        for market2 in other_markets:
            if market2[1] == waypoint_1[0][1]:  # buy -> sell
                waypoint_2 = [waypoint_1, market2]
                # print('-----' + str(waypoint_2))
                for market3 in btc_markets:
                    if market3[1] == waypoint_2[1][2]:
                        waypoint_3 = [waypoint_2, market3]  # buy -> sell -> sell
                        # print('----------' + str(waypoint_3))
                        paths.append(waypoint_3)
            elif market2[2] == waypoint_1[0][1]:  # buy -> buy
                waypoint_2 = [waypoint_1, market2]
                # print('-----' + str(waypoint_2))
                for market3 in btc_markets:
                    if market3[1] == waypoint_2[1][1]:
                        waypoint_3 = [waypoint_2, market3]  # buy -> buy -> sell
                        # print('----------' + str(waypoint_3))
                        paths.append(waypoint_3)
    return paths


def clean_paths(listed_paths):
    cleaned_paths = []
    for listed_path in listed_paths:
        new_path = [listed_path[0][0][0], listed_path[0][1], listed_path[1]]
        cleaned_paths.append(new_path)
    return cleaned_paths


def sort_paths(paths):
    bss_paths = []
    bbs_paths = []
    for path in paths:
        if path[0][1] == path[1][1]:  # Buy -> Sell -> Sell
            bss_paths.append(path)
        else:  # Buy -> Buy -> Sell
            bbs_paths.append(path)
    return [bss_paths,bbs_paths]


def check_for_empties(paths):
    non_empty_bss_paths = []
    non_empty_bbs_paths = []
    for bss_path in paths[0]:
        if not (bss_path[0][5] =='0.00000000') and not (bss_path[1][4] == '0.00000000') and not (bss_path[2][4] == '0.00000000'):
            non_empty_bss_paths.append(bss_path)
    for bbs_path in paths[1]:
        if not (bbs_path[0][5] =='0.00000000') and not (bbs_path[1][5] == '0.00000000') and not (bbs_path[2][4] == '0.00000000'):
            non_empty_bbs_paths.append(bss_path)
    return [non_empty_bss_paths, non_empty_bbs_paths]

def make_paths(markets, base_currencies):
    grouped_markets = group_markets(markets, base_currencies)
    possible_paths = connect(grouped_markets)
    possible_paths = clean_paths(possible_paths)
    sorted_possible_paths = sort_paths(possible_paths)
    sorted_paths = check_for_empties(sorted_possible_paths)
    return sorted_paths

