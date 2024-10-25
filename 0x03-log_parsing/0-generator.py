#!/usr/bin/python3
import sys

# Initialize total size and status code counts
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
    """Prints the total file size and the count of status codes"""
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


try:
    for line in sys.stdin:
        try:
            parts = line.split(" ")
            if len(parts) < 7:
                continue

            # Extracting the file size and status code
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            # Updating metrics
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1

            line_count += 1

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats()

        except Exception:
            continue

except KeyboardInterrupt:
    print_stats()
    raise

print_stats()
