students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def names():
    for key in students:
        print key["first_name"], key["last_name"]

names()

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }



def stu_inst():
    count = 0
    print 
    for i in users:
        print i
        for key in users[i]:
            count += 1
            a = len(key['first_name']) + len(key["last_name"])
            print count, "-", key["first_name"].upper(), key["last_name"].upper(), "-", a


stu_inst()
     


