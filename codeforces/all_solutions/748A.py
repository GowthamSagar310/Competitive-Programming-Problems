c, r, p = map(int, input().split())

seats_per_lane = r * 2

# lane_number = ((p-1) // seats_per_lane) + 1
# row_number = ((p-seats_per_lane * (lane_number-1)-1) // 2) + 1
# side = "R" if p % 2 == 0 else "L"
# print(lane_number, row_number, side)


lane_number = ((p-1) // seats_per_lane) + 1
pos = (p-1) % seats_per_lane # which row 
desk = (pos) // 2 + 1
side = "L" if pos % 2 == 0 else "R"
print(lane_number, desk, side)