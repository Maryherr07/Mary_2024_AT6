class UserInputValidator:
    def validate_positive_integers(self, inputs):
        """
        Validates a list of strings to check for positive integers.
        Returns a list of valid positive integers.
        """
        valid_integers = []
        for input_str in inputs:
            if input_str.isdigit() and int(input_str) > 0:
                valid_integers.append(int(input_str))
        return valid_integers
        pass