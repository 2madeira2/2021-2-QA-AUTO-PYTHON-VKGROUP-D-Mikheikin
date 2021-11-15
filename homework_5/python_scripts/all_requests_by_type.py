import params

types = dict()

with open(params.FILE_PATH, "r") as f:
    for line in f:
        r_type = line.split()[5][1:]
        if r_type in types:
            types[r_type] += 1
        else:
            types[r_type] = 1

with open(params.FILE_RESULT_PATH, 'w') as f:
    f.write("Total number of requests by type:\n")
    for k in types:
        f.write(f"{k} {str(types[k])}\n")
