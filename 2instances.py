from userinputvalidator import UserInputValidator


validator1 = UserInputValidator()
validator2 = UserInputValidator()

inputs1 = ["10", "abc", "-5", "0", "25", "42"]
inputs2 = ["5", "15", "25", "0", "xyz"]

# Validate and display results using validator1
valid_integers1 = validator1.validate_positive_integers(inputs1)
validator1.display_validation_message()
print(f"Validator 1 - Valid Integers: {valid_integers1}")

# Validate and display results using validator2
valid_integers2 = validator2.validate_positive_integers(inputs2)
validator2.display_validation_message()
print(f"Validator 2 - Valid Integers: {valid_integers2}")