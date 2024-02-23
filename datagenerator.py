import csv
import random
from datetime import datetime, timedelta

def generate_random_temperature(last_temp, machine_id):
    """
    Generates a random temperature based on the last temperature recorded,
    with more fluctuations for a specific machine 
    """
    min_temp = max(20, last_temp - 2)
    max_temp = min(100, last_temp + 2)
    
    # Adjust fluctuation range based on machine_id
    if machine_id == 1:
        min_temp = max(10, last_temp - 5)
        max_temp = min(110, last_temp + 5)
    
    return round(random.uniform(min_temp, max_temp), 2)

def generate_machine_temperature_data(start_datetime, end_datetime, interval, num_machines):
    """
    Generates random temperature data for multiple machines.
    """
    machine_data = {}
    for machine_id in range(1, num_machines + 1):
        machine_data[machine_id] = []
        last_datetime = start_datetime
        last_temp = random.uniform(20, 100)
        
        while last_datetime < end_datetime:
            last_datetime += timedelta(minutes=interval)
            last_temp = generate_random_temperature(last_temp, machine_id)
            timestamp = last_datetime.strftime("%Y-%m-%d %H:%M:%S")
            machine_data[machine_id].append((timestamp, last_temp))
    
    return machine_data

def write_to_csv(machine_data, filename_prefix):
    """
    Writes machine data to CSV files.
    """
    for machine_id, data in machine_data.items():
        filename = f"{filename_prefix}_machine_{machine_id}.csv"
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Timestamp', 'Temperature (C)'])
            csv_writer.writerows(data)
        print(f"Machine {machine_id} data saved to {filename}.")

if __name__ == "__main__":
    start_datetime = datetime(2024, 1, 22)  # Start date for historical data
    end_datetime = datetime.now()  # End date is the current date and time
    interval = 30  # Interval in minutes
    num_machines = 2  # Number of machines
    
    filename_prefix = "historical_temperature_data"

    machine_data = generate_machine_temperature_data(start_datetime, end_datetime, interval, num_machines)
    write_to_csv(machine_data, filename_prefix)