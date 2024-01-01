from Process_classes import process_list

def FCFS(inp_arrival_times, inp_burst_times):
    inp_process_list = process_list(inp_arrival_times, inp_burst_times)
    inp_process_list.createprocessList()
    print("Unsorted Process List:", inp_process_list.__getlist__(), '\n\n')

    # Sorting the input process list.
    inp_process_list.sortListByArrivalTime()
    print("Sorted Process List:", inp_process_list.__getlist__(), '\n\n')

    curBT, prevBT = 0, 0
    curProcess = 0
    processAT= 0
    time_pointer = 0
    idleTime, total_idle_time = 0, 0

    gantt_chart = []  # Process_name,Start_Time, Completion_Time
    # print("Total-BurstTime:",inp_process_list.__getTotalBurstTime__())
    print(inp_process_list.__getlist__())
    for process_num in range(0,inp_process_list.length()):
        curProcess = inp_process_list.__getprocess__(process_num)
        processAT = curProcess.arrival_time
        

        print("Current Process", curProcess.process_name)
        print("ProcessAT, curBT, prevBT", processAT, curBT, prevBT,time_pointer)
        print("Timepointer:",time_pointer)

        if processAT > time_pointer:
            idleTime = processAT - time_pointer
            
            time_pointer += total_idle_time
            total_idle_time += idleTime
            gantt_chart.append([processAT-idleTime, 'Idle',idleTime, time_pointer,total_idle_time])
        
        if processAT < time_pointer:
            processAT = time_pointer

        time_pointer = processAT + curProcess.burst_time # 3,
        
        gantt_chart.append([processAT, curProcess.process_name,time_pointer])
        curBT = curProcess.burst_time + prevBT
        prevBT += curBT
        

    print("Gantt Chart:", gantt_chart)
    print("Execution Sequence:", [entry[1] for entry in gantt_chart])

# Input examples from the Front-end.
# arrival_times = [1, 4, 5, 6]
# burst_times = [2, 3, 2, 1]
# input1 = FCFS(arrival_times, burst_times)


arrival_times = [1,10,5,6]
burst_times = [2,3,3,10]
input1 = FCFS(arrival_times, burst_times)