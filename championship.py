import random

from team import teams, mathcmaking, get_teams_with_biggest_fans_number


# matches = mathcmaking(teams, return_match=True) # order matters (turn and return matches) 
total_game_days = 26
matches_per_day = 7
teams_biggest_fans_number = get_teams_with_biggest_fans_number(teams, 5)

index_day_game = 0
index_match = 1
index_match_city = 2
index_first_team = 0
index_second_team = 1


def make_initial_version(matches):
    random.shuffle(matches)
    championship = []

    day_game = 0
    count = 0

    for match in matches:
        if count % matches_per_day == 0:
            day_game += 1

        # day game (0), match (campos_teams, simba_team), city [of home team] (Campos)
        championship.append([day_game, match, match[index_first_team].city])

        count += 1

    return championship


def fitness(championship_planner):
    fit = 0
    
    for i in range(total_game_days):
        cities = []
        teams = []

        day = i + 1
        teams_in_biggest_fans_number = 0

        championship_day = championship_planner[i*matches_per_day:i*matches_per_day+matches_per_day]

        for play in championship_day:
            # checks that there is not more than one game in the same city
            city = play[index_match_city]
            if city not in cities:
                cities.append(city)
            else:
                fit -= 1

            # check that the team is not about to play in more than one game
            first_team = play[index_match][index_first_team] 
            if first_team not in teams:
                teams.append(first_team)
            else:
                fit -= 1

            # check if the team is part of the teams with the biggest fan clubs in the championship
            if first_team in teams_biggest_fans_number:
                teams_in_biggest_fans_number += 1
            
            # check that the team is not about to play in more than one game
            second_team = play[index_match][index_second_team] 
            if second_team not in teams:
                teams.append(second_team)
            else:
                fit -= 1

            # check if the team is part of the teams with the biggest fan clubs in the championship
            if second_team in teams_biggest_fans_number:
                teams_in_biggest_fans_number += 1

        # check that there isn't more than one of the big clubs playing on the same day
        if teams_in_biggest_fans_number > 1:
            fit -= 1 

    return fit


def mutation(championship_planner):
    day_1 = 0
    day_2 = 0

    # ensure that there will be a change on two different days (which really matters for the requirements)
    while day_1 == day_2:
        day_1 = random.randint(1, total_game_days)
        day_2 = random.randint(1, total_game_days)
    
    game_1 = random.randint(1, matches_per_day)
    game_2 = random.randint(1, matches_per_day)

    index_championship_1 = (day_1 - 1) * 7 + (game_1 - 1)
    index_championship_2 = (day_2 - 1) * 7 + (game_2 - 1)

    aux_city_1 = championship_planner[index_championship_1][index_match_city]
    aux_city_2 = championship_planner[index_championship_2][index_match_city]
    aux_match_1 = championship_planner[index_championship_1][index_match]
    aux_match_2 = championship_planner[index_championship_2][index_match]

    # print(day_1, game_1, aux_match_1[index_first_team].name, aux_match_1[index_second_team].name, aux_city_1)
    # print(day_2, game_2, aux_match_2[index_first_team].name, aux_match_2[index_second_team].name, aux_city_2)

    championship_planner[index_championship_1][index_match_city] = aux_city_2
    championship_planner[index_championship_2][index_match_city] = aux_city_1
    championship_planner[index_championship_1][index_match] = aux_match_2
    championship_planner[index_championship_2][index_match] = aux_match_1

    return championship_planner


def crossover(parent_1, parent_2):
    child_1 = parent_1[:]
    child_2 = parent_2[:]

    random_index_quantity = random.randint(1, len(parent_1))  # Número aleatório de pontos de corte
    random_index = random.sample(range(0, len(parent_1) + 1), random_index_quantity) 
    random_index.sort()
    # print(random_index)

    change_parent = True
    for i in range(len(random_index)):
        if (change_parent and i + 1 < len(random_index)):
            start = random_index[i]
            end = random_index[i+1]
            child_1[start:end] = parent_2[start:end]
            child_2[start:end] = parent_1[start:end]
        change_parent = not change_parent
            

    return [child_1, child_2]


def crossover_population(population):
    new_population = population[:]

    random_index_quantity = int(len(new_population) * 0.50)
    random_index = random.sample(range(0, len(new_population)), random_index_quantity)
    random_index.sort()

    for i in range(len(random_index)):
        if (i % 2 == 0):
            index = random_index[i]
            children = crossover(new_population[index], new_population[index + 1])
            new_population.extend(children)
    
    return new_population


def tragedy(population, matches):
    new_population = population[:]

    random_index_quantity = int(len(new_population) * 0.90)
    random_index = random.sample(range(0, len(new_population)), random_index_quantity) 
    random_index.sort()

    for i in range(len(random_index)):
        index = random_index[i]
        new_population[index] = make_initial_version(matches)
    
    return new_population


def select(population, population_size=10):
    new_population = sorted(population, key=fitness, reverse=True)
    return new_population[0:population_size]


def print_championship_planning(championship):
    for championship_game in championship:
        print(f"Dia {championship_game[index_day_game]}°\t{championship_game[index_match][index_first_team].name} X {championship_game[index_match][index_second_team].name}\t[[ em {championship_game[index_match_city]} ]]")
