#ed = Email addresses Directory

ed = { 'Kyle Cheung' : 'hello@kylezoa.com',
       'Tekin Ozbek' : 'tekin@tekinozbek.net',
       'Robo Balasko' : 'robo.balasko@gmail.com',
       'spamzorz' : 'ICANHAZTEHLULZ@4chan.org'
     }

nameForEmail = input('Which email would you like? Please type name: ')

#print my email
print(nameForEmail + "'s email is" , ed['nameForEmail'])

#delete the spamzorz

print("The spammer's email is", ed['spamzorz'])
del ed['spamzorz']

print('There are {0} amount of emails in the directory.'.format(len(ed)))

print('These are all the emails in the directory:', end=' ')

print('All the emails in the directory are:', ed[0:3])