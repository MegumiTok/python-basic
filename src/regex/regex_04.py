import re

# \w
# Matches Unicode word characters

# +
# Causes the resulting RE to match 1 or more repetitions of the preceding RE. 
# ab+ will match ‘a’ followed by any non-zero number of ‘b’s; it will not match just ‘a’.

m1 = re.findall("\w+(?:\s|$)", "green pears")
print(m1) # ['green ', 'pears']


m2 = re.search('(?<=abc)Here', 'abcHere Here dfeHere')
print(m2.group(0)) # Here


m3 = re.split("(?<=。)", '吾輩は猫である。名前はまだない。')
print(m3) # ['吾輩は猫である。', '名前はまだない。', '']

m4 = re.split("(?<=。)(?=.)", '吾輩は猫である。名前はまだない。')
print(m4) # ['吾輩は猫である。', '名前はまだない。']