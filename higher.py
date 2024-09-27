import random


data = [
    {
        "name": "Lionel Messi",
        'followers': random.choice(range(0, 101)),
        'country': 'Argentina',
        'description': "GOAT, multiple Ballon d'Or winner"
    },
    {
        "name": "Cristiano Ronaldo",
        'followers': random.choice(range(0, 101)),
        'country': 'Portugal',
        'description': "The most followed footballer in the world"
    },
    {
        "name": "Neymar Jr",
        'followers': random.choice(range(0, 101)),
        'country': 'Brazil',
        'description': "Brazilian magician with flair"
    },
    {
        "name": "Kylian Mbappé",
        'followers': random.choice(range(0, 101)),
        'country': 'France',
        'description': "Speedster and World Cup winner"
    },
    {
        "name": "Sergio Ramos",
        'followers': random.choice(range(0, 101)),
        'country': 'Spain',
        'description': "Legendary Spanish defender"
    },
    {
        "name": "Zlatan Ibrahimović",
        'followers': random.choice(range(0, 101)),
        'country': 'Sweden',
        'description': "The lion of football"
    },
    {
        "name": "Robert Lewandowski",
        'followers': random.choice(range(0, 101)),
        'country': 'Poland',
        'description': "Goal machine from Poland"
    },
    {
        "name": "Kevin De Bruyne",
        'followers': random.choice(range(0, 101)),
        'country': 'Belgium',
        'description': "Midfield maestro"
    },
    {
        "name": "Eden Hazard",
        'followers': random.choice(range(0, 101)),
        'country': 'Belgium',
        'description': "Belgian dribbler"
    },
    {
        "name": "Sadio Mané",
        'followers': random.choice(range(0, 101)),
        'country': 'Senegal',
        'description': "Senegalese winger with pace"
    },
    {
        "name": "Mohamed Salah",
        'followers': random.choice(range(0, 101)),
        'country': 'Egypt',
        'description': "Egyptian King"
    },
    {
        "name": "Paul Pogba",
        'followers': random.choice(range(0, 101)),
        'country': 'France',
        'description': "World Cup-winning midfielder"
    },
    {
        "name": "Virgil van Dijk",
        'followers': random.choice(range(0, 101)),
        'country': 'Netherlands',
        'description': "The Dutch wall in defense"
    },
    {
        "name": "Karim Benzema",
        'followers': random.choice(range(0, 101)),
        'country': 'France',
        'description': "French striker, Ballon d'Or winner"
    },
    {
        "name": "Luka Modrić",
        'followers': random.choice(range(0, 101)),
        'country': 'Croatia',
        'description': "Midfield magician, Ballon d'Or 2018"
    },
    {
        "name": "Erling Haaland",
        'followers': random.choice(range(0, 101)),
        'country': 'Norway',
        'description': "The unstoppable goal scorer"
    },
    {
        "name": "Antoine Griezmann",
        'followers': random.choice(range(0, 101)),
        'country': 'France',
        'description': "Versatile French forward"
    },
    {
        "name": "Harry Kane",
        'followers': random.choice(range(0, 101)),
        'country': 'England',
        'description': "Prolific English striker"
    },
    {
        "name": "Gareth Bale",
        'followers': random.choice(range(0, 101)),
        'country': 'Wales',
        'description': "Speedster and Welsh wizard"
    },
    {
        "name": "Romelu Lukaku",
        'followers': random.choice(range(0, 101)),
        'country': 'Belgium',
        'description': "Powerful Belgian forward"
    },
    {
        "name": "Jadon Sancho",
        'followers': random.choice(range(0, 101)),
        'country': 'England',
        'description': "Young English winger"
    },
    {
        "name": "Thiago Silva",
        'followers': random.choice(range(0, 101)),
        'country': 'Brazil',
        'description': "Veteran Brazilian defender"
    },
    {
        "name": "Phil Foden",
        'followers': random.choice(range(0, 101)),
        'country': 'England',
        'description': "English wonderkid"
    },
    {
        "name": "Mason Mount",
        'followers': random.choice(range(0, 101)),
        'country': 'England',
        'description': "Talented English midfielder"
    },
    {
        "name": "Marcus Rashford",
        'followers': random.choice(range(0, 101)),
        'country': 'England',
        'description': "English forward and philanthropist"
    },
    {
        "name": "Raheem Sterling",
        'followers': random.choice(range(0, 101)),
        'country': 'England',
        'description': "Pacy English winger"
    },
    {
        "name": "Toni Kroos",
        'followers': random.choice(range(0, 101)),
        'country': 'Germany',
        'description': "German midfielder with precision"
    },
    {
        "name": "Gerard Piqué",
        'followers': random.choice(range(0, 101)),
        'country': 'Spain',
        'description': "Spanish legend and Barça icon"
    },
    {
        "name": "Manuel Neuer",
        'followers': random.choice(range(0, 101)),
        'country': 'Germany',
        'description': "Sweeper-keeper extraordinaire"
    },
    {
        "name": "Luis Suárez",
        'followers': random.choice(range(0, 101)),
        'country': 'Uruguay',
        'description': "Uruguayan striker with bite"
    }
]



def randon_int():
    random_integer = random.choice(range(0, len(data)))
    return random_integer


def find_second_choice():
    global index, second_index
    second_index = randon_int()
    while index == second_index:
        second_index = randon_int()
    return second_index


def get_good_answer(first_choice, second_choice):
    if first_choice['followers'] > second_choice['followers']:
        good_answer = "a"
    elif first_choice['followers'] < second_choice['followers']:
        good_answer = "b"
    else:
        good_answer = 'a'
    return good_answer



def answer_is_correct(good_answer, answer_user):
    global user_is_right
    if answer_user != good_answer:
        print('not_good _______________')
        user_is_right = False
        return False
    else:
        user_is_right = True
        return True


def add_point():
    global user_point
    user_point += 1
    return user_point


user_is_right = True
user_point = 0

index = randon_int()

user_a = data[index]
second_index = find_second_choice()
user_b = data[second_index]


# begin
# on récupére la bonne réponse entre les 2 choix

while user_is_right:
    the_good_answer = get_good_answer(user_a, user_b)
    print(f"compare A : {user_a['name']} description :  {user_a['description']}, followers: {user_a['followers']} \n")
    print(f"against B : {user_b['name']} description :  {user_b['description']}, followers: {user_b['followers']}")
    #réponse du user
    user_answer = input(f"tape 'A' for {user_a['name']} and 'B' for {user_b['name']} : ")
    is_correct = answer_is_correct(the_good_answer, user_answer)
    if is_correct:
        add_point()
        print(f"answer is correct you current score : {user_point} ")

    index = second_index
    user_a = data[index]
    user_b = data[find_second_choice()]

print(f"answer is wrong :  you got {user_point} points")