#Assume that several IITs start offering online degrees across multiple branches. The email-id of a student is defined as follows:
#branch_degree_year_roll@student.onlinedegree.institute.ac.in
#For example, if the email-id is CS_BT_21_7412@student.onlinedegree.iitm.ac.in, then this student is from the computer science branch, pursuing a BTech degree from IITM, starting from the year 2021, with 7412 as the roll number. branch, degree and year are codes of length two, while roll and institute are codes of length four. Accept a student's email-id as input and print the following details, one item on each line:
#(1)Branch
#(2) Degree
#(3) Year
#(4) Roll number
#(5) Institute

email = input()
print(email[0:2])
print(email[3:5])
print(email[6:8])
print(email[9:13])
print(email[35:39])
