def sort_strings(arr):
    if not arr:
        return arr

    max_len = max([len(s) for s in arr])
    buckets = [[] for _ in range(26)]
    for i in range(max_len-1, -1, -1):
        for string in arr:
            if len(string) <= i:
                buckets[0].append(string)
            else:
                index = ord(string[i]) - ord('a')
                buckets[index].append(string)
        arr = []
        for bucket in buckets:
            arr += bucket
            bucket.clear()

    return arr
