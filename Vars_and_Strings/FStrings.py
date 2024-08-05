# Set the variable called first  to your first name.
#
# Set the variable called last  to your last name.
#
# Then set the variable called formatted  to a new string that interpolates both values
# (from the first and last variables) using f-strings or the .format()  method.
# Make sure you follow this exact pattern for the new string that you store to the formatted variable
# (pay attention to capital/lowercase letters, spaces, commas, etc):

# "First Name: Colt, Last Name: Steele"


first = None
last = None

formatted = None
formatted2 = None

first = "Rouge"
last = "Trooper"

formatted = f"First Name: {first}, Last Name: {last}"
print(formatted)

formatted2 = "First Name: {}, Last Name: {}".format(first, last)
print(formatted2)