lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Oscar", "Toby"]


friends.sort()
lucky_numbers.sort()
lucky_numbers.reverse()

friends.append("Creed")
friends.insert(1, "Kelly") # insert is 2 params
friends.remove("Jim") # Remove item
# friends.clear() # everything remove

print(friends.index("Kevin"))
print(friends.count("Oscar"))

friends.extend(lucky_numbers)
print(friends)


friends2 = friends.copy()
print(friends2)
