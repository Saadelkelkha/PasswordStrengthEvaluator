# Function to count the number of lowercase letters in the password
def NbCMin(p):
    n = 0
    for i in range(len(p)):
        if ord("a") <= ord(p[i]) <= ord("z"):
            n = n + 1
    return n

# Function to count the number of uppercase letters in the password
def NbCMaj(p):
    j = 0
    for i in range(len(p)):
        if ord("A") <= ord(p[i]) <= ord("Z"):
            j += 1
    return j

# Function to count the number of non-alphabetic characters in the password
def NbCAlpha(p):
    a = 0
    for i in range(len(p)):
        if not(ord("A") <= ord(p[i]) <= ord("Z")) and (not(ord("a") <= ord(p[i]) <= ord("z"))):
            a += 1
    return a

# Function to find the length of the longest sequence of uppercase letters in the password
def LongMaj(p):
    o = 0
    k = 0
    for i in range(len(p)):
        if ord("A") <= ord(p[i]) <= ord("Z"):
            o += 1
        else:
            o = 0
        if k < o:
            k = o
    return k

# Function to find the length of the longest sequence of lowercase letters in the password
def LongMin(p):
    t = 0
    y = 0
    for i in range(len(p)):
        if ord("a") <= ord(p[i]) <= ord("z"):
            t += 1
        else:
            t = 0
        if y < t:
            y = t
    return y

# Function to calculate the password strength score
def score(p):
    s = len(p) * 4 + (len(p) - NbCMin(p)) * 3 + (len(p) - NbCMaj(p)) * 2 + NbCAlpha(p) * 5 - LongMin(p) * 2 - LongMaj(p) * 2
    return s

# User input for the password
p = input("Type password: ")

# Calculate the password strength score
s = score(p)

# Determine the strength category based on the score
if s < 20:
    print("Very Weak")
elif 20 <= s < 40:
    print("Weak")
elif 40 <= s < 80:
    print("Strong")
else:
    print("Very Strong")
