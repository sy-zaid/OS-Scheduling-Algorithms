from Process_classes import process_list
def FCFS(inp_arrival_times,inp_burst_times):
    """
    Function to simulate the FCFS algorithm.
    
    VARIABLES:
    - inp_arrival_time: A list of all the arrival times given by the user.
    - inp_burst_time: A list of all the burst times given by the user.
    
    OUTPUT REQUIREMENTS:
    
    - Execution Sequence
    
    - Turn Around Time (for each process)
    --- Formula: Turnaround Time (TAT)=Completion Time-Arrival Time (AT)
    
    - Finish Time (for each process)
    ---  Formula: Finish Time (FT)=Arrival Time (AT)+Turnaround Time (TAT)
    
    - Waiting Time (for each process)
    --- Formula: Waiting Time (WT)=Turnaround Time (TAT)-Burst Time
    
    - Average Turn Around Time
    --- Formula: Average Turnaround Time (AvgTAT)= 
                                                    Number of Processes/
                                            Sum of Turnaround Times of all processes

    - Average Waiting Time 
    --- Formula: Average Waiting Time (AvgWT)= 
                                                Number of Processes/
                                            Sum of Waiting Times of all processes
    """
    
    
    inp_process_list = process_list(inp_arrival_times,inp_burst_times)
    inp_process_list.createprocessList()
    print("Unsorted Process List:",inp_process_list.__getlist__(),'\n\n')
    
    # Sorting the input process list.
    inp_process_list.sortListByArrivalTime()
    print("Sorted Process List:",inp_process_list.__getlist__(),'\n\n')
    
    curBT,prevBT = 0,0
    curProcess = inp_process_list.__getprocess__(0)
    curAT,prevAT = curProcess.arrival_time, 0
    
    idleTime, total_idle_time = 0, 0
    
    completion_time = 0
    execution_sequence = []
    gantt_chart = [] # Process_name,Start_Time, Completion_Time
    # print("Total-BurstTime:",inp_process_list.__getTotalBurstTime__())
    
    
    # print("Current Process:",curProcess.process_name,'\n')
    
    for process in range(0,inp_process_list.length()+idleTime):
        curProcess = inp_process_list.pop()
        print("Current Process",curProcess.process_name)
        if curAT != curBT:
            idleTime = curAT - curBT
            gantt_chart.append(["No process",idleTime])
            total_idle_time += idleTime
        else:
            if len(gantt_chart) == 0:
                gantt_chart.append()
                
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    





# Input examples from the Front-end.
arrival_times = [1,4,5,6]
burst_times = [2,3,2,1]  

input1 = FCFS(arrival_times,burst_times)



priorities = [1, 2, 3] # High to Low
# OR
quantum_time = 2