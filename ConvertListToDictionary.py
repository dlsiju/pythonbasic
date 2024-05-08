# Convert list into dicitonary

languages = ['Python', 'Java', 'c#']
versions = [3, 22, 12]
dictionary = dict(zip(languages, versions))
print('converted dictionary=', dictionary)
print('dictionary[Python]=', dictionary['Python'])
print('dictionary[Java]=', dictionary['Java'])
print('dictionary[c#]=', dictionary['c#'])
