# Define a dictionary that contains information about several members of your family. Use the following example as a template.

my_family = {
    'sister': {
        'name': 'Meredith',
        'age': 28
    },
    'cousin': {
        'name': 'Chris',
        'age': 28
    }
}

# Using a dictionary comprehension, produce output that looks like the following example.

family_stuff = {f'{values["name"]} is my {family_member} and is {str(values["age"])} years old' for family_member, values in my_family.items()}

print(family_stuff)
