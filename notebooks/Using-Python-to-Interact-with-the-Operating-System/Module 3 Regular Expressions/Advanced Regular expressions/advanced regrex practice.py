"""function to rearrange names using regular expressions"""

import re
def rearrange_name(name):
    result = re.search(r"^(\w*), ([\w \.]*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])

print(rearrange_name("Rahman, Lubna"))
print(rearrange_name("Lubna Rahman"))
print(rearrange_name("Rahman, Lubna Z."))
