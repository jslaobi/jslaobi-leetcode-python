class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        population_change = [0] * 101

        for birth, death in logs:
            population_change[birth - 1950] += 1
            population_change[death - 1950] -= 1
        
        max_population = 0
        curr_population = 0
        max_year = 0

        for i in range(2050 - 1950 + 1):
            curr_population += population_change[i]

            if curr_population > max_population:
                max_population = curr_population
                max_year = 1950 + i
        
        return max_year
