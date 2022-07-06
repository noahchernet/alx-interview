#!/usr/bin/python3
'''Module 0-stats.py
Reads standard input line by line and computes metrics:
'''
import fileinput
import re
import sys


def main():
    count = 0
    total_file_size = 0
    status_codes_compilation = {200: 0, 301: 0,
                                400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    try:
        '''Program execution starts here'''
        for line in fileinput.input():
            # Check if the line has the correct log format,
            # else continue to the next line
            log = re.match(
                r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.+\]' +
                r' "GET /projects/260 HTTP/1.1" \d{3} [0-9]+$', line)

            if log:
                count += 1
                status_code = int(
                    re.match(r'.*?([0-9]+) \d+$', log.string).group(1))
                file_size = int(re.match('.*?([0-9]+)$', log.string).group(1))
                # print("File size: " + str(file_size) + " Status code: " +
                # str(status_code))

                total_file_size += file_size

                if status_code in list(status_codes_compilation.keys()):
                    status_codes_compilation[status_code] += 1

            else:
                continue

            if count == 10:
                count = 0  # Reset the counter

                # Print cumulative file size
                print("File size: " + str(total_file_size))
                for i in [200, 301, 400, 401, 403, 404, 405, 500]:
                    if status_codes_compilation[i] != 0:
                        print(i, status_codes_compilation[i])
    except KeyboardInterrupt:
        # Print cumulative file size
        print("File size: {}".format(total_file_size))
        for i in [200, 301, 400, 401, 403, 404, 405, 500]:
            if status_codes_compilation[i] != 0:
                print("{}: {}".format(i, status_codes_compilation[i]))
        raise


if __name__ == "__main__":
    main()
