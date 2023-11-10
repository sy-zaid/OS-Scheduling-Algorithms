class process:
    def __init__(self,process_name,arrival_time,burst_time):
        self.process_name = process_name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
    
    def arrival_time(self):
        return self.arrival_time
    
    def burst_time(self):
        return self.burst_time

    def process_name(self):
        return self.process_name

