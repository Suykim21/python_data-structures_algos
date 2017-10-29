def create(str_one):
    compress = {}
    counter = 1
    current = str_one[0]
    results = []
    for i in str_one:
        if current == i:
            counter += 1
        else:
            compress[current] = counter
            current = i
            counter = 1
    for k,v in compress.items():
        results.append(k + str(v))
    print("".join(results))
    return "".join(results)

create('aaabbcccddddd')