def main():
    random.seed(42)
    
    # Create the population
    pop = toolbox.population(n=300)
    hof = tools.HallOfFame(1)
    
    # Define the statistics
    stats_fit = tools.Statistics(lambda ind: ind.fitness.values)
    stats_size = tools.Statistics(len)
    mstats = tools.MultiStatistics(fitness=stats_fit, size=stats_size)
    mstats.register("avg", np.mean)
    mstats.register("std", np.std)
    mstats.register("min", np.min)
    mstats.register("max", np.max)
    
    # Run the evolutionary algorithm
    pop, log = tools.eaSimple(pop, toolbox, 0.5, 0.2, 40, stats=mstats, halloffame=hof, verbose=True)
    
    # Display the best individual and its fitness
    print("Best individual: ", hof[0])
    print("Fitness: ", hof[0].fitness.values)

if __name__ == "__main__":
    main()
