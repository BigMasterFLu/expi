# Name:Charlie Tessier
# Period: PM
# Student Performance Analyzer


# Program introduction
print("========================================")
print("       STUDENT PERFORMANCE ANALYZER")
print("========================================")
print()
print("Enter the student's information below.")
print()


# Get all of the student's information from the user
student_name = input("What is the student's name? ")
grade_level = int(input("What grade level is the student in? "))
assignment_average = float(input("What is the student's assignment average? "))
quiz_average = float(input("What is the student's quiz average? "))
test_average = float(input("What is the student's test average? "))
attendance = float(input("What is the student's attendance percentage? "))
missing_assignments = int(input("How many missing assignments does the student have? "))
print()


# Calculate the overall grade using weights: assignments 30%, quizzes 30%, tests 40%
def calculate_grade(assignment_average, quiz_average, test_average):
    assignment_portion = assignment_average * 0.30
    quiz_portion = quiz_average * 0.30
    test_portion = test_average * 0.40
    overall_grade = assignment_portion + quiz_portion + test_portion
    print("Overall Grade:", overall_grade)
    return overall_grade


# Decide the letter grade that matches the overall grade
def letter_grade(overall_grade):
    if overall_grade >= 90:
        print("Letter Grade: A")
    elif overall_grade >= 80:
        print("Letter Grade: B")
    elif overall_grade >= 70:
        print("Letter Grade: C")
    elif overall_grade >= 60:
        print("Letter Grade: D")
    else:
        print("Letter Grade: F")


# Decide how good the student's attendance is
def attendance_status(attendance):
    if attendance >= 95:
        print("Attendance Status: Excellent Attendance")
    elif attendance >= 90:
        print("Attendance Status: Good Attendance")
    elif attendance >= 80:
        print("Attendance Status: Attendance Warning")
    else:
        print("Attendance Status: Poor Attendance")


# Decide how serious the student's missing assignments are
def assignment_status(missing_assignments):
    if missing_assignments == 0:
        print("Missing Assignment Status: Excellent")
    elif missing_assignments <= 2:
        print("Missing Assignment Status: Good")
    elif missing_assignments <= 4:
        print("Missing Assignment Status: Warning")
    else:
        print("Missing Assignment Status: Critical")


# Check academic eligibility with nested conditionals (no "and" or "or" allowed here)
def check_eligibility(overall_grade, attendance, missing_assignments):
    if overall_grade >= 70:

        if attendance >= 90:

            if missing_assignments <= 2:
                print("Academic Eligibility: ELIGIBLE")
                print("Student passed all three requirements.")
            else:
                print("Academic Eligibility: NOT ELIGIBLE")
                print("Reason: Too many missing assignments.")

        else:
            print("Academic Eligibility: NOT ELIGIBLE")
            print("Reason: Attendance is too low.")

    else:
        print("Academic Eligibility: NOT ELIGIBLE")
        print("Reason: Overall grade is too low.")


# Check High Honors with three levels of nested conditionals (no "and" or "or" allowed here)
def check_high_honors(overall_grade, attendance, missing_assignments):
    if overall_grade >= 90:

        if attendance >= 95:

            if missing_assignments == 0:
                print("High Honors: YES")
            else:
                print("High Honors: NO")
                print("Reason: Student has missing assignments.")

        else:
            print("High Honors: NO")
            print("Reason: Attendance requirement not met.")

    else:
        print("High Honors: NO")
        print("Reason: Grade requirement not met.")


# Check good standing using "and" (both requirements must be true)
def check_good_standing(overall_grade, attendance):
    if overall_grade >= 70 and attendance >= 90:
        print("Good Standing: YES")
    else:
        print("Good Standing: NO")


# Check whether extra academic support is needed using "or" (either problem counts)
def check_support(overall_grade, attendance):
    if overall_grade < 70 or attendance < 80:
        print("Additional Support: RECOMMENDED")
    else:
        print("Additional Support: NOT NEEDED")


# Display a message that matches the student's grade level
def grade_level_message(grade_level):
    if grade_level == 9:
        print("Welcome to your freshman year!")
    elif grade_level == 10:
        print("Keep building your skills!")
    elif grade_level == 11:
        print("Junior year - keep pushing!")
    elif grade_level == 12:
        print("Senior year - finish strong!")
    else:
        print("Invalid grade level.")


# Compare the three averages to find the student's strongest category
def strongest_category(assignment_average, quiz_average, test_average):
    if assignment_average >= quiz_average:

        if assignment_average >= test_average:
            print("Strongest Category: Assignments")
        else:
            print("Strongest Category: Tests")

    else:

        if quiz_average >= test_average:
            print("Strongest Category: Quizzes")
        else:
            print("Strongest Category: Tests")


# EXTRA CREDIT: combine "and" with "or" to find outstanding students
def check_advanced_status(overall_grade, attendance, missing_assignments):
    if overall_grade >= 90 and attendance >= 95 or overall_grade >= 85 and missing_assignments == 0:
        print("Advanced Status: OUTSTANDING STUDENT")
    else:
        print("Advanced Status: STANDARD STUDENT STATUS")


# Call the functions using the student's information as arguments
overall_grade = calculate_grade(assignment_average, quiz_average, test_average)
letter_grade(overall_grade)
attendance_status(attendance)
assignment_status(missing_assignments)
print()

check_eligibility(overall_grade, attendance, missing_assignments)
print()

check_high_honors(overall_grade, attendance, missing_assignments)
print()

check_good_standing(overall_grade, attendance)
check_support(overall_grade, attendance)
print()

grade_level_message(grade_level)
strongest_category(assignment_average, quiz_average, test_average)
print()


# Student login simulation using nested conditionals (no "and" or "or" allowed here)
username = input("Enter username: ")
pin = input("Enter PIN: ")

if username == "student":

    if pin == "1234":
        print("Login Successful!")
    else:
        print("Login Failed: Incorrect PIN.")

else:
    print("Login Failed: Incorrect username.")
print()


# Print an organized summary of everything the user entered
print("========================================")
print("            STUDENT SUMMARY")
print("========================================")
print()
print("Student:", student_name)
print("Grade Level:", grade_level)
print()
print("Assignment Average:", assignment_average)
print("Quiz Average:", quiz_average)
print("Test Average:", test_average)
print()
print("Overall Grade:", overall_grade)
print("Attendance:", attendance)
print("Missing Assignments:", missing_assignments)
print()
check_advanced_status(overall_grade, attendance, missing_assignments)
print()
print("========================================")
