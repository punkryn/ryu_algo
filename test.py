from heapq import heappop, heappush
INF = int(1e9)

def dijkstra(start, end, n, traps, graph, is_trap, trap_idx):
    distance = [[INF] * (1 << len(traps)) for _ in range(n + 1)]
    distance[start][0] = 0
    q = [(0, start, 0)]
    while q:
        cur_cost, cur, state = heappop(q)

        if distance[cur][state] < cur_cost:
            continue

        for nxt, cost, edge_state in graph[cur]:
            nxt_cost = cost + cur_cost
            nxt_state = state
            if not is_trap[cur] and not is_trap[nxt]:
                if edge_state:
                    if nxt_cost < distance[nxt][nxt_state]:
                        distance[nxt][nxt_state] = nxt_cost
                        heappush(q, (nxt_cost, nxt, nxt_state))
            elif not is_trap[cur] and is_trap[nxt]:
                nxt_trap_state = trap_state(nxt, state, trap_idx)
                if edge_state != nxt_trap_state:
                    if nxt_trap_state:
                        nxt_state = off(nxt_state, nxt, trap_idx)
                    else:
                        nxt_state = on(nxt_state, nxt, trap_idx)
                    
                    if nxt_cost < distance[nxt][nxt_state]:
                        distance[nxt][nxt_state] = nxt_cost
                        heappush(q, (nxt_cost, nxt, nxt_state))
            elif is_trap[cur] and not is_trap[nxt]:
                cur_trap_state = trap_state(cur, state, trap_idx)
                if edge_state != cur_trap_state:
                    if nxt_cost < distance[nxt][nxt_state]:
                        distance[nxt][nxt_state] = nxt_cost
                        heappush(q, (nxt_cost, nxt, nxt_state))
            else:
                cur_trap_state = trap_state(cur, state, trap_idx)
                nxt_trap_state = trap_state(nxt, state, trap_idx)

                if cur_trap_state == nxt_trap_state and edge_state:
                    if nxt_trap_state:
                        nxt_state = off(nxt_state, nxt, trap_idx)
                    else:
                        nxt_state = on(nxt_state, nxt, trap_idx)
                    
                    if distance[nxt][nxt_state] > nxt_cost:
                        distance[nxt][nxt_state] = nxt_cost
                        heappush(q, (nxt_cost, nxt, nxt_state))
                elif cur_trap_state != nxt_trap_state and not edge_state:
                    if nxt_trap_state:
                        nxt_state = off(nxt_state, nxt, trap_idx)
                    else:
                        nxt_state = on(nxt_state, nxt, trap_idx)
                    
                    if distance[nxt][nxt_state] > nxt_cost:
                        distance[nxt][nxt_state] = nxt_cost
                        heappush(q, (nxt_cost, nxt, nxt_state))
    
    ans = INF
    for i in range((1 << len(traps))):
        ans = min(ans, distance[end][i])
    return ans
                    
def off(state, idx, trap_idx):
    return state ^ (1 << trap_idx[idx])

def on(state, idx, trap_idx):
    return state | (1 << trap_idx[idx])
            
def trap_state(nxt, state, trap_idx):
    if not (state & (1 << trap_idx[nxt])):
        return False
    return True
    
def make_trap(traps, n):
    is_trap = [False] * (n + 1)
    trap_idx = [0] * (n + 1)
    for i in range(len(traps)):
        t = traps[i]
        is_trap[t] = True
        trap_idx[t] = i
    return is_trap, trap_idx

def solution(n, start, end, roads, traps):
    answer = 0
    
    graph = [[] for _ in range(n + 1)]
    for road in roads:
        x, y, c = road
        graph[x].append((y, c, True))
        graph[y].append((x, c, False))
    
    is_trap, trap_idx = make_trap(traps, n)
    answer = dijkstra(start, end, n, traps, graph, is_trap, trap_idx)
    
    return answer

n = 4
start=1
end=4
roads=[[1, 2, 1], [3, 2, 1], [2, 4, 1]]
traps=[2, 3]
solution(n, start, end, roads, traps)