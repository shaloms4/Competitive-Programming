def split_and_join(line):
    string_list=line.split(" ")
    string_join="-".join(string_list)
    return string_join
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)