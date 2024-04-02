class Team:
    def __init__(self, name, city, fans_number):
        self.name = name
        self.city = city
        self.fans_number = fans_number

campos_team = Team("Campos FC", "Campos", 23_000)
guardioes_team = Team("Guardiões FC", "Guardião", 40_000)
protetores_team = Team("CA Protetores", "Guardião", 20_000)
leoes_team = Team("SE Leões", "Leão", 40_000)
simba_team = Team("Simba EC", "Leão", 15_000)
granada_team = Team("SE Granada", "Granada", 10_000)
lagos_team = Team("CA Lagos", "Lagos", 20_000)
solaris_team = Team("Solaris EC", "Ponte-do-Sol", 30_000)
porto_team = Team("Porto FC", "Porto", 45_000)
ferroviaria_team = Team("Ferroviária EC", "Campos", 38_000)
portuarios_team = Team("Portuários AA", "Porto", 12_000)
azedos_team = Team("CA Azedos", "Limões", 18_000)
escondidos_team = Team("SE Escondidos", "Escondidos", 50_000)
secretos_team = Team("Secretos FC", "Escondidos", 25_000)

teams = [
    campos_team,
    guardioes_team,
    protetores_team,
    leoes_team,
    simba_team,
    granada_team,
    lagos_team,
    solaris_team,
    porto_team,
    ferroviaria_team,
    portuarios_team,
    azedos_team,
    escondidos_team,
    secretos_team
]

def mathcmaking(teams, return_match=False):
    matches = []

    if return_match:
        for i in range(len(teams)):
            for j in range(len(teams)): # ensure no repetition of matches
                if i != j:
                    match = [teams[i], teams[j]]
                    matches.append(match)
    else:
        for i in range(len(teams)):
            for j in range(i + 1, len(teams)): # ensure no repetition of matches
                match = [teams[i], teams[j]]
                matches.append(match)

    return matches

def get_teams_with_biggest_fans_number(all_teams, rank=5):
    teams = all_teams[:]
    rank_teams = []

    while not len(rank_teams) == rank:
        biggest_fans_number = 0
        team_with_biggest_fans_number = None

        for team in teams:
            if team.fans_number > biggest_fans_number:
                biggest_fans_number = team.fans_number
                team_with_biggest_fans_number = team
        
        if team_with_biggest_fans_number != None:
            rank_teams.append(team_with_biggest_fans_number)
            teams.remove(team_with_biggest_fans_number)

    return rank_teams
