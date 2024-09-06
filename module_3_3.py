values_list = ('ААА', 'Hello', False)
values_dict = {'a': 55, 'b': 'world', 'c': True}
values_list_2 = (34, 'double')


def print_params(a=1, b='строка', c=True):
    print(a, b, c)



print_params(b=25)
print_params(c=[1, 2, 3])
print_params(**values_dict)
print_params(*values_list)

print_params(*values_list_2, 42)
