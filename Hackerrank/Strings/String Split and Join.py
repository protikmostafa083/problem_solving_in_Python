def split_and_join(line):
    # write your code here
    line = line.split(' ') # converting into a list
    return "-".join(line)
    

if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result
