import random
import csv


# class Item:
#     def __init__(self):
#         self.weight = random.randrange(10, 60)
#         self.value = random.randrange(1, 100)
#         self.string = 'weight: ' + str(self.weight) + ' / value: ' + str(self.value)
#         self.gene = 0
# class Item:
#     def __init__(self, weight, value):
#         self.weight = weight
#         self.value = value
#         self.string = 'weight: ' + str(self.weight) + ' / value: ' + str(self.value)
#         self.gene = 0


# bag_cap = 1000


# item1 = Item(52,51)
# item2 = Item(24,91)
# item3 = Item(40,92)
# item4 = Item(12,23)
# item5 = Item(55,53)
# item6 = Item(25,72)
# item7 = Item(32,44)
# item8 = Item(21,31)
# item9 = Item(28,79)
# item10 = Item(24,96)
#
# items = [item1, item2, item3, item4, item5, item6, item7, item8, item9, item10]
# # items = [Item() for _ in range(10)]
# weights = [item.weight for item in items]
# values = [item.value for item in items]
# length = 10
# for item in items:
#     print(item.string)
#
#
# def generate():
#     chromosome = []
#     w = 0
#     for item in items:
#         if item.weight < bag_cap - w and random.randint(0, 1) == 1:
#             item.gene = random.randint(0, int((bag_cap-w)/item.weight))
#             temp = item.weight * item.gene
#             w += temp
#         chromosome.append(item.gene)
#     return chromosome


datafile = 'test.txt'
weights = []
values = []
with open(datafile, 'rU') as data:
    lines = data.readlines()
    length = int(lines[0])
    data_only = lines
    data_only.remove(lines[0])
    read = data_only
    # next(f)  # skip headings
    reader = csv.reader(read, delimiter='\t')
    for weight, value in reader:
        weights.append(int(weight))
        values.append(int(value))


cap = 5000   # bag capacity
cross_rate = 0.6  # crossover rate
u_rate = 0.6  # uniform crossover rate aka chance of gene to swap
eli = 1  # number of elites
mutation_rate = 0.1
pop_size = 50
max_gen = 100


# def generate():
#     chromosome = []
#     list_max = max_item()
#     total_weight = 0
#     for i in range(length):
#         gene = random.randint(0, list_max[i])
#         total_weight += gene*weights[i]
#         chromosome.append(gene)
#     if total_weight < 1000:
#         return chromosome
#     else:
#         return generate()


def generate():
    chromosome = [0]*length
    c = cap
    w = 0
    for i in range(length):
        temp = int(c/weights[i])
        if random.random() < 0.5:
            chromosome[i] = random.randint(0, int(temp/4))
            c -= chromosome[i] * weights[i]
            w += chromosome[i] * weights[i]
    return chromosome
    # for i in range(length):
    #     if weights[i] < cap - w:
    #         if random.random() < 0.5:
    #             gene = int((cap-w)/weights[i])
    #             temp = weights[i] * gene
    #             w += temp
    #     chromosome.append(gene)
    # return chromosome


# def generate():
#     chromosome = []
#     w = 0
#     for i in range(length):
#         i.gene = 0
#         if weights[i] < cap - w and random.randint(0, 1) == 1:
#             i.gene = random.randint(0, int((cap - w) / weights[i]))
#             temp = weights[i] * i.gene
#             w += temp
#         # print(gene)
#         chromosome.append(i.gene)
#     return chromosome


def fitness(chromosome):
    total_value = 0
    total_weight = 0
    for i in range(length):
        total_value += chromosome[i]*values[i]
        total_weight += chromosome[i]*weights[i]
    if total_weight > cap:
        return 0
    # # print("done fitness")
    return total_value


# def roulette_selection(pop):
#     print(pop[0])
#     print(fitness(pop[0]))
#     chosen = []
#     max_fitness = fitness(pop[0])
#     # print(max_fitness)
#     while True:
#         index = int(random.random()*(length - eli))
#         if random.random() < fitness(pop[index])/max_fitness:
#             chosen.append(pop[index])
#         if len(chosen) == 2:
#             break
#     # # print("done selection")
#     print(chosen)
#     return chosen


def roulette_selection(pop):
    # sorted_pop = sorted(pop, key=lambda x: fitness(x), reverse=True)
    sum_fits = sum(fitness(x) for x in pop)
    chosen = []
    for _ in range(2):
        r = random.random() * sum_fits
        sum_temp = 0
        for i in pop:
            sum_temp += fitness(i)
            if sum_temp > r:
                chosen.append(i)
                break
    return chosen


def crossover(dad, mom):
    # child1 = dad
    # child2 = mom
    for i in range(length):
        if random.random() < u_rate:
            dad[i], mom[i] = mom[i], dad[i]
    # if random.random() < mutation_rate:
    #     mutate(dad)
    #     mutate(mom)
    # # print("done crossover")
    return dad, mom


# def mutate(chromosome, chance):
#     list_max = max_item()
#     r = random.randint(0, len(chromosome) - 1)  # pick random gene from selected chromosome
#     # temp = chromosome[r]
#     chromosome[r] = type()
#     # chromosome[r] = random.randint(0, list_max[r])  # mutate that gene
#     # while chromosome[r] == temp:  # if new mutated gene is the same, mutate again till it's different
#     #     chromosome[r] = random.randint(0, list_max[r])
#     # print("done mutate")


