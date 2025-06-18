# assignment5
# Task1
This Python script uses a dictionary to store student names along with their marks. The user can input a student's name, and the script will return their corresponding marks if found.
 # Features
 - Stores student names and their marks in a dictionary
- Accepts user input to search for a specific student
- Displays the marks if the student exists in the dictionary
- Informs the user if the student is not found
 # Code
 dictionary={ 
       "Jahanvi":34,
       "Neeraj":45,
       "Dheeraj":56,
       "Bharat":78,
       "Pragya":46,
       "Ragini":90,
       "Daksh":59,
       "Rajendra":60
       }

students_name= input("Enter the student's name:")
if students_name in dictionary:
  print(f"{students_name}'s marks : {dictionary[students_name]}")
else:
  print("student not found")

# Task 2
This Python script demonstrates how to perform basic list operations, including slicing and reversing. It extracts the first five elements from a list of numbers and then reverses the extracted sublist.
 # Features
1. Initializes a list of numbers from 1 to 10.
2. Extracts the first five elements using list slicing.
3. Reverses the extracted sublist.
4. Prints the original list, the sliced list, and the reversed list.
 # Code
 numbers=[1,2,3,4,5,6,7,8,9,10]
print(f"Original list :{numbers}")
extracted_numbers = numbers[0:5]
print(f"Extracted first five elements: {extracted_numbers}")
extracted_numbers.reverse()
print(f"Reversed extracted elements:{extracted_numbers}")
