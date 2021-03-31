# # Try it for yourself

# Given a list of users, create a function to find the user with a user_id of 4.


# ### Task:
# Write a solution to the above task and then submit it as a new github repo. 

users = [
  { "user_id": 1, "first_name": "Margaret", "last_name": "Chicken" },
  { "user_id": 2, "first_name": "Bill", "last_name": "Gates" },
  { "user_id": 3, "first_name": "Steve", "last_name": "Jobs" },
  { "user_id": 4, "first_name": "Guido", "last_name": "van Rossum" },
  { "user_id": 5, "first_name": "Brendan", "last_name": "Eich" },
]

def user_finder(list, id):
    for user in users:
        if user["user_id"] == id:
            user_id = user["user_id"]
            firstname = user["first_name"]
            lastname = user["last_name"]
            return f"user {user_id} has been found, their name is {firstname} {lastname}"
    return f"ID: {id} has no name association in our database, please check your typing"

user_id_for_searching = input("What is your user ID? ")
try:
    int_conversion_of_input = int(user_id_for_searching)
    print(user_finder(users, int_conversion_of_input))
except:
    print("Please type a number as your input for user ID")