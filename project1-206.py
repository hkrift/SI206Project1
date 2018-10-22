#Worked on this project with Molly Heller and Samantha Sherman.  We helped eachother when we got stuck on certain parts and we talked through how we were going to code it before we started.

import csv
import matplotlib.pyplot as plt
import os
import filecmp
from dateutil.relativedelta import *
from datetime import date

def getData(file):
	data = open(file, "r")
	listofdictionaries = []

	for line in data.readlines()[1:]:
		dictionary = {}

		values= line.split(",")
		first_name = values[0].strip()
		last_name = values[1].strip()
		email_address = values[2].strip()
		Class = values[3].strip()
		DOB = values[4].strip()

		dictionary["First"]= first_name
		dictionary["Last"]= last_name
		dictionary["Email"]= email_address
		dictionary["Class"]= Class
		dictionary["DOB"]= DOB

		listofdictionaries.append(dictionary)

	return listofdictionaries

def mySort(data, key):
	sorted_list = sorted(data, key = lambda x: x[key])
	new_list = []
	for x in sorted_list:
		new_list.append(x['First'] + " " + x['Last'])
	return new_list[0]

def classSizes(data):
	freshman = 0
	sophomore = 0
	junior = 0
	senior = 0

	for x in data:
		if x["Class"] == "Senior":
			senior = senior + 1
		if x["Class"] == "Junior":
			junior = junior + 1
		if x["Class"] == "Sophomore":
			sophomore = sophomore + 1
		if x["Class"] == "Freshman":
			freshman = freshman + 1

	classes = ["Senior", "Junior", "Sophomore", "Freshman"]
	class_size = [senior, junior, sophomore, freshman]
	class_list = (("Senior", senior), ("Junior", junior), ("Sophomore", sophomore),("Freshman", freshman))
	new_list = sorted(class_list, key = lambda x: x[-1], reverse = True)

	plt.bar(classes, class_size, label= "Class Distribution", color = "r")
	plt.show()

	return new_list

def findMonth(x):
	January = 0
	February = 0
	March = 0
	April = 0
	May = 0
	June = 0
	July = 0
	August = 0
	September = 0
	October = 0
	November = 0
	December = 0

	for student in x:
		if student["DOB"].split("/")[0] == "1":
			January = January + 1

		if student["DOB"].split("/")[0] == "2":
			February = February + 1

		if student["DOB"].split("/")[0] == "3":
			March = March + 1

		if student["DOB"].split("/")[0] == "4":
			April = April + 1

		if student["DOB"].split("/")[0] == "5":
			May = May + 1

		if student["DOB"].split("/")[0] == "6":
			June = June + 1

		if student["DOB"].split("/")[0] == "7":
			July = July + 1

		if student["DOB"].split("/")[0] == "8":
			August = August + 1

		if student["DOB"].split("/")[0] == "9":
			September = September + 1

		if student["DOB"].split("/")[0] == "10":
			October = October + 1

		if student["DOB"].split("/")[0] == "11":
			November = November + 1

		if student["DOB"].split("/")[0] == "12":
			December = December + 1

	months = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
	month_names = (January, February, March, April, May, June, July, August, September, October, November, December)
	month_distribution = list(zip(months, month_names))
	most_common_month = sorted(month_distribution, key= lambda x: x[-1], reverse= True)

	print(most_common_month)

	return most_common_month[0][0]

def mySortPrint(data, key, file):
	sortedlist = sorted(data, key= lambda x: x[key])
	new_list = []

	for x in sortedlist:
		new_list.append((x["First"].strip()+","+x["Last"].strip()+","+x["Email"].strip()+"\n"))

		final_file= open(file, "w")

		for x in new_list:
			final_file.write(x)

def findAge(data):
	list1 = []
	age = []

	for person in data:
		list1.append(person["DOB"])
		p = person["DOB"]
		x = p.split("/")

	list2 = []
	for x in list1:
		y = x.split("/")
	list2.append(y)

	for z in list2:
		if int(z[0]) < 10:
			age.append(2018 - int(z[2]))

		elif int(z[0]) > 10:
			age.append(2017 - int(z[2]))

		elif int(z[0]) == 10 and int(z[1]) <= 16:
			age.append(2018 - int(z[2]))

		elif int(z[0]) == 10 and int(z[1]) > 16:
			age.append(2017 - int(z[2]))

	total = 0

	for num in age:
		total = total + num
	print(total)
	average = total / len(age)

	return round(average)
	pass

################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it"s supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score

# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData("P1DataA.csv")
	data2 = getData("P1DataB2.csv")
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,"First"),"Abbot Le",25)
	total += test(mySort(data2,"First"),"Adam Rocha",25)

	print("First student sorted by Last name:")
	total += test(mySort(data,"Last"),"Elijah Adams",25)
	total += test(mySort(data2,"Last"),"Elijah Adams",25)

	print("First student sorted by Email:")
	total += test(mySort(data,"Email"),"Hope Craft",25)
	total += test(mySort(data2,"Email"),"Orli Humphrey",25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[("Junior", 28), ("Senior", 27), ("Freshman", 23), ("Sophomore", 22)],25)
	total += test(classSizes(data2),[("Senior", 26), ("Junior", 25), ("Freshman", 21), ("Sophomore", 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data, "Last", "results.csv")
	if os.path.exists("results.csv"):
		total += test(filecmp.cmp("outfile.csv", "results.csv"),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == "__main__":
	main()
