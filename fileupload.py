import leancloud

leancloud.init("Yf3MSyqMdVjhofKx5vflC4eF-MdYXbMMI","n63Ne1Jj2bs17yGUPzSuYq7K")

Person = leancloud.Object.extend('Person')

with open('testfile.jpg', 'rb') as f:
	file = leancloud.File('testfile.jpg',f)
	file.save()

D = Person()
D.set('Name','Unknown')
D.set('Profile',file)
D.save()