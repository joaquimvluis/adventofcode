meals = []
meal = []
i = 0

with open('input.txt') as f:
    for line in f.readlines():
        if line == '\n':
            meals.append(meal)
            meal=[]
            i += 1
        else:
            meal.append(int(line.strip()))

max = 0
meals_calories = []
for meal in meals:
    sum = 0
    for calories in meal:
        sum += calories
    meals_calories.append(sum)

    if sum > max:
        max = sum

print("The Elf carrying the most amount of calories is carrying: {} calories".format(max))

###### second part
meals_calories.sort(reverse=True)
top3 = 0
for calories in meals_calories[0:3]:
   top3 += calories
print("The top three Elves are carrying a total of {} calories".format(top3))



