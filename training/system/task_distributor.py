import threading
from queue import Queue
from dataclasses import dataclass
from typing import Callable, Optional
import time


@dataclass
class Task:
    offset: int
    data: object


@dataclass
class TaskAndCallback:
    task: Task
    callback: Callable[[], None]


class WorkManager:
    def add_task(self, task: Task):
        raise NotImplementedError
    
    def get_complete_offset(self) -> int:
        raise NotImplementedError
    
    def poll(self) -> Optional[TaskAndCallback]:
        raise NotImplementedError


class TaskDistributor(WorkManager):
    def __init__(self):
        self.tasks_queue = Queue()
        self.complete_offset = 0
        self.completed = set()
        self.next_offset = -1
        self.lock = threading.Lock()
    
    def add_task(self, task: Task):
        if self.next_offset == -1 or task.offset == self.next_offset + 1:
            self.next_offset = task.offset
        else:
            raise ValueError("Task offset must be sequential")
        
        def callback():
            with self.lock:
                self.completed.add(task.offset)
                while self.complete_offset + 1 in self.completed:
                    self.complete_offset += 1
                    self.completed.remove(self.complete_offset)
        
        self.tasks_queue.put(TaskAndCallback(task, callback))
    
    def get_complete_offset(self) -> int:
        return self.complete_offset
    
    def poll(self) -> Optional[TaskAndCallback]:
        try:
            return self.tasks_queue.get()
        except:
            return None


def worker(manager: TaskDistributor):
    while True:
        task_and_callback = manager.poll()
        if task_and_callback is None:
            continue
        
        print(f"Processing task {task_and_callback.task.offset}")
        time.sleep(0.1)  # simulate work
        
        task_and_callback.callback()
        print(f"Completed task {task_and_callback.task.offset}")


def watermark_monitor(manager: TaskDistributor):
    while True:
        offset = manager.get_complete_offset()
        print(f"Watermark: {offset}")
        time.sleep(0.3)


def main():
    manager = TaskDistributor()
    
    # Start 5 worker threads
    for i in range(5):
        thread = threading.Thread(target=worker, args=(manager,), daemon=True)
        thread.start()
    
    # Add tasks
    for i in range(10, 16):
        manager.add_task(Task(i, f"Data-{i}"))
    
    # Periodically check watermark
    monitor_thread = threading.Thread(target=watermark_monitor, args=(manager,), daemon=True)
    monitor_thread.start()
    
    # Keep main thread alive for a while
    time.sleep(3)


if __name__ == "__main__":
    main()
