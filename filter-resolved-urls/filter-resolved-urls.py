import re,sys

str0=str(sys.stdin.read())
str1=re.search('(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]', str0)

if str1 is not None:
    print(str1.group(0))
