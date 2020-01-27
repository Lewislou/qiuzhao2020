import os
from datetime import date, timedelta
from collections import Counter

leetcode_id = ["biss", "biss-test"]

name_dict = Counter()

days_to_subtract = 2

today = date.today()
for i in range(days_to_subtract + 1):
    before_day = today - timedelta(days=i)
    before_day_dir = str(before_day).replace("-", "_")
    try:
        for file in os.listdir(before_day_dir):
            name = file.split("_")[0]
            name_dict[name] += 1
        print("####log####")
        print("date: ", before_day)
        print(name_dict)
    except Exception:
        print("Exception!!! date: ", before_day, " isn't in the github repository")

print()
print("####Name count####")
print("name count: ", name_dict)


print()
print("####Final result(people who should be out)####")
for name in leetcode_id:
    if name_dict[name] == 0:
        print(name)