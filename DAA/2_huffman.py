# Huffman encoding using a greedy strategy
import heapq
from itertools import count

text = input("Text: ")
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
serial = count()
heap = [(f, next(serial), ch) for ch, f in freq.items()]
heapq.heapify(heap)
if not heap:
    print({})
else:
    while len(heap) > 1:
        f1, _, a = heapq.heappop(heap)
        f2, _, b = heapq.heappop(heap)
        heapq.heappush(heap, (f1 + f2, next(serial), (a, b)))
    codes = {}
    def make_codes(node, code=""):
        if isinstance(node, str):
            codes[node] = code or "0"
        else:
            make_codes(node[0], code + "0")
            make_codes(node[1], code + "1")
    make_codes(heap[0][2])
    print("Codes:", codes)
    print("Encoded:", "".join(codes[c] for c in text))
