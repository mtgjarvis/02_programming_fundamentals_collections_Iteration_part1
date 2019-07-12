fav_colours = ['blue', 'brown', 'black', 'grey']
fam_age = [40, 42, 45, 7, 33, 30]
coin_flip = ['heads', 'tails', 'heads', 'tails', 'tails', 'heads']
fav_artists = ['Leonard Cohen', 'Dylan', 'LCD Sound System']

fav_words = {
    'Obliterate': 'destroy utterly', 
    'Discomblobluated': 'confused and disconcerted', 
    'Sublime': 'of such excellence, grandeur, or beauty as to inspire great admiration or awe'
    }
fav_movies = {
    'Arrival': 2016, 
    'No Country For Old Men': 2007, 
    'Django Unchained': 2012
    }
cities = {
    'Paris': 2141000, 
    'New York': 8623000, 
    'Toronto': 2930000
    }
friends_fam = {'Holly': 40, 'Tracey': 42, 'Katie': 38, 'Sean': 37, 'Vincent': 44, 'Mike': 45}

print(coin_flip)
print(fav_colours[0])

sorted(friends_fam)
for key, val in friends_fam.items():
    print(f'{key} is {val} old')


friends_fam.update({'Baby': 0})

print(fav_movies.get("Arrival"))

print(fav_colours[-1])

cities['Halifax'] =  431000

coin_flip.reverse()
print(coin_flip)

print(cities.get("Paris"))

for name in fav_artists:
    print(f'I think {name} is great.')

print(fav_artists[0: 2])

for key, value in fav_movies.items():
    print(f'{key} cam out in {value}')

# print("-----")
# friends_fam2 = sorted(friends_fam.items(), reverse=True, key = lambda x: x[1])
# print(friends_fam2)

friends_fam_list = sorted(friends_fam.values(), reverse=True)
print(friends_fam_list)

fav_movies['Beauty and the Beast'] = [1999, 2017]
print(fav_movies)

for key, val in friends_fam.items():
    if val < 40:
        print(f'{key} is under 40')

print(max(friends_fam_list))

print(coin_flip.count('heads'))

fav_artists.remove('Dylan')

# removes 1 from the value of Halifax
cities['Halifax'] -= 1

# adds all the values together
print(sum(cities.values()))

# prints message if value is above or below a certain age
for key, val in friends_fam.items():
    if val >= 41:
        print(f'{key} is old.')
    else:
        print(f'{key} is young.')

# printed the last 2 items in the list
print(fav_colours[-2:])

# added 1 year to every key's value
for val in friends_fam:
    friends_fam[val] += 1
print(friends_fam)

# added 2 colors
fav_colours.extend(['Green', 'Purple'])

# added dictionary with nested lists
movies_year = {
    '1999': ['The Matrix', 'Star Wars: Episode 1', 'The Mummy'],
    '2009': ['Avatar', 'Star Trek', 'District 9'],
    '2019': ['How to Train Your Dragon 3', 'Toy Story 4', 'Star Wars: Episode 9']
}
# added list with nested lists
phone_buttons = [
    [1, 2, 3],
    [4, 5, 6],
    ['*', 0, '#']
]

# created a list with a dict and list nested
countries = [
    {'name': 'Canada', 'continent': 'North America', 'island': 'No'},
    {'name': 'USA', 'continent': 'North America', 'island': 'No'},
    {'name': 'Australia', 'continent': 'Australia', 'island': 'Yes'}
]

# printed the string 20 times
print("I will not skateboard in the halls" * 20)

# created a list with the string repeated 20 times
skateboard_20 = ["I will not skateboard in the halls" *20]

# created list using range
num_list = list(range(1, 51))
print(num_list)

# sums all the number in num_list
new_sum = 0
for num in num_list:
    new_sum += num
print(new_sum)

new_num_list = []
for val in num_list:
    for x in range(1,4):
        new_num_list.append(val)
print(new_num_list)

not_island = []
for item in countries:
    if item['island'] == 'No':
        not_island.append(item)
print(countries)
print(not_island)

# made a list of expenses and summed the values
#Add up the numbers and output the result. Put this code into a method. The method should take a list as an argument and return the sum of the expenses in the list. Call the method twice with different lists.

year_end_2018 = [1224, 2126, 332, 654, 932, 234]
year_end_2019 = [4344, 23, 542, 753, 345, 23, 23]


def sum_of_year(x):
    total_cost = 0
    for item in (x):
        total_cost += item
    return total_cost


print(sum_of_year(year_end_2018))
print(sum_of_year(year_end_2019))

grocery_list = ["carrots", "toilet paper", "apples", "salmon"]

# prints grocery_list vertically with *
def grocery_prt(x):
    for grocery in grocery_list:
        grocery = (f'* {grocery}')
        print(grocery)
grocery_list.append('rice')
grocery_prt(grocery_list)

print('Number of items to pick up', len(grocery_list))

# checks if bannans is in list
if 'bannans' in grocery_list > 0:
    print("You don't need bannans today.")
else:
    print('You need to pick up bannans today.')

# displays 2nd item in list before the sort below
print(grocery_list[1])

#sorts and prints list using function grocery_prt
print(grocery_prt(grocery_list.sort()))

# removed salmon from list
grocery_list.remove('salmon')
print(grocery_list)



