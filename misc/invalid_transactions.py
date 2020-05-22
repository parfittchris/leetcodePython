def invalidTransactions(transactions):
    invalids = [];
    people = {}
    selected = {}
    i = 0 


    
    while (i < len(transactions)):
        current = transactions[i].split(',')

        name = current[0]
        time = current[1]
        amt = current[2]
        loc = current[3]

        if int(amt) >= int(1000):
            selected[i] = True
            invalids.append(transactions[i])

        if not name in people:
            people[name] = {}

        people[name][time] = {'idx':i, 'loc':loc}

        i += 1

    for person in people:
        all_times = sorted(list(people[person].keys()))
        j = 0

        while j < len(all_times) - 1:
            current_range = [int(all_times[j]) - 60, int(all_times[j]) + 60]
            k = j + 1
            while k < len(all_times):
                if int(all_times[k]) > current_range[0] and int(all_times[k]) < current_range[0]:
                    pass
                k += 1
            
            
            
            j +=  1

    return invalids

arr = ["alice,20,800,mtv", "alice,50,100,beijing"]
print(invalidTransactions(arr))
