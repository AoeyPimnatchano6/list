#Program interface should have all of these:
#1. Tell the user what program is and what is cando
#2. Tell the user make choices or select option
#3. Let the user enter information -you should include a helpful message
#4. Display result or answer
#5. Let the user closethe program

teamlist = []
choice = ' '
while choice != 'X':
    print("TEAM MANAGER")
    print("===============")
    print("This program will help you mange your team")
    print("\n")
    print("A: Append a value")
    print("B: Print the team list")
    print("X: Exit the program")
    choice = input("Enter your choice: ")
    if choice = "A":
        name = input("Enter a name: ")
        teamlist.append(name)
print(teamlist)