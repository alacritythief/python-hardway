query = True
entries = []

while query == True:
    if len(entries) == 5:
        query = False
    else:
        add = raw_input('Enter a number: ')
        entries.append(add)

print entries

for x in entries:
    print x
