class TimeMap(object):

    def __init__(self):
        self.timemap = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key] += [(value, timestamp)]

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        arr = self.timemap.get(key,[])
        l , r = 0,  len(arr) - 1
        res = ""

        while l<=r:
            mid = (l+r) // 2

            if arr[mid][1] == timestamp:
                res = arr[mid][0]
                break
            elif arr[mid][1] < timestamp:
                res = arr[mid][0]
                l = mid+1
            else:
                r = mid-1
        return res
            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)