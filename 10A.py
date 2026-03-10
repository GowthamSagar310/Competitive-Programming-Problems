n, p1, p2, p3, t1, t2 = map(int, input().split())
prev_end = -1
total = 0
for _ in range(n):
    l, r = map(int, input().split())
    total += (r-l) * p1
    if prev_end != -1:

        total_interval = l-prev_end
        
        first_phase = min(t1, total_interval)
        total += first_phase * p1

        second_phase = min(t2, total_interval-first_phase)
        total += second_phase * p2

        third_phase = max(0, total_interval-first_phase-second_phase)
        total += third_phase * p3

    prev_end = r
print(total)
