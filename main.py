import WebCalls.phone as phone
import Algorithms.pather as pather
import time

# start time check (used for later references)
#    - only checked once
start_time = time.time()
print('\tstart time: ' + str(start_time))
print('')

completed_event_loop_count = 0
# while True:  # production loop
while completed_event_loop_count == 0:  # single loop for testing
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
    paths = pather.make_paths(markets,base_currencies)


    completed_event_loop_count += 1

