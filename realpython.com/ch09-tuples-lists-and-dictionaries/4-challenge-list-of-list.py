# 9.4 Challenge: List of lists

# Write a program that contains the following lists of lists:

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(list_of_universities):
    student_enrollment_values = []
    tuition_fees = []

    for items in list_of_universities:
        student_enrollment_values.append(items[1])
        tuition_fees.append(items[2])
    return student_enrollment_values, tuition_fees

def mean(values):
    return sum(values)/ len(values)

def median(values):
    values.sort()
    if len(values) % 2 == 1:
        center_index = int(len(values)/2)
        return values[center_index]
    else:
        left_center_index = (len(values) - 1) / 2
        right_center_index = (len(values) + 1) / 2
        return mean([values[left_center_index], values[right_center_index]])

totals = enrollment_stats(universities)

print("\n")
print("*****" * 6)
print(f"Total students:   {sum(totals[0]):,}")
print(f"Total tuition:  $ {sum(totals[1]):,}")
print(f"\nStudent mean:     {mean(totals[0]):,.2f}")
print(f"Student median:   {median(totals[0]):,}")
print(f"\nTuition mean:   $ {mean(totals[1]):,.2f}")
print(f"Tuition median: $ {median(totals[1]):,}")
print("*****" * 6)
print("\n")