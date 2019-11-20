def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])

assert count_upper_case("") == 0, "Empty String"
assert count_upper_case("All is") == 1, "One Upper Case"
assert count_upper_case("all") == 0, "One lower case"
assert count_upper_case("+") == 0, "One special carachter"

assert count_upper_case("All Akk") == 2, "Empty String 2"
assert count_upper_case("AkAk") == 2, "One lower case  2"

print("all test past")
