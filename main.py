import WebCalls.phone as phone
import Algorithms.pather as pather
import Algorithms.evaluations as eval
import HandOfGod.hand as hand
import time

# start time check (used for later references)
#    - only checked once
start_time = time.time()
print('\tstart time: ' + str(start_time))
print('')
# print("\tsetting up trade scene. please don't touch anything. please.")
# print("\ttime: " + str(time.time()))
# print('')
# hand.setup_scene_1()

completed_event_loop_count = 0
while True:  # production loop
# while completed_event_loop_count == 0:  # single loop for testing
    # base currencies check
    #    - first time through
    #    - every 150 seconds max
    if completed_event_loop_count == 0 or time.time() - last_check_time_base_currencies > 150:
        base_currencies = phone.get_base_currency_ids()
        last_check_time_base_currencies = time.time()
        print('\tbase currencies checked for activity and new additions')
        print('\ttime: ' + str(last_check_time_base_currencies))
        print('')
    # markets check
    #    - first time through
    #    - every 5 seconds max
    if completed_event_loop_count == 0 or time.time() - last_check_time_markets > 5:
        markets = phone.get_market_infos()
        last_check_time_markets = time.time()
        print('\tmarkets checked for new prices, activity, and new additions')
        print('\ttime: ' + str(last_check_time_markets))
        print('')
    # get paths
    paths = pather.make_paths(markets, base_currencies)
    # eval BSS paths
    print('\tevaluating buy -> sell -> sell paths for profitability')
    print('\ttime: ' + str(time.time()))
    print('')
    for bss_path in paths[0]:
        eval_results = eval.bss_light_eval(bss_path)
        if eval_results[0] > 0.01:
            print('Found possible trade! ' + str(bss_path))
            print('-> ' + str(eval_results[0] * 100) + '%')
            print('')
            print('\tevaluating order books to determine if path is actionable')
            print('\ttime: ' + str(time.time()))
            print('')
            book1 = phone.get_ask_book([bss_path[0][0]])
            book2 = phone.get_bid_book([bss_path[1][0]])
            book3 = phone.get_bid_book([bss_path[2][0]])
            deep_eval_results = eval.bss_deep_eval(bss_path, book1, book2, book3)
            first_time = True
            while deep_eval_results[0][0] > 0.01:
                print('Trade is actionable! ' + str(bss_path))
                print('-> ' + str(deep_eval_results[0][0] * 100) + '%')
                print('-> https://www.coinexchange.io/market/' + bss_path[0][1] + '/' + bss_path[0][2] + ' ' + str(deep_eval_results[1][0]))
                print('-> https://www.coinexchange.io/market/' + bss_path[1][1] + '/' + bss_path[1][2] + ' ' + str(deep_eval_results[1][1]))
                print('-> https://www.coinexchange.io/market/' + bss_path[2][1] + '/' + bss_path[2][2] + ' ' + str(deep_eval_results[1][2]))
                print('')
                # if first_time:
                #     hand.url_1_input("https://www.coinexchange.io/market/" + bss_path[0][1] + '/' + bss_path[0][2])
                #     hand.url_2_input("https://www.coinexchange.io/market/" + bss_path[1][1] + '/' + bss_path[1][2])
                #     hand.url_3_input("https://www.coinexchange.io/market/" + bss_path[2][1] + '/' + bss_path[2][2])
                    # choice = input('Should I setup the trades? "y" or "n" ')
                    # if choice == "y":
                    #     hand.url_1_input("https://www.coinexchange.io/market/" + bss_path[0][1] + '/' + bss_path[0][2])
                    #     hand.url_2_input("https://www.coinexchange.io/market/" + bss_path[1][1] + '/' + bss_path[1][2])
                    #     hand.url_3_input("https://www.coinexchange.io/market/" + bss_path[2][1] + '/' + bss_path[2][2])
                first_time = False
                book1 = phone.get_ask_book([bss_path[0][0]])
                book2 = phone.get_bid_book([bss_path[1][0]])
                book3 = phone.get_bid_book([bss_path[2][0]])
                deep_eval_results = eval.bss_deep_eval(bss_path, book1, book2, book3)
    # eval BBS paths
    print('\tevaluating buy -> buy -> sell paths for profitability')
    print('\ttime: ' + str(time.time()))
    print('')
    for bbs_path in paths[1]:
        eval_results = eval.bbs_light_eval(bbs_path)
        if eval_results[0] > 0.01:
            print('Found possible trade! ' + str(bbs_path))
            print('-> ' + str(eval_results[0] * 100) + '%')
            print('')
            print('\tevaluating order books to determine if path is actionable')
            print('\ttime: ' + str(time.time()))
            print('')
            book1 = phone.get_ask_book([bbs_path[0][0]])
            book2 = phone.get_ask_book([bbs_path[1][0]])
            book3 = phone.get_bid_book([bbs_path[2][0]])
            deep_eval_results = eval.bbs_deep_eval(bbs_path, book1, book2, book3)
            first_time = True
            while deep_eval_results[0][0] > 0.01:
                print('Trade is actionable! ' + str(bbs_path))
                print('-> ' + str(deep_eval_results[0][0] * 100) + '%')
                print('-> https://www.coinexchange.io/market/' + bbs_path[0][1] + '/' + bbs_path[0][2] + ' ' + str(deep_eval_results[1][0]) )
                print('-> https://www.coinexchange.io/market/' + bbs_path[1][1] + '/' + bbs_path[1][2] + ' ' + str(deep_eval_results[1][1]))
                print('-> https://www.coinexchange.io/market/' + bbs_path[2][1] + '/' + bbs_path[2][2] + ' ' + str(deep_eval_results[1][2]))
                print('')
                # if first_time:
                #     hand.url_1_input("https://www.coinexchange.io/market/" + bbs_path[0][1] + '/' + bbs_path[0][2])
                #     hand.url_2_input("https://www.coinexchange.io/market/" + bbs_path[1][1] + '/' + bbs_path[1][2])
                #     hand.url_3_input("https://www.coinexchange.io/market/" + bbs_path[2][1] + '/' + bbs_path[2][2])
                    # choice = input('Should I setup the trades? "y" or "n" ')
                    # if choice == "y":
                    #     hand.url_1_input("https://www.coinexchange.io/market/" + bbs_path[0][1] + '/' + bbs_path[0][2])
                    #     hand.url_2_input("https://www.coinexchange.io/market/" + bbs_path[1][1] + '/' + bbs_path[1][2])
                    #     hand.url_3_input("https://www.coinexchange.io/market/" + bbs_path[2][1] + '/' + bbs_path[2][2])
                first_time = False
                book1 = phone.get_ask_book([bbs_path[0][0]])
                book2 = phone.get_ask_book([bbs_path[1][0]])
                book3 = phone.get_bid_book([bbs_path[2][0]])
                deep_eval_results = eval.bbs_deep_eval(bbs_path, book1, book2, book3)
    completed_event_loop_count += 1

