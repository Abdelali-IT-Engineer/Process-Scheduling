def sjf_function(processes):
    """
    Simulates the Shortest Job First (SJF) scheduling algorithm.

    Args:
        processes: A list of Process objects.

    Prints the Gantt chart and calculates waiting time and turnaround time for each process.
    """
    processes.sort(key=lambda process: process.arrival_time)  # Sort by arrival time initially
    
    current_time = 0
    completed_processes = []
    remaining_processes = processes.copy()
    
    while remaining_processes:
        # Filter processes that have arrived by current time
        available_processes = [p for p in remaining_processes if p.arrival_time <= current_time]
        
        if not available_processes:
            # If no process has arrived, move time forward to the next arriving process
            current_time = remaining_processes[0].arrival_time
            available_processes = [p for p in remaining_processes if p.arrival_time <= current_time]
        
        # Select the process with the shortest CPU burst from the available processes
        next_process = min(available_processes, key=lambda process: process.cpu_burst)
        
        completed_time = current_time + next_process.cpu_burst
        next_process.waiting_time = current_time - next_process.arrival_time
        next_process.turnaround_time = next_process.waiting_time + next_process.cpu_burst

        completed_processes.append(next_process)
        remaining_processes.remove(next_process)
        current_time = completed_time

        print(f"[{current_time - next_process.cpu_burst}:{current_time}] Process {next_process.name}")

    # Calculate average waiting time and turnaround time
    avg_waiting_time = sum(process.waiting_time for process in completed_processes) / len(completed_processes)
    avg_turnaround_time = sum(process.turnaround_time for process in completed_processes) / len(completed_processes)

    print(f"Average Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")

