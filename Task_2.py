def filter_logs(start_time, end_time, log_path):
    with open(log_path, 'r') as file:
        for line in file:
            timestamp_str = line[:19]
            
            if start_time <= timestamp_str <= end_time:
                print(line.strip())

if __name__ == "__main__":
    filter_logs("2024-10-29 12:00:00", "2024-10-29 14:00:00", "logs.txt")
