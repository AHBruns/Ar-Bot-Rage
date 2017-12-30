import WebCalls.spectacles as spectacles
import requests
import sys

parsed_phonebook = spectacles.parse()
# for item in parsed_phonebook:
#     print(item)


def safe_request(url):
    success = False
    tries = 0
    while not success and tries < 10:
        try:
            tries += 1
            resp = requests.get(url)
            json_resp = resp.json()
            success = True
        except:
            pass
    if tries >= 10:
        return ['failed request']
    else:
        return json_resp


def response_evaluation(resp, path):
    i = 0
    for path_choice in path:
        if path_choice in parsed_phonebook[0]:
            if 'loop' == parsed_phonebook[0][path_choice]:
                return iterate(resp, path[-i:][0])
        else:
            resp = resp[path_choice]
        i += 1


def iterate(resp, path):
    results = []
    for resp_item in resp:
        resp_item_results = []
        for path_choice in path:
            if type(path_choice) == list:
                resp_item_results.append(response_evaluation(resp_item, path_choice))
            else:
                resp_item_results.append(resp_item[path_choice])
        results.append(resp_item_results)
    return results


def get_market_ids():
    base_url = parsed_phonebook[5]['base-url']
    function_name = parsed_phonebook[3]["all-market-ids"][0]
    result_parse_path = parsed_phonebook[3]["all-market-ids"][1]
    function_string = parsed_phonebook[1][function_name][0]
    arg_num = parsed_phonebook[1][function_name][1]
    args = parsed_phonebook[1][function_name][2]
    resp = ['arg required']
    if arg_num == 0:
        call_url = base_url + function_string
        resp = safe_request(call_url)
    if type(resp) == list:
        if resp[0] == 'arg required':
            sys.exit('unknown args required for api call')
        elif resp[0] == 'failed request':
            sys.exit('api call failed to return a usable response')
    return response_evaluation(resp, result_parse_path)


def get_active_market_ids():
    market_ids = get_market_ids()
    active_markets = []
    for market in market_ids:
        if market[3] == True:
            active_markets.append(market)
    return active_markets


def get_currency_ids():
    base_url = parsed_phonebook[5]['base-url']
    function_name = parsed_phonebook[3]["all-currency-ids"][0]
    result_parse_path = parsed_phonebook[3]["all-currency-ids"][1]
    function_string = parsed_phonebook[1][function_name][0]
    arg_num = parsed_phonebook[1][function_name][1]
    args = parsed_phonebook[1][function_name][2]
    resp = ['arg required']
    if arg_num == 0:
        call_url = base_url + function_string
        resp = safe_request(call_url)
    if type(resp) == list:
        if resp[0] == 'arg required':
            sys.exit('unknown args required for api call')
        elif resp[0] == 'failed request':
            sys.exit('api call failed to return a usable response')
    return response_evaluation(resp, result_parse_path)


def get_base_currency_ids():
    markets = get_active_market_ids()
    currencies = get_currency_ids()
    base_currencies = []
    for market in markets:
        for currency in currencies:
            if currency[1] == market[2] and currency not in base_currencies:
                base_currencies.append(currency)
    return base_currencies


def get_prices():
    base_url = parsed_phonebook[5]['base-url']
    function_name = parsed_phonebook[3]["all-market-prices"][0]
    result_parse_path = parsed_phonebook[3]["all-market-prices"][1]
    function_string = parsed_phonebook[1][function_name][0]
    arg_num = parsed_phonebook[1][function_name][1]
    args = parsed_phonebook[1][function_name][2]
    resp = ['arg required']
    if arg_num == 0:
        call_url = base_url + function_string
        resp = safe_request(call_url)
    if type(resp) == list:
        if resp[0] == 'arg required':
            sys.exit('unknown args required for api call')
        elif resp[0] == 'failed request':
            sys.exit('api call failed to return a usable response')
    return response_evaluation(resp, result_parse_path)


def get_market_infos():
    prices = get_prices()
    markets = get_active_market_ids()
    market_infos = []
    for price in prices:
        for market in markets:
            if market[0] == price[0]:
                datapoint = market
                datapoint.append(price[1])
                datapoint.append(price[2])
                market_infos.append(datapoint)
                break
    return market_infos

# print(get_market_ids())
# print('-----------------------------------------------------------------------------------')
# print(get_currency_ids())
# print('-----------------------------------------------------------------------------------')
# print(get_base_currency_ids())
# print('-----------------------------------------------------------------------------------')
# print(get_prices())
# print('-----------------------------------------------------------------------------------')
# print(get_market_infos())