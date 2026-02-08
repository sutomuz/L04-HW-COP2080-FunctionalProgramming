#grade_compute.py
# Functions to convert between letter grades and numbers

def gradeToNumber(grade):
    """
    Converts letter grades to GPA number
    Modifies + and -
    """
    grade = grade.upper()

    if grade[0] == "A":
        num = 4.0
    elif grade[0] == "B":
        num = 3.0
    elif grade[0] == "C":
        num = 2.0
    elif grade[0] == "D":
        num = 1.0
    else:
        num = 0.0

    # modifier
    if len(grade) == 2:
        if grade[1] == "+":
            num = num + 0.3
        elif grade[1] == "-":
            num = num - 0.3
    
    return num
    
def numberToGrade(num):
    """
    Converts GPA number back to a letter grade
    """
    if num >= 3.85:
        return "A"
    elif num >= 3.50:
        return "A-"
    elif num >= 3.15:
        return "B+"
    elif num >= 2.85:
        return "B"
    elif num >= 2.50:
        return "B-"
    elif num >= 2.15:
        return "C+"
    elif num >= 1.85:
        return "C"
    elif num >= 1.50:
        return "C-"
    elif num >= 1.15:
        return "D+"
    elif num >= 0.85:
        return "D"
    elif num >= 0.50:
        return "D-"
    else:
        return "F"