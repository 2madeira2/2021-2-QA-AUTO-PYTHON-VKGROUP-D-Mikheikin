import params

requests = dict()
with open(params.FILE_PATH, "r") as f:
    for line in f:
        request = line.split()[6]
        if request in requests:
            requests[request] += 1
        else:
            requests[request] = 1

requests_sorted = {k: requests[k] for k in sorted(requests, key=requests.get, reverse=True)}

with open(params.FILE_RESULT_PATH, "w") as f:
    f.write("Top 10 most frequent requests:\n")
    count = 0
    for key in requests_sorted:
        if count < 10:
            f.write(f"Requested URL: {key}, number of requests: {str(requests_sorted[key])}\n")
        count += 1
