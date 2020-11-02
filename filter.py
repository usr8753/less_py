sequences = [14, 145, 23, 23, 10, 9, 5, 4, 2, 1, 17, 7, 83]

for element in sequences:
    if element > 4:
        print(element)

def my_filter(element):
    return element > 4

filtered_result = filter(my_filter, sequences)

print(list(filtered_result))
print(set(filtered_result))

# with lambda
filtered_result = filter(lambda x:x>4, sequences)
