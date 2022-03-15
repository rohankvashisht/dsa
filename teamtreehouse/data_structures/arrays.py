# Video link: https://www.youtube.com/watch?v=8hly31xKli0
new_list = [5,8,3,7]
result = new_list[0]

if 1 in new_list: print(True)

for n in new_list:
  if n == 1:
    print(True)

    break

# Adding to a list (3 methods)

new_list.insert(0, 45)

new_list.append(4)
new_list.append([65,13,17])

new_list.extend([6,9,4,8])

print(new_list)
