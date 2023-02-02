# remove whitespace

import re

str ="吾輩は猫で  ある。名前はまだ   ない。どこで生れた  か頓（とん）と見当がつかぬ。"

### いくつかの書き方を紹介します ########################
# with regex
def remove2(s):
    s = re.sub(r"\s+", "", s)
    return s

print(remove2(str))

# Using split() and join() function
def remove(s):
    s = "".join(s.split(" "))
    return s

print(remove(str))

# Using translate() function
def remove3(s):

    # Using translate() function to remove whitespaces
    s = s.translate(s.maketrans('', '', ' '))
    return s

print(remove3(str))

# Using replace() Function
def remove4(s):
    # Using the replace function to remove whitespaces
    s = s.replace(" ", "")
    return s

print(remove4(str))