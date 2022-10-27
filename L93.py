#The authors' names are: Julia, Julia, and Christina

#Find and Remove
string = "SPAM!HelloSPAM! worldSPAM!!"
output = []
index = 0
while index < len(string):
    if string[index:index+5] == "SPAM!" :
        index += 5
    else:
        output.append(string[index])
        index += 1
print("".join(output))

def remove_substring(string, substring):
    output= []
    index = 0
    while index < len(string):
        if string[index:index+len(substring)] == substring :
            index += len(substring)
        else:
            output.append(string[index])
            index += 1
    print("".join(output))
remove_substring("Ice Ice Baby, Ice Ice Baby", "Baby")
