# def create(str_one):
#     compress = {}
#     counter = 1
#     current = str_one[0]
#     results = []
#     for i in str_one:
#         if current == i:
#             counter += 1
#         else:
#             compress[current] = counter
#             current = i
#             counter = 1
#     for k,v in compress.items():
#         results.append(k + str(v))
#     print("".join(results))
#     return "".join(results)

def compress(string):
    char_set = {key:0 for key in string}
    for char in string:
        char_set[char] += 1
    compressed = ''.join('{}{}'.format(key, val) for key, val in char_set.items())
    print(compressed)
    return compressed


compress('aabbbcccccddd')