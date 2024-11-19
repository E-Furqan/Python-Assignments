import re

def DataValidation(value, data_type):
    if data_type == "integer":
        try:
            int(value)
            return True
        except ValueError:
            return False
    elif data_type == "float":
        try:
            float(value)
            return True
        except ValueError:
            return False
    elif data_type == "email":
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(email_regex, value))
    else:
        return False  


def main():
    value1 = "5"
    data_type1 = "integer"
    print(DataValidation(value1, data_type1))  

    value2 = "user@example.com"
    data_type2 = "email"
    print(DataValidation(value2, data_type2))  

    value3 = "5.67"
    data_type3 = "float"
    print(DataValidation(value3, data_type3))  

    value4 = "invalid-email"
    data_type4 = "email"
    print(DataValidation(value4, data_type4))  


if __name__=="__main__":
    main()
