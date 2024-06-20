
def fifo_function(processes):
    current_time = 0
    for process in processes:
        if process.arrival_time > current_time:
            current_time = process.arrival_time

        process.waiting_time = current_time - process.arrival_time
        current_time += process.cpu_burst

        process.turnaround_time = current_time - process.arrival_time

    # Calculate average waiting time and turnaround time
    avg_waiting_time = sum(process.waiting_time for process in processes) / len(processes)
    avg_turnaround_time = sum(process.turnaround_time for process in processes) / len(processes)

    # Print results
    print("FIFO Scheduling Results:")
    print("Average Waiting Time:", avg_waiting_time)
    print("Average Turnaround Time:", avg_turnaround_time)
    print("Individual Process Statistics:")
    for process in processes:
        print(f"Process: {process.name}, Waiting Time: {process.waiting_time}, Turnaround Time: {process.turnaround_time}")


