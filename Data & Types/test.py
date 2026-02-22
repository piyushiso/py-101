temps = {
    'K': [10, 20, 30],
    'H': [20, 30, 40]
}

for k, v in temps.items():
    av = sum(v)/len(v)
    print(k, av)