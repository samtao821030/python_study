M=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

l1 = [col+10 for row in M for col in row]
print(l1)

l2 = [[col for col in row] for row in M]
print(l2)