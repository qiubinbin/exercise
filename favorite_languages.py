from collections import OrderedDict
favorite_languages=OrderedDict()
favorite_languages['jen']='pyhton'
favorite_languages['sarah']='c'
favorite_languages['job']='java'
favorite_languages['phil']='c++'
for name,language in favorite_languages.items():
	print(name.title()+"'s favorite language is "+language.title()+'.')
