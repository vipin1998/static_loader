
def fun(str):
    words = 0;
    chars = 0;
    lines = 0;
    with open(str) as f:
        for line in f:
            lines = lines + 1
            line = line.split()
            words = words + len(line)
            for item in line:
                chars = chars + len(item)
    print(str)
    print("lines ",lines);
    print("words ",words);
    print("chars ",chars);

with open("input.txt") as f:
    for line in f:
        line = line.split()
        for item in line:
            if item.startswith('load'):
                item = item[6:] #remove First six character of string
                item = item[:-3] #remove last three character of string
                fun(item)
