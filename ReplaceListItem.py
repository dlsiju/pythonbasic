# 2.Replace list’s item Python with .Net in the following list

languages = ['Java', 'Python', 'JavaScript']
print('languages list=', languages)
index = 0;
check = lambda x: list(map(lambda xx: xx.lower(), languages)).index(x)
try:
    existingLanguage = input('enter the language that you want to remove')
    index = check(existingLanguage.lower())
    newLanguage = input('enter new language to add')
    languages[index] = newLanguage
    print('languages list after replace=', languages)

except:
    print('language', existingLanguage, ' not found on list')
