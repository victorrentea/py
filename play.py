
from enum import Enum


class JobStatus(Enum):
    PENDING = 1
    RUNNING = 2
    SUCCESS = 3
    FAILURE = 4
    CANCELLED = 5

def param_cu_or(p:JobStatus=None):
    print (p or "default val")


param_cu_or(JobStatus.SUCCESS)
param_cu_or()