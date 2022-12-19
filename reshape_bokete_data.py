import json

with open("C:\\Users\\yryo1\\Workspace\\Neural_Oh-giri_Generator_v1\\scraping_project\\bokete_scrape\\spiders\\test.json", encoding = "utf-8") as f:
    a = f.readlines()

tmp = []
for i, A in enumerate(a):
    if A == '[\n' or A == ']\n' or A == '][\n' or A == ']': continue
    A = A.strip("\n")
    if A[-1] == ",":
        r = json.loads(A[:-1])
    else:
        r = json.loads(A)
    tmp.append(r)

data = [tmp[0]]
previous_numver = tmp[0]["boke_number"]

for T in tmp:
    if T["boke_number"] != previous_numver:
        previous_numver = T["boke_number"]
        data.append(T)
    else:
        data[-1]["bokes"] += T["bokes"]

with open("boke_data.json", "w") as f:
    json.dump(data, f, indent = 4)