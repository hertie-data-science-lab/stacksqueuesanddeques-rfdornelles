## tests

print("Testing...")
D = ArrayDequeMaxlen(5)

print(D._data)
print(D._cap)

print("add first\n")
D.add_first("1")
D.add_first(2)
D.add_first("3")

print(D._data)

print("size:", D.len())
print("first:", D.first())
print("last:", D.last())

print("add last\n")
D.add_last("a")
D.add_last("b")

print(D._data)

print("size:", D.len())
print("first:", D.first())
print("last:", D.last())

print("first:", D.delete_first())
print(D._data)

print("-----------------------------")