sequences = [14, 145, 23, 23, 10, 9, 5, 4, 2, 1, 17, 7, 83]

# if value > 4, give me cursor as result
filter_res = filter(lambda x:x>4, sequences)

# take cursor form filter, if value > 4 then double it
map_res = map(lambda y:y*y, filter_res)

# print cursor using set with random number position
print(set(map_res))
