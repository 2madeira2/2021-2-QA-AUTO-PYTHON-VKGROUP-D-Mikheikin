import os
from collections import Counter
from fnmatch import fnmatch

FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'access.log'))


def count_requests():
    with open(FILE_PATH, "r") as f:
        n = len(f.readlines())
    return n



def count_request_types():
    types = dict()
    with open(FILE_PATH, "r") as f:
        for line in f:
            r_type = line.split()[5][1:]
            if r_type in types:
                types[r_type] += 1
            else:
                types[r_type] = 1
    return types


def most_frequent_requests():
    with open(FILE_PATH, 'r') as log:
        url_column = [req.split()[6] for req in log.readlines()]
        freq_requests = Counter(url_column).most_common(10)
    return freq_requests


def largest_4xx_requests():
    with open(FILE_PATH, 'r') as log:
        url_code_size_ip_columns = [(req.split()[6], int(req.split()[8]), int(req.split()[9]), req.split()[0])
                                    for req in log.readlines() if fnmatch(req.split()[8], '4??')]
        url_code_size_ip_columns.sort(key=lambda req: req[2], reverse=True)
    return url_code_size_ip_columns[:5]


def users_with_5xx_requests():
    with open(FILE_PATH, 'r') as log:
        ip_with_5xx = [req.split()[0] for req in log.readlines() if fnmatch(req.split()[8], '5??')]
        freq_ip = Counter(ip_with_5xx).most_common(5)
    return freq_ip
