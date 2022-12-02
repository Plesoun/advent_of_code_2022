most_calories = []
pack_contents = 0
pack_number = 0

with open("input", "r") as f:
    for line in f.readlines():
        if '\n' == line:
            pack_number += 1
            most_calories.append(pack_contents)
            pack_contents = 0
            continue
        pack_contents += int(line.rstrip())

print("top 3 most cal heavy elves: ", sorted(most_calories)[-3:])
print("Top three totaled", sum(sorted(most_calories)[-3:]))
