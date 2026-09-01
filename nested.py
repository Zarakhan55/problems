# for x in range (1,4):
#     for y in range (1,4):
#         print(x,y)
# for i in range(1, 6):
#     for j in range(i):
#         print("*", end="")
#     print()
    
#     print("*", end="") → stay on same line ➡️

# print()             → go to next line ⬇️


for n in range(1, 6):
    for m in range(1, n + 1):
        print(m, end="")
    print()
    
    
names = ["Zara", "Ali", "Sara"]
for name in names:
    print(name)
    
numbers = [10, 20, 30, 40, 50]
total=0
for number in numbers:
    total=total+number
    print(total)