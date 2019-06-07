import re
import sys

test_cases = int(input())
for test_case in range(test_cases):
    search_catalog = dict()
    search_query_no = int(input())
    for x in range(search_query_no):
        in_data = input().strip()
        if not re.search("top [1-9]*", in_data):
            if in_data in search_catalog.keys():
                search_catalog[in_data] += 1
            else:
                search_catalog[in_data] = 1
        else:
            searches_to_show = in_data.split()[1]
            # to_display = sorted(search_catalog.items(), key=lambda x: (x[1],x[0]), reverse=True)
            to_display = sorted(search_catalog.items(), key=lambda x: (-x[1], x[0]))
            
            for i in to_display[:int(searches_to_show)]:
                print(i[0], end=" ")
            print(end="\n")
