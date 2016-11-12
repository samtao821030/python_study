import re
match = re.match('Hello[\t]*(.*)world','Hello   Python world')
match.group(1)