import params

users = dict()

with open(params.FILE_PATH, "r") as f:
    for line in f:
        l = line.split()
        if "5" in l[8]:
            if l[0] in users:
                users[l[0]] += 1
            else:
                users[l[0]] = 1

users_sorted = {k: users[k] for k in sorted(users, key=users.get, reverse=True)}

with open(params.FILE_RESULT_PATH, 'w') as f:
    f.write("Top 5 users by the number of requests that ended with a server (5XX) error:\n")
    count = 0
    for key in users_sorted:
        if count < 5:
            f.write(f"User: {key}, number of requests: {str(users_sorted[key])}\n")
        count += 1
