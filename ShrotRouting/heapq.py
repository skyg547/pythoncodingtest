# 힙 라이브러리 사용 예제
import _heapq


# 오름차순 힙 령(heapSort)
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        _heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(_heapq.heappop(h))
    return result


result = heapsort(([1, 3, 5, 6, 9, 2, 4, 6, 8, 0]))

print(result)


# 내림차순 힙 정렬(Heap Sort) 따로 제공 x 부호를 바꿔서 넣기
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        _heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-_heapq.heappop(h))
    return result


result = heapsort([1, 3, 5, 6, 9, 2, 4, 6, 8, 0])
print(result)
