import sys
from bisect import bisect_right

# read input
n, m = sys.stdin.readline().strip().split()
n, m = int(n), int(m)
persons, candidates = [], []
for _ in range(n):
    x, y = sys.stdin.readline().strip().split()
    persons.append((int(x), int(y)))
for _ in range(m):
    x, y = sys.stdin.readline().strip().split()
    candidates.append((int(x), int(y)))
pos_xs = sorted([item[0] for item in persons])  # person positions x
pos_ys = sorted([item[1] for item in persons])  # person positions y

cost_xs = [0 for _ in range(n)]
cost_ys = [0 for _ in range(n)]
for each in pos_xs:
    cost_xs[0] += each - pos_xs[0]
for each in pos_ys:
    cost_ys[0] += each - pos_ys[0]
for idx in range(1, n):
    cost_xs[idx] = cost_xs[idx - 1] - (n - 2 * idx) * (pos_xs[idx] - pos_xs[idx - 1])
for idx in range(1, n):
    cost_ys[idx] = cost_ys[idx - 1] + (2 * idx - n) * (pos_ys[idx] - pos_ys[idx - 1])

def cal_cost(pos, sorted_positions, costs):
    assert len(sorted_positions) == len(costs)
    left_num = bisect_right(sorted_positions, pos)
    right_num = len(sorted_positions) - left_num
    if left_num == 0:
        return costs[0] + (sorted_positions[0] - pos) * len(sorted_positions)
    else:
        dist = pos - sorted_positions[left_num - 1]
        return costs[left_num - 1] + dist * (left_num - right_num)

result = None
cost = None
for x, y in candidates:
    x_cost = cal_cost(x, pos_xs, cost_xs)
    y_cost = cal_cost(y, pos_ys, cost_ys)
    if cost is None or x_cost + y_cost < cost:
        result = (x, y)
        cost = x_cost + y_cost
sys.stdout.write(f"{result[0]} {result[1]}\n")
sys.stdout.flush()