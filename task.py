import operator
slots = {
    1: 380 * 37,
    2: 220 * 83,
    3: 1087 * 80,
    4: 3948 * 109,
    5: 5773 * 38,
    6: 183 * 100,
    7: 2999 * 489,
    8: 269 * 10388,
    9: 2739 * 380,
    10: 4872 * 286
}
# Calculate amounts for each slot
arr = slots
print(arr)

print("")
acc = sorted(arr.items(), key=operator.itemgetter(1))
print("---------asending order---------------------")
print(acc)
#ascending_slots = sorted(arr.items(), key=lambda x: x[1])
#print(ascending_slots)

print("-----------decending order-------------------")
print(acc[::-1])

print("_________________final output for highest_____________________ ")

'''print(acc[0])
print(acc[1])
print(acc[2])'''
print(acc[:3])


print("_________________final output for lowest_____________________ ")

'''print(acc[7])
print(acc[8])
print(acc[9])'''
print(acc[-3:])