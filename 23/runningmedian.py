#bisect: 점프투파이썬 - https://wikidocs.net/105425
#bisect document: https://docs.python.org/ko/3/library/bisect.html

from sys import stdin
from bisect import insort_left

if __name__=='__main__':
    for _ in range(int(stdin.readline())):
        N, a, b = map(int, stdin.readline().split())
        ans = 0
        A = [1983]
        temp = 1983
        for i in range(N):
            ans += A[(len(A)-1)//2]
            temp = (temp * a + b) % 20090711
            insort_left(A, temp) #이진 분할 알고리즘으로 정렬된 리스트를 구성
        print(ans%20090711)

#heapq document: https://docs.python.org/ko/3/library/heapq.html 
import heapq

def main():
    for _ in range(int(input().strip())):
        N, a, b = map(int, input().strip().split())
        cur = 1983
        ans = 0
        
        #the heapq is for min heap,
        #so need to change the sign of the element in max heap
        max_heap = []
        min_heap = [] 

        for i in range(N):
            if(len(max_heap) > len(min_heap)):
                heapq.heappush(min_heap, cur)
            else:
                heapq.heappush(max_heap, -cur)

            if max_heap and min_heap and -max_heap[0] > min_heap[0]:
                t1 = heapq.heappop(min_heap)
                t2 = heapq.heappop(max_heap)
                heapq.heappush(min_heap, -t2)
                heapq.heappush(max_heap, -t1)

            ans += -max_heap[0]
            cur = (cur * a + b) % 20090711

        print((ans) % 20090711)
"""
if __name__ == '__main__':
    main()
"""
