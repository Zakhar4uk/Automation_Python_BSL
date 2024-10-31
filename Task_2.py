from datetime import datetime

def filter_logs(start_time, end_time, log_path):
    start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_time = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")

    with open(log_path, 'r') as file:
        for line in file:
            try:
                date_str = " ".join(line.split()[:3]) + f" {start_time.year}"
                log_date = datetime.strptime(date_str, "%b %d %H:%M:%S %Y")
                    
                if start_time <= log_date <= end_time:
                    print(line.strip())
            except:
                pass

if __name__ == "__main__":
    start = "2024-10-27 00:00:00"
    end = "2024-10-27 00:01:00"
    filter_logs(start, end, "messages")
