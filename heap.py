import sys
import heapq

mval_list = []
paris_list = []

mval_list.clear()
paris_list.clear()

sys_maxsize_simulation = 9223372036854775807  # This is typically the value of sys.maxsize on most 64-bit systems

heapq.heappush(mval_list, -sys_maxsize_simulation)
heapq.heappush(mval_list, sys_maxsize_simulation)

print("Heap:", mval_list)

