import re

text = "20d30s500m-10r10"

pattern = re.compile(r'(\d+)([dsmr]-?\d+)*')

matches = pattern.finditer(text)

print(matches)



first_match = entry.group(0)

print(first_match)
# first_match = matches[0]

# print(first_match)

# rollstring = first_match.group(0)

# print(rollstring)