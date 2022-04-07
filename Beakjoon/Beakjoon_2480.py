import statistics

a, b, c = map(int, input().split())

if(a == b == c and a == c): print(10000 + a*1000) 
elif(a != b != c and a != c): print(max(a,b,c) * 100)
else: print(1000 + statistics.mode([a,b,c])*100)

# def solve(a, b, c):
#     #a, b, c = map(int, input().split())
#     if(a == b == c and a == c): print(10000 + a*1000)  # 3개 
#     elif(a != b != c and a != c): print(max(a,b,c) * 100) # 0개
#     else: print(1000 + statistics.mode([a,b,c])*100) #2개
# for i in range(1,7):
#     print('---------------------')
#     for j in range(1,7):
#         for k in range(1,7):
#             print(i, j, k, ':',end = '')
#             solve(i, j, k)
            