import sys

test_cases = int(input())
for test_case in range(test_cases):
    final_set = set()
    case_num = int(input())
    for x in range(case_num):
        in_data = input()
        x, y = map(int, in_data.split())
        markers = range(x, y + 1)
        final_set = final_set.union(set(markers))
    # print(final_set)
    sys.stdout.write(str(len(final_set))+'\n')
