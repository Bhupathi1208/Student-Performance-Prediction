study_hours = [2, 3, 4, 5, 6, 7, 8, 1, 3, 5,
               4, 6, 7, 8, 2, 9, 5, 4, 7, 6]
attendance = [60, 65, 70, 75, 80, 85, 90, 55, 68, 78,
              72, 82, 88, 95, 62, 96, 79, 74, 91, 84]
previous_score = [45, 50, 55, 60, 65, 70, 75, 40, 52, 63,
                  58, 68, 73, 80, 48, 85, 62, 57, 78, 71]
final_score = [48, 53, 58, 64, 70, 76, 84, 42, 55, 67,
               61, 72, 79, 88, 50, 92, 70, 63, 85, 77]

def average(values):
    total = 0

    for value in values:
        total += value

    return total / len(values)


avg_study = average(study_hours)
avg_attendance = average(attendance)
avg_previous = average(previous_score)
avg_final = average(final_score)

study_dev = []
attendance_dev = []
previous_dev = []
final_dev = []

for i in range(len(final_score)):

    study_dev.append(study_hours[i] - avg_study)
    attendance_dev.append(attendance[i] - avg_attendance)
    previous_dev.append(previous_score[i] - avg_previous)
    final_dev.append(final_score[i] - avg_final)

study_numerator = 0
study_denominator = 0

attendance_numerator = 0
attendance_denominator = 0

previous_numerator = 0
previous_denominator = 0


for i in range(len(final_score)):

    study_numerator += study_dev[i] * final_dev[i]
    study_denominator += study_dev[i] * study_dev[i]

    attendance_numerator += attendance_dev[i] * final_dev[i]
    attendance_denominator += attendance_dev[i] * attendance_dev[i]

    previous_numerator += previous_dev[i] * final_dev[i]
    previous_denominator += previous_dev[i] * previous_dev[i]


study_coefficient = study_numerator / study_denominator

attendance_coefficient = (
    attendance_numerator / attendance_denominator
)

previous_coefficient = (
    previous_numerator / previous_denominator
)


intercept = (
    avg_final
    - study_coefficient * avg_study
    - attendance_coefficient * avg_attendance
    - previous_coefficient * avg_previous
)

print("\n======================================")
print(" STUDENT PERFORMANCE PREDICTION")
print("======================================")

print("\nPrediction Formula:")

print(
    "Final Score = "
    + str(round(intercept, 2))
    + " + "
    + str(round(study_coefficient, 2))
    + " × Study Hours + "
    + str(round(attendance_coefficient, 2))
    + " × Attendance + "
    + str(round(previous_coefficient, 2))
    + " × Previous Score"
)

print("\nEnter Student Details")
print("---------------------")

study = float(input("Study hours per day: "))

attend = float(
    input("Attendance percentage: ")
)

previous = float(
    input("Previous exam score: ")
)

prediction = (
    intercept
    + study_coefficient * study
    + attendance_coefficient * attend
    + previous_coefficient * previous
)
if prediction < 0:
    prediction = 0

if prediction > 100:
    prediction = 100

if prediction >= 90:

    category = "Excellent"

elif prediction >= 75:

    category = "Very Good"

elif prediction >= 60:

    category = "Good"

elif prediction >= 40:

    category = "Average"

else:

    category = "Needs Improvement"

print("\n======================================")
print(" PREDICTION RESULT")
print("======================================")

print(
    "Predicted Final Score:",
    round(prediction, 2)
)

print(
    "Performance:",
    category
)


if prediction >= 40:

    print("Result: PASS")

else:

    print("Result: FAIL")


print("======================================")