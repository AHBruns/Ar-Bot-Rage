import WebCalls.phone as phone
import time

# start time check (used for later references)
#    - only checked once
start_time = time.time()
print('\tstart time: ' + str(start_time))
print('')

completed_event_loop_count = 0
while True:
    # base currencies check
    #    - first time through
    #    - every 10 loops
    #    - every 150 seconds
    if completed_event_loop_count == 0 or completed_event_loop_count % 10 == 0 or time.time() - last_check_time_base_currencies > 150:
        base_currencies = phone.get_base_currency_ids()
        last_check_time_base_currencies = time.time()
        print('\tbase currencies checked for activity and new additions')
        print('\t' + str(base_currencies))
        print('\ttime: ' + str(last_check_time_base_currencies))
        print('')

    completed_event_loop_count += 1

