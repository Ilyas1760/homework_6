my_dict = {'Ilyas':2002, 'Artem':1917,'Roma':1861}
print(my_dict['Roma'])
print(my_dict.get('Viktor'))
my_dict.update({'Ivan':1990,
                'Liza':1945})
list=my_dict
print(list.pop('Ilyas'))
print(my_dict)


my_set={5,20,'картина',20,'дерево',5}
print(my_set)
my_set.add(33)
my_set.add('лицо')
print(my_set)
(my_set.discard('картина'))
print(my_set)