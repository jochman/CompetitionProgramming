import math
import sys

MY_LATITUDE, MY_LONGTITUDE = map(math.radians, map(float, input().split(",")))

r = float(input())


def harevine(lat, lon):
    lat2, lon2 = map(math.radians, [lat, lon])
    er = 6378.137
    return 2 * er * math.asin(
        math.sqrt(pow(math.sin((MY_LATITUDE - lat2) / 2), 2) + math.cos(MY_LATITUDE) * math.cos(lat2) * pow(
            math.sin((MY_LONGTITUDE - lon2) / 2), 2)))


input()  # dont need headers
input_data = sys.stdin.readlines()  # get all other data
res = {}
for line in input_data:
    timestamp, lat, long, phone = line.split(",")
    if phone not in res:
        if harevine(float(lat), float(long)) <= r:
            res[phone] = timestamp
    else:
        if res[phone] < timestamp:
            if harevine(float(lat), float(long)) <= r:
                res[phone] = timestamp
            else:
                res.pop(phone)
res = [phone.rstrip() for phone in res.keys()]
res.sort()
ans = ""
for phone in res:
    ans += f"{phone},"

print(ans.rstrip(','))
