import params
import re


with open(params.FILE_PATH, "r") as f:
    a = [x.split() for x in f if re.search(r'4\d\d', x.split()[8])]
    s = sorted([(i[6], i[8], int(i[9]), i[0]) for i in a], key=lambda x: x[2], reverse=True)[:5]

with open(params.FILE_RESULT_PATH, 'w') as f:
    f.write("Top 5 largest requests in size that ended with a client (4XX) error:\n")
    for x in s:
        f.write(f'{x[0]} {x[1]} {x[2]} {x[3]}\n')