def mutate(chromosome, chance):
    for i in range(length):
        if random.random() < chance:
            swap_indx = random.randint(0, length - 2)
            if swap_indx >= i:
                swap_indx += 1
                chromosome[i], chromosome[swap_indx] = chromosome[swap_indx], chromosome[i]
    return chromosome,


def elites(sorted_pop):
    return [sorted_pop[i]for i in range(eli)]

#
# def evaluate():
#     return
#
#
# def tournament_selection():
#     # sample = pop
#     return
#
#
# def rank_selection():
#     # rank = []
#     # for i in range(len(pop)):
#     #     c_rank =
#
#     return


def new_population(pop):
    new_pop = []
    # print("new pop: {0}".format(new_pop))
    elite_group = elites(pop)
    # print("elites: {0}".format(elite_group))
    new_pop.extend(elite_group)
    # print("new pop with elites: {0}".format(new_pop))
    pop = [x for x in pop if x not in elite_group]
    # print(len(new_pop))
    while len(new_pop) < pop_size:
        # 18+
        parents = roulette_selection(pop)
        # print(parents)
        dad = parents[0]
        child1 = dad
        mom = parents[1]
        # if child1 == child2:
        child2 = mom
        if random.random() < cross_rate:
            new_children = crossover(dad, mom)
            child1 = new_children[0]
            child2 = new_children[1]
            mutate(child1, mutation_rate)
            mutate(child2, mutation_rate)
        if child1 == child2 and fitness(child1) != 0:
            new_pop.append(child1)
        elif child1 != child2:
            if fitness(child1) != 0:
                new_pop.append(child1)
            if fitness(child2) != 0:
                new_pop.append(child2)
        # elif child1 != child2 and fitness(child2) != 0:
        #     new_pop.append(child2)
    # print("done new_pop")
    # print(new_pop)
    return new_pop


# get the total weight of each gene from chromosome
# aka gene = 4 => total weight = 4 * item.weight
def get_weight(chromosome):
    c_weight = []
    for i in range(length):
        w = chromosome[i]*weights[i]
        c_weight.append(w)
    # print("done get_weight")
    return c_weight


def max_item():
    list_max = []
    for i in range(length):
        num = int(cap/weights[i])
        list_max.append(num)
    # print("done max_item")
    return list_max


# def max_item(chromosome):
#     list_weight = get_weight(chromosome)
#     list_max = []
#     w = 0
#     maxitem = 0
#     # for i in range(len(chromosome)):
#     #     if weights[i] < cap - w:
#     #         # print(list_weight[i])
#     #         maxitem = int((cap-w)/weights[i])
#     #         temp = weights[i] * chromosome[i]
#     #         w += temp
#     #     list_max.append(maxitem)
#     # return chromosome
#     c = cap
#     for i in range(length):
#         temp = int(c / weights[i])
#         # if random.random() < 0.5:
#         maxitem = random.randint(0, temp)
#         c -= chromosome[i] * weights[i]
#         list_max.append(maxitem)
#     return list_max


def main():
    generation = 1
    # pop = []
    # while len(pop)< pop_size:
    #     if fitness(generate()) != 0:
    #         pop.append(generate())
    #         pr
    # print(pop)
    pop = [generate() for _ in range(pop_size)]
    # print("initilaized pop: {0}".format(pop))
    # pop = sorted(pop, key=lambda x: fitness(x), reverse=True)
    # while pop[1] != pop[2] != pop[3]:
    for _ in range(max_gen):
        print(generation)
        pop = sorted(pop, key=lambda x: fitness(x), reverse=True)
        print(pop)
        fit = [fitness(i) for i in pop]
        print(fit)

        pop = new_population(pop)
        print(pop)

        print("----------------")
        generation += 1
    # print("am i fucked?")
    print(pop[0])


if __name__ == '__main__':
    main()

#
# Nuclear Zone
#

#
# # print(pop[0])
# print(max_item())
# print("-------------------")
# # print(weights)
# # print(get_weight(pop[0]))
#
# print(pop[0])
# print(pop[1])
#
# print("-------------------")
# newchild = crossover(pop[0], pop[1])
# child_1 = newchild[0]
# child_2 = newchild[1]
# print(child_1)
# print(fitness(child_1))
# print(child_2)
# print(fitness(child_2))
# print(fitness(generate()))
#
# popu = [generate() for _ in range(length)]
# popu = sorted(popu, key=lambda x: fitness(x), reverse=True)
# roulette_selection(popu)

# for _ in range(100):

# a = generate()
# print(a)
# print(fitness(a))

# popu = [generate() for _ in range(length)]
# popu = sorted(popu, key= lambda x: fitness(x), reverse=True)
# new_population(popu)

# print(pop)
# fit = [fitness(i) for i in pop]
# print(fit)
# pop = new_population(pop)
# print(pop)

# fit = [fitness(i) for i in pop]
# print(fit)

# popu = [[4, 48, 0, 100, 0, 27, 7, 20, 0, 28], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0], [0, 26, 0, 0, 4, 0, 2, 13, 0, 0]]
# # print(new_population(popu))
# for _ in range(100):
#     popu = sorted(popu, key=lambda x: fitness(x), reverse=True)
#     new_population(popu)
#     popu = new_population(popu)
#     print(new_population(popu))