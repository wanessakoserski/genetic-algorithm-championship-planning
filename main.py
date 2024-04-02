from team import teams, mathcmaking, get_teams_with_biggest_fans_number
from championship import make_initial_version, fitness, mutation, crossover, crossover_population, tragedy, select, print_championship_planning


matches = mathcmaking(teams, return_match=True) # order matters (turn and return matches) 


print("Iniciando...")


generations = 0
population_size = 10
population = [ make_initial_version(matches) for _ in range(0, population_size) ]
max_generation = 200_000

while generations < max_generation:
    for i in range(12):
        mutated_population = [ mutation(individual) for individual in population ]

    if generations % 200:
        population = crossover_population(population)
    
    population.extend(mutated_population)

    if generations % 10000:
        population = tragedy(population, matches)

    population = select(population, population_size)

    generations += 1 
    if generations % 100 == 0:
        
        print(fitness(population[0]))
        # print_championship_planning(population[0])
        if fitness(population[0]) == 0:
            # print_championship_planning(population[0], fitness, generations)
            break
print_championship_planning(population[0])
print("Finalizado")