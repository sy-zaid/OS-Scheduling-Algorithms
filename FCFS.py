from Process_classes import process

# Number of process from the user.
# num_processes = eval(input('Enter number of processes you want to calculate.'))

num_processes = 4

gantt_chart = []
job_que = []

execution_state = []

p1 = process('p1', 0, 6)
p2 = process('p2', 2, 4)
p3 = process('p3', 1, 3)
p4 = process('p4', 1, 2)

temp_que = [p1, p2, p3, p4]
# print(temp_que)

arrival_times = [p1.arrival_time, p2.arrival_time, p3.arrival_time, p4.arrival_time]

sorted_process = sorted(temp_que,
                        key=lambda x: x.arrival_time)  # These processes are sorted on the basis of their arrival times.


# print(sorted_process)
def check_arrival_time(lst, AT):
    res = []
    for i in lst:
        if i.arrival_time == AT:
            res.append(i)
    res = sorted(res, key=lambda x: x.burst_time)
    return res


# print(check_arrival_time(sorted_process, 1)[0].process_name)

AT = 0
total_execution_time = 0

for i in range(0, 4):

    if len(check_arrival_time(sorted_process, AT)) == 1:

        gantt_chart.append(
            [sorted_process[AT].process_name])

        job_que.append(
            [sorted_process[AT].process_name, sorted_process[AT].arrival_time, sorted_process[AT].burst_time])

        sorted_process[AT].burst_time -= 1
        total_execution_time += 1
        AT += 1

    elif len(check_arrival_time(sorted_process, AT)) > 1:
        for process in check_arrival_time(sorted_process, AT):
            job_que.append(
                [process.process_name, process.arrival_time, process.burst_time])

        # process.burst_time -= 1
        total_execution_time += 1
        AT += 1

    # if total_execution_time == sorted_process[AT].arrival_time:
    #     # print('total_execution_time', total_execution_time)
    #     same_process = check_arrival_time(sorted_process, total_execution_time)
    #
    #     sorted_same_process = sorted(same_process, key=lambda x: x.burst_time)
    #     print('sorted_same_process', sorted_same_process[0].process_name)
    #
    #     for k in range(len(sorted_same_process)):
    #         job_que.append(
    #             [sorted_same_process[k].process_name, sorted_same_process[AT].arrival_time,
    #              sorted_same_process[AT].burst_time])

print(p1.process_name, p1.arrival_time, p1.burst_time)
print(p2.process_name, p2.arrival_time, p2.burst_time)
print(p3.process_name, p3.arrival_time, p3.burst_time)
print(p4.process_name, p4.arrival_time, p4.burst_time)

# print(p1.burst_time)
print("GANTT CHART:", gantt_chart)
print("JOB QUEUE:", job_que)
