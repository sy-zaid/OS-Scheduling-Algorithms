class process:
    def __init__(self,process_name,arrival_time,burst_time,priority=0):
        self.process_name = process_name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority

class process_list():
    def __init__(self,lst_arrival_times, lst_burst_times, lst_prior = None, qt = 0):
        self.lst_arrival_times = lst_arrival_times
        self.lst_burst_times = lst_burst_times
        self.lst_prior = lst_prior
        self.qt = qt
        self.process_list = []
        self.num_processes = len(self.lst_arrival_times)
    
    def createprocessList(self):
        for i in range(0,self.num_processes):
            process_name = f"Process-{i}"
            process_arrival_time = self.lst_arrival_times[i]
            process_burst_time = self.lst_burst_times[i]
            self.process_list.append(process(process_name,process_arrival_time,process_burst_time))
        
        return process_list
            
        
    def __getlist__(self):
        res = []
        for i in range(self.num_processes):
            res.append(self.process_list[i].process_name)
            
        return res
    
    def sortListByArrivalTime(self): 
        self.process_list.sort(key=lambda x: x.arrival_time) 
        return self.process_list
    
    def sortListByBurstTime(self):
        self.process_list.sort(key=lambda x: x.burst_time)
        return self.process_list
        
        


# Input examples from the Front-end.
arrival_times = [3,1,2]
burst_times = [1,2,4]  
input1 = process_list(arrival_times,burst_times)
input1.createprocessList()
input1.sortListByArrivalTime()
print(input1.__getlist__())
input1.sortListByBurstTime()
print(input1.__getlist__())
priorities = [1, 2, 3] # High to Low
# OR
quantum_time = 2