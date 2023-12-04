import os
import time

def get_folder_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def write_to_log(message, log_file_path):
    with open(log_file_path, "a") as log_file:
        log_file.write(message + "\n")

def monitor_folder_growth(path, log_file_path, interval=60):
    prev_size = get_folder_size(path)
    while True:
        time.sleep(interval)
        new_size = get_folder_size(path)
        growth = new_size - prev_size
        growth_rate = growth / interval  # Bytes per second
        log_message = f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Folder size increased by {growth} bytes in the last {interval} seconds. Growth rate: {growth_rate} bytes/sec"
        print(log_message)
        write_to_log(log_message, log_file_path)
        prev_size = new_size

# Main execution
if __name__ == "__main__":
    folder_path = "C:\\posttest"  # Replace with the path to your folder
    log_file_path = "C:\\posttest\\logfile.log"  # Replace with the path to your log file
    monitor_folder_growth(folder_path, log_file_path)
