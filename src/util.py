def get_int(input_str: str, error_str: str = "Please Enter a Number!"):
    while True:
        try:
            return int(input(input_str))
        except ValueError:
            print(error_str)
