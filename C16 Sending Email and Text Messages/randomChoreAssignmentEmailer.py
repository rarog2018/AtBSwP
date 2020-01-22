#! python3
# program that sends emails with chores that need to be done to peole from 
# the list, 
# use: just run the program without arguments, or with one command line argument
# that contains .txt file with email addresses each in new line
# the chores can be edited in chores.txt file (each in new line as well)

# load the email addresses from the .txt file or from the emailAs.json file
# load the chores from the chores.txt file
# prompt for the email and password
# setup the connection
# generate the random chore
# check if the chore is already assigned to the email
# send the email with the chore
# repeat last three untill all the emails get chores or all the chores are used

import json, random, smtplib, sys

emailList = []
assignments = {}
SMTPsdn = {"gmail.com" : ['smtp.gmail.com', 587], "op.pl" : ['smtp.poczta.onet.pl', '587'],
            "outlook.com" : ['smtp-mail.outlook.com', 587], "att.net" : ['mpt.mail.att.net', 465]}

# load the email addresses from the .txt file or from the email.json file
# if there was a command line argument provided load them from .txt file
if len(sys.argv) > 1:
    # try to open the file
    try:
        emailFile = open(sys.argv[1], 'r')
    except Exception as err:
        print(err)
        sys.exit(1)

    # try to read the file
    try:
        for line in emailFile.readlines():
            emailList.append(line.rstrip())
        emailFile.close()
    except Exception as err:
        print(err)
        sys.exit(2)

    # check if emailList is empty
    if emailList == []:
        print("The email list is empty")
        sys.exit(3)

    # update the dictionary
    for email in emailList:
        assignments[email] = ""

# load the data from the emailAs.json file
else:
    # try to load the data from the file
    try:
        eAsF = open('emailAs.json', 'r')
        assignments = json.load(eAsF)
    except Exception as err:
        print(err)
        sys.exit(12)

    # load emails to the list
    for email in assignments.keys():
        emailList.append(email)

########## MAIN CODE #####################
# load the chores from the chores.txt file
choreList = [] 

# try to open the file
try:
    choreFile = open('chores.txt', 'r')
except Exception as err:
    print("It is essential to provide chores in chores.txt file\n" + str(err))
    sys.exit(4)

# try to read the file
try:
    for chore in choreFile.readlines():
        choreList.append(chore.rstrip())
    choreFile.close()
except Exception as err:
    print(err)
    sys.exit(5)

# check if choreList is empty
if choreList == []:
    print("chore list is empty")
    sys.exit(6)

# prompt for the email and password
myEmail = input("Type your email address: ")

# setup the connection
# check if the email address is correct
try:
    SMTPdata = SMTPsdn[myEmail.split('@')[1]]
except Exception as err:
    print("Unknown email server domain" + str(err))
    sys.exit(7)

# connect  to the smtp server
try:
    smtpObj = smtplib.SMTP(SMTPdata[0], SMTPdata[1])
except Exception as err:
    print(err)
    sys.exit(8)

# prompt for the email and password
password = input("Type your password: ")

# login to your email
try:
    smtpObj.login(myEmail, password)
except Exception as err:
    print(err)
    sys.exit(9)

# repeat untill all the emails get chores or all the chores are used
for email in emailList:
    if choreList != []:
        flag = True
        while flag:
            chore = random.choice(choreList)    # generate the random chore
            # check if the chore is already assigned to the email
            if assignments[email] != chore:
                # if the chore is different then assign it
                assignments[email] = chore
                choreList.remove(chore) # remove the chore from the choreList
                flag = False    # reset the flag

                # send the email with the chore
                print("Sending %s to %s..." % (chore, email))
                smtpObj.sendmail(myEmail, email, 'Subject: Chore for You\n%s' \
                    % (assignments[email]))
            # if there is more than one element in the list repeat while loop
            elif len(choreList) > 1:
                continue
            # if there is only one element in the list there is nothing else to
            # pick, so do not assign this chore to the email
            else:
                assignments[email] = ""
                print("Sending free week message to %s" % (email))
                smtpObj.sendmail(myEmail, email, 'Subject: Free week for You\n:)')
                flag = False

    # if chore list is empty other people have free week
    else:
        assignments[email] = ""
        print("Sending free week message to %s" % (email))
        smtpObj.sendmail(myEmail, email, 'Subject: Free week for You\n:)')

# disconnect from the SMTP server
try:
    smtpObj.quit()
except Exception as err:
    print(err)
    sys.exit(10)

# save the chores to the file
try:
    emailAsFile = open('emailAs.json', 'w')
    json.dump(assignments, emailAsFile)
    emailAsFile.close()
except Exception as err:
    print(err)
    sys.exit(11)

print('Done')
