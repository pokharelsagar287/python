#pre-defined usernames and passwords

users = {
    "sagar": "sagar123",
    "admin": "admin123",
    "user": "user123",
    "test": "test123"
}

max_attempts = 3
attempts = 0

while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print("Login successful!")
        break
    else:
        print("Invalid username or password. Please try again.")
        attempts += 1
if attempts == max_attempts:
    print("Maximum login attempts reached. Please try again later.")
   
   
