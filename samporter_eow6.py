# Sam Porter
# 10/04/2026
# End of week assignment - week 6

# Exercise 1
print("Exercise 1")
employees = ["Bob", "Carlos", "Alice"]
print(employees)

# Add dana to the end of the list
employees.append("Dana")
print(employees)

# Remove bob from the list
employees.remove("Bob")
print(employees)

# Add evenelyn to the beginning of the list
employees.insert(0, "Evelyn")
print(employees)

# Put the list in alphabetical order
employees.sort()
print(employees)


# Exercise 2

print("Exercise 2")
ratings = [5, 4, 3, 5, 5, 5, 2, 3, 3, 3, 3, 2, 5, 4, 3]

# Check if there are any 5-star ratings
print("There are 5-star ratings in the results:", 5 in ratings)


# Count the number of 5-star ratings

print("Number of 5-star ratings:", ratings.count(5))

# Calculate the average rating
average_rating = sum(ratings) / len(ratings)
print("Average ratings:", average_rating)

# Check if there is a 1-star rating
if 1 in ratings:
    print("Low rating exists.")
else:
    print("No 1-star ratings found.")


# Exercise 3


print("Exercise 3")

stock = [120, 45, 300, 53, 90, 6, 200, 108, 43, 2]

# Sort and print the stock in numerical order (smallest to largest)
stock.sort()
print("Ascending:", stock)

# Sort and print the stock in reverse numerical order (Largest to smallest)

stock.sort(reverse=True)
print("Descending:", stock)


# Exercise 4


print("Exercise 4")


revenue = [
    12000,
    15000,
    14000,
    16000,
    18000,
    17000,
    20000,
    21000,
    19000,
    22000,
    23000,
    24000,
]

# Slice the revenue into 4 quarters
q1 = revenue[0:3]
q2 = revenue[3:6]
q3 = revenue[6:9]
q4 = revenue[9:12]

print("Q1:", q1)
print("Q2:", q2)
print("Q3:", q3)
print("Q4:", q4)


# Calculate totals

q1_total = sum(q1)
q2_total = sum(q2)
q3_total = sum(q3)
q4_total = sum(q4)


# Calculate averages

q1_average = q1_total / len(q1)
q2_average = q2_total / len(q2)
q3_average = q3_total / len(q3)
q4_average = q4_total / len(q4)


print(f"Q1 Total: ${q1_total:,.2f}, Average: ${q1_average:,.2f}")
print(f"Q2 Total: ${q2_total:,.2f}, Average: ${q2_average:,.2f}")
print(f"Q3 Total: ${q3_total:,.2f}, Average: ${q3_average:,.2f}")
print(f"Q4 Total: ${q4_total:,.2f}, Average: ${q4_average:,.2f}")


# Exercise 5

import copy

print("Exercise 5")

customer_purchases = [
    "milk",
    ["milk", "bread", "eggs"],
    "bread",
    ["milk", "bread", "eggs", "tp"],
]

print("Number of customers:", len(customer_purchases))

# Check if tp was purchased
found = False

for item in customer_purchases:
    if isinstance(item, list) and "tp" in item:
        found = True
    elif item == "tp":
        found = True

print("TP purchased:", found)

# Create a deep copy
customer_copy = copy.deepcopy(customer_purchases)

# Change tp to butter in the deep copy
customer_copy[3][3] = "butter"

# Print original and deep copy

print("Original list:", customer_purchases)
print("Deep copy:", customer_copy)
