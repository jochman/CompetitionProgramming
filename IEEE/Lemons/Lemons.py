from math import ceil, log

NUMBER_OF_PUMPS, TRAVEL_TIME, NUMBER_OF_MINS_TO_CHECK = (int(s) for s in input().split())
total_check_time = int((NUMBER_OF_MINS_TO_CHECK * ceil(log(NUMBER_OF_PUMPS, 2))))
print(total_check_time + ((NUMBER_OF_PUMPS - 1) * TRAVEL_TIME))
