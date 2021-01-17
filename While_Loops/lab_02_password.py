user_name = input()
password = input()

while True:
    current_password = input()
    if password == current_password:
        print(f'Welcome {user_name}!')
        break
