#문제: https://www.acmicpc.net/problem/2525
h, m = map(int, input().split())
s = int(input())
a = (60*h + m) + s

if((a/60) >= 24) :print(int(a/60 - 24), int(a%60))
else: print(int(a/60), int(a%60))