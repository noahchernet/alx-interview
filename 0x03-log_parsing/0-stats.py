#!/usr/bin/python3
'''Module 0-stats.py
Reads standard input line by line and computes metrics:
'''
import fileinput
import re


def main():
    '''Program execution starts here
    Logs from standard output are read and their status codes and their
    frequencies are printed.
    If a log line doesn't match the format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file-size>
    it's skipped'''
    count = 0
    total_file_size = 0
    status_codes = {200: 0, 301: 0,
                    400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    try:
        for line in fileinput.input():
            # Check if the line has the correct log format,
            # else continue to the next line
            log = re.match(
                r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.+\]' +
                r' "GET /projects/260 HTTP/1.1" \d{3} [0-9]+$', line)

            if log:
                status_code = int(
                    re.match(r'.*?([0-9]+) \d+$', log.string).group(1))
                file_size = int(re.match('.*?([0-9]+)$', log.string).group(1))
                # print("File size: " + str(file_size) + " Status code: " +
                # str(status_code))

                total_file_size += file_size

                if status_code in list(status_codes.keys()):
                    status_codes[status_code] += 1

            else:
                continue
            # Counting each line regardless of having matching log format
            count += 1

            if count != 0 and count % 10 == 0:
                print_codes(status_codes, total_file_size)

    except KeyboardInterrupt:
        print_codes(status_codes, total_file_size)
        raise


def print_codes(status_codes, total_file_size):
    """Prints the status code and the number of times they appear"""
    print("File size: {}".format(total_file_size))
    for i in [200, 301, 400, 401, 403, 404, 405, 500]:
        if status_codes[i] != 0:
            print("{}: {}".format(i, status_codes[i]))


if __name__ == "__main__":
    main()
