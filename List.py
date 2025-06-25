# List comprehension is an elegant way to define and create lists based on existing lists.
# Syntax of List Comprehension.
# [expression for item in list]

l = []
for a in range(1, 101):
    # print(a)
    l.append(a)
print(l)

n=[m for m in range(1,101)]
print(n)

n=[h for h in range(1,101) if h%2==0]
print(n)
