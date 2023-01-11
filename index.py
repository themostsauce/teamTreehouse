from distutils.command.build_scripts import first_line_re


first_name = input("What is your first name? ")
print("Hello,", first_name)
if first_name == "Wathiq":
    print(first_name, "is learning Python")
elif first_name == "Floss Pick":
    print(first_name, "is learning with other studnets. Good job {}".format(first_name))
else:
    # This is just in case we have a younger user who can't yet read
    age = int(input("How old are you? "))
    if age <= 6:
        print("Wow! You're {}! If you're confident with your reading already...".format(age))
    print("Booooo {}".format(first_name))
print("Have a great day, {}!".format(first_name))