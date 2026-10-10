def salary_details(salary):
    highest = salary[0]
    lowest = salary[0]
    total = 0
    count = 0

    for i in salary:
        if i > highest:
            highest = i

        if i < lowest:
            lowest = i

        total = total + i

        if i > 50000:
            count = count + 1

    average = total / len(salary)

    return highest, lowest, average, count


salary = [45000, 30000, 20000, 25000]

highest, lowest, average, count = salary_details(salary)

print("Highest salary:", highest)
print("Lowest salary:", lowest)
print("Average salary:", average)
print("salary more than 50000:",count)