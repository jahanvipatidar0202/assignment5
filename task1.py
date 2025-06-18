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