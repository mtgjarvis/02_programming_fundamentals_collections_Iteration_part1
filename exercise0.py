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

friends_fam = sorted(friends_fam.values(), reverse=True)
print(friends_fam)

fav_movies['Beauty and the Beast'] = 1991
fav_movies['Beauty and the Beast'] =  2017
print(fav_movies)