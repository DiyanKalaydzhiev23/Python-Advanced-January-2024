from collections import deque

pumps_data = deque([[int(x) for x in input().split()] for _ in range(int(input()))])  # [[1, 5], [10, 3], [1, 3]]

pumps_data_copy = pumps_data.copy()
gas_in_tank = 0
index = 0

while pumps_data_copy:
    petrol, distance = pumps_data_copy.popleft()

    gas_in_tank += petrol

    if gas_in_tank >= distance:
        gas_in_tank -= distance
    else:
        pumps_data.rotate(-1)
        pumps_data_copy = pumps_data.copy()
        index += 1
        gas_in_tank = 0

print(index)
