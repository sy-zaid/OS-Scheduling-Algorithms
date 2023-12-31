from Process_classes import process_list

def FCFS(inp_arrival_times, inp_burst_times):
    inp_process_list = process_list(inp_arrival_times, inp_burst_times)
    inp_process_list.createprocessList()
    print("Unsorted Process List:", inp_process_list.__getlist__(), '\n\n')

    # Sorting the input process list.
    inp_process_list.sortListByArrivalTime()
    print("Sorted Process List:", inp_process_list.__getlist__(), '\n\n')

    curBT, prevBT = 0, 0
    curProcess = inp_process_list.pop()
    curAT, prevAT, nextAT = curProcess.arrival_time, 0, 0

    idleTime, total_idle_time = 0, 0

    completion_time = 0
    execution_sequence = []
    gantt_chart = []  # Process_name,Start_Time, Completion_Time
    # print("Total-BurstTime:",inp_process_list.__getTotalBurstTime__())

    for process_num in range(inp_process_list.length() + total_idle_time):

        print("Current Process", curProcess.process_name)
        print("curAT, curBT, prevBT", curAT, curBT, prevBT)

        if curAT > curBT:
            idleTime = curAT - curBT
            gantt_chart.append([curBT, 'Idle', curAT])
            total_idle_time += idleTime

        gantt_chart.append([curAT, curProcess.process_name, curAT + curProcess.burst_time])

        curProcess = inp_process_list.pop()
        curAT = curProcess.arrival_time
        curBT = curProcess.burst_time

    print("Gantt Chart:", gantt_chart)
    print("Execution Sequence:", [entry[1] for entry in gantt_chart])

# Input examples from the Front-end.
arrival_times = [1, 4, 5, 6]
burst_times = [2, 3, 2, 1]
input1 = FCFS(arrival_times, burst_times)
