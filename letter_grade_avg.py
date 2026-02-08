# letter_grade_avg.py
# Accepts 4 letters then drops the lower and averages the remaining 3

from grade_compute import gradeToNumber, numberToGrade

def processLine(line):
    """
    Splits inputs, checks grades, and converts to numbers
    """
    grades = [g.strip().upper() for g in line.split("$")]

    if len(grades) != 4:
        return None, None
    
    nums = [gradeToNumber(g) for g in grades]
    return grades, nums

def dropLowest(nums):
    """
    Removes and returns the lowest grade
    """
    lowest = min(nums)
    nums.remove(lowest)
    return lowest

def calcAvg(nums):
    """
    Calculates the average of the 3 remaining grades
    Adds a curve if all remaining is less than or equal to B-
    """

    avg = sum(nums) / 3

    if all(x <= gradeToNumber("B-") for x in nums):
        avg += 0.25

    return avg

def printResult(grades, lowest_num, avg):
    """
    Prints ASCII summary
    """

    lowest_letter = numberToGrade(lowest_num)
    final_letter = numberToGrade(avg)

    width = 38  # inside width of the box

    print("+" + "-" * width + "+")
    print("|" + f"Grades Entered: {', '.join(grades)}".ljust(width) + "|")
    print("|" + f"Lowest Grade Dropped: {lowest_letter}".ljust(width) + "|")
    print("|" + f"Calculated Average: {avg:.2f}".ljust(width) + "|")
    print("|" + f"Final Letter Grade: {final_letter}".ljust(width) + "|")
    print("+" + "-" * width + "+")

def main():
    """
    Main function to run the grade averaging process
    """
    
    while True:
        line = input("Enter 4 letter grades separated by $ (or Q to quit): ")

        # quit condition
        if line.strip().upper() == "Q":
            print("Exiting program.")
            break
        
        grades, nums = processLine(line)

        # invalid input check
        if grades is None:
            print("Invalid input. Please enter exactly 4 letter grades.")
            continue
        
        lowest = dropLowest(nums)
        avg = calcAvg(nums)
        printResult(grades, lowest, avg)

main()
