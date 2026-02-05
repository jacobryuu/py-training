from dataclasses import dataclass
from typing import Optional


@dataclass
class ScheduledTask:
    id: str
    priority: int
    duration_millis: int  # 模拟执行时间


class ITaskScheduler:
    def submit(self, task: ScheduledTask):
        raise NotImplementedError
    
    def poll(self) -> Optional[ScheduledTask]:
        raise NotImplementedError


class TaskScheduler(ITaskScheduler):
    def submit(self, task: ScheduledTask):
        pass
    
    def poll(self) -> Optional[ScheduledTask]:
        return None
