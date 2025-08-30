# Mini Login System in Python

username = "Yousef"
password = "1234"

attempts = 0
max_attempts = 3
access = False

while attempts < max_attempts:
    u_input = input("Enter username: ")
    p_input = input("Enter password: ")

    if u_input == username and p_input == password:
        print("Login Successful! Welcome,", username)
        access = True
        break
    else:
        attempts += 1
        left = max_attempts - attempts
        if left > 0:
            print(f" Invalid login! You have {left} attempt(s) left.")

if not access:
    print(" Access Denied! Too many failed attempts.")