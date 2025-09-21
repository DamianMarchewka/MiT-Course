values = [60, 100, 120, 30, 600]
weights = [10, 20, 5, 20, 30]
total_weight = 50

def backpack_greedy(weights, valuees, total_weight):

    data = []
    for i in range(len(weights)):
        data.append({
            "v": valuees[i],
            "w": weights[i],
            "cost": float(valuees[i])/float(weights[i])
        })

    data = sorted(data, key=lambda x: x['cost'], reverse=True)
    print(f'DEBUG: {data}')

    remain = total_weight
    result = 0
    result_list = []
    i = 0

    while i < len(data):
        if (data[i]['w'] <= remain):
            remain -= data[i]['w']
            result += data[i]['v']
            result_list.append(data[i])
            print(f"DEBUG: adding {data[i]} - total values = {result} remaining space {remain}")
        i += 1
    return  result, result_list

print(backpack_greedy(weights, values, total_weight))