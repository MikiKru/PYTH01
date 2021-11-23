listA = [1,2,3]
listB = ['A','B','C']

listA.extend(listB)
print(listA, listB)
listA.insert(3, None)
print(listA)
listA[3] = "NEW"
print(listA)
# listA[100]    - uwaga na adresowanie


queue = []                              # FILO
queue.append("E1")
queue.append("E2")
queue.append("E3")
queue.append("E4")
print(queue)
print("usunięto: " + queue.pop())
print("usunięto: " + queue.pop())
print("usunięto: " + queue.pop())
print(queue)