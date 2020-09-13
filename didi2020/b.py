import sys

def dijkstra(n, edges, start):
    start = start - 1
    weight = [[100000000 for _ in range(n)] for _ in range(n)]
    for idx in range(n):
        weight[idx][idx] = 0
    for x, y, value in edges:
        weight[x-1][y-1] = value
        weight[y-1][x-1] = value

    short_path = [-1] * n
    visited = [False] * n

    short_path[start] = 0
    visited[start] = True

    for count in range(1, n):
        k = -1
        dmin = 100000000000
        for idx in range(n):
            if not visited[idx] and weight[start][idx] < dmin:
                dmin = weight[start][idx]
                k = idx
        short_path[k] = dmin
        visited[k] = True

        for idx in range(n):
            if not visited[idx] and weight[start][k] + weight[k][idx] < weight[start][idx]:
                weight[start][idx] = weight[start][k] + weight[k][idx]
    return short_path

def get_inputs():
    n, m = sys.stdin.readline().strip().split()
    n, m = int(n), int(m)
    edges = []
    for _ in range(m):
        u, v, time = sys.stdin.readline().strip().split()
        u, v, time = int(u), int(v), int(time)
        edges.append((u, v, time))
    s, e, start = sys.stdin.readline().strip().split()
    s, e = int(s), int(e)
    return n, m, edges, s, e, start

def print_outputs(start_time, add_hours):
    tmp, hour = start_time.split("/")
    month, day = tmp.split(".")
    month, day, hour = int(month), int(day), int(hour)
    new_hour = (hour + add_hours) % 24
    add_days = (hour + add_hours) // 24
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    assert sum(month_days) == 366
    new_day = add_days + day
    new_month = month
    while new_day > month_days[new_month]:
        new_day -= month_days[new_month]
        new_month += 1
    sys.stdout.write(f"{new_month}.{new_day}/{new_hour}\n")
    sys.stdout.flush()

def main():
    n, m, edges, s, e, start = get_inputs()
    short_distance = dijkstra(n, edges, s)
    minist_time = short_distance[e - 1]  # 到巴黎的最短时间（小时）
    print_outputs(start, minist_time)

main()