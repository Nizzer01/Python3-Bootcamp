

# Gets input from user note as string
# Also no user inout validation
print("How many kms did you cycle today?")
kms = input()
print("Ok, you said " + kms)


miles = float(kms) / 1.60934
miles = round(miles, 2)

print("That is {} miles".format(miles))
