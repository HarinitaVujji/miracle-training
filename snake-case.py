# Function using snake_case
def calculate_total_marks(math_marks, science_marks, english_marks):

    total_marks = math_marks + science_marks + english_marks
    average_marks = total_marks / 3

    print("Total Marks:", total_marks)
    print("Average Marks:", average_marks)


# Calling the function
calculate_total_marks(85, 90, 88)