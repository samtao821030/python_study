def ups(line):
    for sub in line.split(','):
        yield sub.upper()

print(list(enumerate(ups('aaa,bbb,ccc'))))