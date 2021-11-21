import params

with open(params.FILE_PATH, "r") as f:
    n = len(f.readlines())

with open(params.FILE_RESULT_PATH, 'w') as f:
    f.write(f"Total number of requests in {params.FILE_PATH}:\n{n}")
