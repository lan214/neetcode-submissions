from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        arr = self.map[key]
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            time = arr[m][0]
            if time < timestamp:
                l = m + 1
            elif time > timestamp:
                r = m - 1
            else:
                return arr[m][1]
        return arr[r][1] if r >= 0 else ""
        
