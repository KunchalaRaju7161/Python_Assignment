class StringClass:
    def __init__(self, user_input):
        self.user_input = user_input

    def get_length(self):
        return len(self.user_input)

    def convert_to_list(self, string_to_list):
        return list(string_to_list)


Company_name = "HashedIn"
my_string = StringClass(Company_name)
length = my_string.get_length()
print("My string length is : ", length)
convert_list = my_string.convert_to_list(Company_name)
print("My string converted into list : ", convert_list)
