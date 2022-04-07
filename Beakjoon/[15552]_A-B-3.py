#문제: https://www.acmicpc.net/problem/15552
import sys
input = sys.stdin.readline

c = int(input())
for _ in range(c):
    a, b = map(int, input().split())
    print(a + b)