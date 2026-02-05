from collections import defaultdict, deque
import time
import threading


class RateLimit:
    def __init__(self, limit: int):
        self.limit = limit
        self.request = defaultdict(deque)
        self.lock = threading.Lock()
    
    def allow_request(self, user_id: str) -> bool:
        current_time = int(time.time() * 1000)  # milliseconds
        
        with self.lock:
            request_queue = self.request[user_id]
            
            # Remove requests older than 60 seconds
            while request_queue and current_time - request_queue[0] > 60000:
                request_queue.popleft()
            
            if len(request_queue) < self.limit:
                request_queue.append(current_time)
                return True
            return False


def main():
    # Create a rate limiter with a limit of 5 requests per minute
    rate_limiter = RateLimit(5)
    
    # Simulate 10 requests from different users
    for i in range(1, 11):
        user_id = f"user{i}"
        allowed = rate_limiter.allow_request(user_id)
        print(f"Request from {user_id} is {'allowed' if allowed else 'blocked'}")


if __name__ == "__main__":
    main()
