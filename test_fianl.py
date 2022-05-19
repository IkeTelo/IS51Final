# Laymen's Terms
"""
The program displays three main functions;
the number of grades, the class average, and the % of grades > average.

using the "Final.txt" file we;
first open print the total number of grades = "num_grades" found on the file
add up the sum of all "grades" found in file
by dividing the sum of "grades" by the "num_grades" we get "class_avg"
print class average "class_avg" to user
using the "class_avg" the program can then output the % of grades that are > average

the functions will output the number of grades
then loop through the scores and output a class average
and finaly, loop and output the % of all grades that are > average
"""
# Pseudo-code
"""
def main():
    file = open("Final.txt", 'r')
    data = files.read
    nums = data.split()
    print("Number of grades: ", len(nums))
then
    infile = open("Final.txt", 'r')
    total = 0
    nums = 0
    line = float(infile.readline())
    while line != "":
        nums += 1
        total += float(line)
        line = infile.readline()
        class_avg = total / nums
    print("The class average is: ", clas_avg)
finally
def calculate_percent_above_avg(nums, class_avg):
    above_avg = 0
    length = len(nums)
    for index in range (length):
        if nunbers[index] > class_avg:
            above_avg = above_avg +1
    return above_avg / length

calculate_percent_above_avg()
main()

"""