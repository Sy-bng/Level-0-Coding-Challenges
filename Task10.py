string1 = str("Bootcamp")
string2 = str("Learnership")
def common():
    s1 = set(string1)
    s2 = set(string2)
    common_letters = s1 & s2
    print(s1 & s2)

common() 
