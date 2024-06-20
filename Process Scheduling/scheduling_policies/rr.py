def rr_function(processes, time_quantum):
    """
    Simulates the Round Robin (RR) scheduling algorithm.

    Args:
        processes: A list of Process objects.
        time_quantum: The time quantum for RR scheduling.

    Prints the Gantt chart and calculates waiting time and turnaround time for each process.
    """
    ready_queue = []  # Queue for processes ready to be executed
    completed_processes = []
    current_time = 0

    while processes or ready_queue:
        # Add processes that have arrived at current time
        ready_queue.extend([p for p in processes if p.arrival_time <= current_time])
        processes = [p for p in processes if p.arrival_time > current_time]

        # Check if ready queue is empty
        if not ready_queue:
            current_time += 1
            continue

        # Get the first process from the queue
        process = ready_queue.pop(0)

        # Execute the process for the time quantum or remaining burst
        execution_time = min(time_quantum, process.remaining_burst)
        print(f"[{current_time}:{current_time + execution_time}] Process {process.name}")
        
        current_time += execution_time
        process.remaining_burst -= execution_time

        # Process completed
        if process.remaining_burst == 0:
            process.turnaround_time = current_time - process.arrival_time
            completed_processes.append(process)
        else:
            # Add back the process to the ready queue for further execution
            ready_queue.append(process)

    # Calculate average waiting time and turnaround time
    for process in completed_processes:
        process.waiting_time = process.turnaround_time - process.cpu_burst
    
    avg_waiting_time = sum(process.waiting_time for process in completed_processes) / len(completed_processes)
    avg_turnaround_time = sum(process.turnaround_time for process in completed_processes) / len(completed_processes)

    print(f"Average Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")

