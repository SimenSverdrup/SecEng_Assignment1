import hashlib
import binascii
import time

def hasNumber(inputString):
    return any(char.isdigit() for char in inputString)

def passwordCracker():

    usernames = []
    hashedPasswords = []
    commonPasswords = []
    crackedPasswords = []
    crackedUsers = []

    f = open("hashedPasswords.txt", "r")

    if f.mode == 'r':
        for x in f:
            users = x.split(":")
            usernames.append(users[1])
            hashedPasswords.append(users[2][:-1])
    f.close()

    i = open("10 000+ most common passwords.txt", "r")
    if i.mode == 'r':
        for y in i:
            if len(y) > 5 and hasNumber(y) and y not in commonPasswords:
                commonPasswords.append(y[:-1])
    i.close()

    index = 0

    #for hashedPassword in hashedPasswords:       #k elements
    for pw in commonPasswords:               #10 000 elements
        currentHash = hashlib.pbkdf2_hmac("sha1", bytes(pw, "utf-8"), b'seclab', 500, 16)
        currentHash = binascii.hexlify(currentHash).decode("utf-8")
        if currentHash in commonPasswords:
            crackedPasswords.append(pw)
            crackedUsers.append(usernames[index])
            print("Password cracked! Username: %s," % usernames[index], "Password: %s\n" % pw)

        else:
            print("No password match for username %s\n" % usernames[index])
            pass
        index += 1

    out = open("Passwords.txt", "w")
    index = 0

    if out.mode == 'w':
        for j in crackedPasswords:
            out.write(str(index + 1))
            out.write(":%s" % crackedUsers[index])
            out.write(":%s\n" % j)
            index += 1
    out.close()

start_time =  time.time()
passwordCracker()
print('time spent', time.time()-start_time)
