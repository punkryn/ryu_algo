def solution(n, plans, clients):
    answer = []
    bugaservice = [0 for _ in range(n+1)]
    payments = [0]
    for idx in range(len(plans)):
        pay,*buga = map(int,plans[idx].split())
        payments.append(pay)
        for b in buga:
            bugaservice[b] = idx+1
    max_payments = payments[-1] 
    INF = float('inf')
    for idx in range(len(clients)):
        use,*buga = map(int,clients[idx].split())
        buga_max = 0
        use_min = 0
        for b in buga:
            if bugaservice[b]:
                buga_max = max(buga_max,bugaservice[b])
            else:
                buga_max = INF
                break
        if use > max_payments:
            use_min = INF
        else:
            left = 0
            right = len(payments)
            while left+1 < right:
                mid = (left+right)//2
                if payments[mid] >= use:
                    right = mid
                else:
                    left = mid
            use_min = right
        if use_min == INF or buga_max == INF:
            answer.append(0)
        else:
            answer.append(max(use_min,buga_max))
    return answer