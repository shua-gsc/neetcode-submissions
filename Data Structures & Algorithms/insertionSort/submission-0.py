# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        arr = pairs[:] # don't mutate input

        snapshots: List[List[Pair]] = []

        for i in range(len(arr)):
            current = arr[i]
            j = i - 1

            # Stable: shift only greater than keys
            while j >= 0 and arr[j].key > current.key:
                arr[j + 1] = arr[j]
                j -= 1
            
            arr[j + 1] = current
            snapshots.append(arr[:]) # snapshot after each insertion

        return snapshots
