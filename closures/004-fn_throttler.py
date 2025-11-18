import time

def rate_limit(min_interval: float):
    last_called = [0.0]  # Mutable to avoid nonlocal
    
    def decorator(func):
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            if elapsed < min_interval:
                print(f"Rate limited. Wait {min_interval - elapsed:.2f}s")
                return None
            last_called[0] = time.time()
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(2.0)
def api_call():
    print("API called!")

def main():
    for _ in range(5):
        api_call()
        time.sleep(1)

if __name__ == '__main__':
    main()