def calculate_waiting_time(processes, n, bt, wt):
    wt[0] = 0

    for i in range(1, n):
        wt[i] = bt[i - 1] + wt[i - 1]

def calculate_turnaround_time(processes, n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]

def calculate_idle_time(processes, n, bt, wt, tat):
    total_idle_time = 0
    for i in range(1, n):
        idle_time = wt[i] - tat[i-1]
        if idle_time > 0:
            total_idle_time += idle_time

    return total_idle_time

def fcfs_scheduling(processes, n, bt, at):
    wt = [0] * n
    tat = [0] * n

    calculate_waiting_time(processes, n, bt, wt)
    calculate_turnaround_time(processes, n, bt, wt, tat)

    total_idle_time = calculate_idle_time(processes, n, bt, wt, tat)

    print("Process\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i]}\t\t{at[i]}\t\t{bt[i]}\t\t{wt[i]}\t\t{tat[i]}")

    print(f"\nTotal Idle Time: {total_idle_time}")

# Example usage
if __name__ == "__main__":
    processes = [0,1,2,3]
    burst_time = [1,4,5,6]
    arrival_time = [2,3,2,1]
    num_processes = len(processes)

    fcfs_scheduling(processes, num_processes, burst_time, arrival_time)
