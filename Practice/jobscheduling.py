#To schedule a set of jobs with given profits and deadlines to maximize the total profit.
from typing import List, Tuple

class Job:
    def __init__(self, job_id: str, deadline: int, profit: int):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

def job_scheduling(jobs: List[Job]) -> Tuple[List[str], int]:
    jobs.sort(key=lambda job: job.profit, reverse=True)
    max_deadline = max(job.deadline for job in jobs)
    schedule = [None] * max_deadline
    total_profit = 0

    for job in jobs:
        for i in range(job.deadline - 1, -1, -1):
            if schedule[i] is None:
                schedule[i] = job.job_id
                total_profit += job.profit
                break

    scheduled_jobs = [job_id for job_id in schedule if job_id is not None]
    return scheduled_jobs, total_profit

jobs_list = [
    Job('A', 2, 100),
    Job('B', 1, 50),
    Job('C', 2, 10),
    Job('D', 1, 20),
    Job('E', 3, 30)
]

scheduled_jobs, max_profit = job_scheduling(jobs_list)
print("Scheduled Jobs:", scheduled_jobs)
print("Total Profit:", max_profit)
