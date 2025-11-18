def make_stats_tracker():
    stats = {"count": 0, "sum": 0.0, "min": float('inf'), "max": float('-inf')}
    
    def add_value(value: float):
        stats["count"] += 1
        stats["sum"] += value
        stats["min"] = min(stats["min"], value)
        stats["max"] = max(stats["max"], value)
        
        avg = stats["sum"] / stats["count"]
        print(f"Count: {stats['count']}, Avg: {avg:.2f}, Min: {stats['min']}, Max: {stats['max']}")
    
    return add_value


def main():
    tracker = make_stats_tracker()
    tracker(10)
    tracker(20)
    tracker(5)


if __name__ == '__main__':
    main()