import numpy as np
import random
import matplotlib.pyplot as plt
import timeit
import os
data_list=list() # List to store data

class Gentic():
    """
    Genetic algorithm for solving the N-Queens problem.

    Attributes:
    - GA: Number of queens
    - population: Number of population for starting the algorithm
    - crossover_percent: Crossover percentage on the population
    - mutation_percent: Mutation percentage on crossover

    Methods:
    - generation(): Create the initial population
    - crossover(population): Perform crossover on the population
    - mutation(crossover): Mutate the crossover
    - cost(population, crossover, mutation): Rank the answers based on cost
    - chart(x, y, title_x, title_y, show=True, path=None, save=False): Plot data
    - folder(name): Create a folder for saving data
    - solution(data_list, k=0): Extract solutions from the data_list
    - run(k): Run the genetic algorithm

    """
    def __init__(self,GA,population,crossover_percent,mutation_percent):
        self.GA=GA
        self.population = population
        self.crossover_percent=crossover_percent
        self.mutation_percent=mutation_percent

    def generation(self):
        """
        Create the first population.

        Returns:
        - population: List of permutations representing the initial population
        """

        #list for appending first population
        population= list()
        #generate first population and suffle for random position
        for i in range(self.population):
           parent = list(range(1,self.GA+1))
           np.random.shuffle(parent)
        # append to population list
           population.append(parent)
        return population




    def crossover(self,population):
        """
        Perform crossover on the population.

        Args:
        - population: List of permutations representing the population

        Returns:
        - crossover: List of permutations representing the children after crossover
        """
        #list of number for randomiz .
        # random number use for choose random position for croos over in parent
        listnumber=list(range(0,self.GA))

        #list for appending childern
        crossover=list()
        #select random parent from population list for cross over
        #cossover event in random position on parents
        for i in range(int(self.population*self.crossover_percent/2)):
            #random choose from population
            crossoverlist=random.choices(population, k=2)
            #random choose from number list
            randomnumber= random.choice(listnumber)
            #cross over
            child1=crossoverlist[0][:randomnumber] + crossoverlist[1][randomnumber:]
            child2=crossoverlist[1][:randomnumber] + crossoverlist[0][randomnumber:]
            crossover.append(child1)
            crossover.append(child2)
        return crossover





    def mutation(self,crossover):
        """
        Mutate the crossover.

        Args:
        - crossover: List of permutations representing the crossover population

        Returns:
        - mutationlist: List of permutations representing the mutated population
        """
        #create list of number
        listnumber=list(range(0,self.GA))
        listvalue=list(range(1,self.GA+1))
        #select random data from crossover for mutated
        select_for_mutation= random.choices(crossover, k = int(self.crossover_percent*len(crossover)))
        #list for appending mutation
        mutationlist=list()
        #loop for mutated
        for i in select_for_mutation:
            #random position
            randomnumber_index= random.choice(listnumber)
            #random value
            randomnumber_value= random.choice(listvalue)
            i[randomnumber_index]=randomnumber_value
            mutationlist.append(i)
        return mutationlist
    




    def cost(self,population=[],crossover=[],mutation=[]):
        """
        Rank the answers based on cost.

        Args:
        - population: List of permutations representing the population
        - crossover: List of permutations representing the crossover population
        - mutation: List of permutations representing the mutated population

        Returns:
        - data_sort: List of permutations representing the sorted data based on cost
        """
        global data_list
        # sum all data for analysis
        data = population + crossover + mutation   
        #select answer from datalist for collect uiqe data     
        data_uni=list()
        for answer in data:
            # if asnwer not in data_uni list add to it
            if answer not in data_uni:
                data_uni.append(answer)

        # all ansewrs check based on repeat value and position 
        for answer in data_uni:                    # 2 shart
            data_dict_cost =dict()
            cost = 0

            for j in range(1,self.GA+1):
                if j in answer:
                    counter = answer.count(j)
                    if counter>1:
                       cost+=counter
                       break

            for i in range(7):
                for j in range(i+1,self.GA):
                        if  abs(answer[j] - answer[i]) == abs(j-i) :
                            cost +=1
    
            # update dict of answer and value
            # this dict has two keys('answer' and 'cost')
            data_dict_cost['answer']=answer
            data_dict_cost['cost']=cost
            data_list.append(data_dict_cost)
        #this function for .sort method of data list that use ranking cost 
        # if value of cost be lower , this answer is better
        def myFunc(e):
            return e['cost']
        #data_list sorted based on cost value.
        data_list.sort(key=myFunc)
        data_sort=list()
        for i in data_list:
            data_sort.append(i['answer'])

        return data_sort[:self.population]
    


    def chart(self,x,y,title_x,title_y,show=True,path=None,save=False):
        """
        Plot the data.

        Args:
        - x: X-axis data for the plot
        - y: Y-axis data for the plot
        - title_x: Title of the X-axis
        - title_y: Title of the Y-axis
        - show: Boolean value indicating whether to show the plot (default: True)
        - path: Path for saving the plot (default: None)
        - save: Boolean value indicating whether to save the plot (default: False)
        """
        fig, ax = plt.subplots()
        ax.plot(x, y, linewidth=1.5,color='black')
        ax.set_xlabel('{}'.format(title_x))
        ax.set_ylabel('{}'.format(title_y))
        ax.set_title('{}/{}'.format(title_x,title_y))
        ax.grid(True,linestyle='--',linewidth=0.5)
        ax.label_outer()
        if show==True:
            plt.show()
        if save==True:
            filename='{}/{}-{}-{}-poplation{}-crossover{}-mutation{}-run{}.png'.format(path,title_x,title_y,self.GA,self.population,self.crossover_percent,self.mutation_percent,self.runner)
            plt.savefig(filename)
            self.population
    def folder(self,name):
        """
        Create a folder for saving data.

        Args:
        - name: Name of the folder

        Returns:
        - path: Path of the created folder
        """
        path = "{}".format(name)
        self.path = path
        # Check whether the specified path exists or not
        isExist = os.path.exists(path)
        if not isExist:
            # Create a new directory because it does not exist
            os.makedirs(path)
        return path
    

    def solution(self,data_list,k=0):
        """
        Extract solutions from the data_list.

        Args:
        - data_list: List of answer and cost number dictionaries
        - k: Number of incorrect positions in the answer (default: 0)

        Returns:
        - solution_list: List of solutions that have a cost of k
        """

        sulation_list=list()
        for answer in data_list:
            if answer['cost']==k:
                sulation_list.append(answer['answer'])
        self.sulation=sulation_list
        return(sulation_list)
    
    def run(self,k):
        """
        Run the genetic algorithm.

        Args:
        - k: Value of the number of runs

        Returns:
        - best_solution: Best solution found after k runs
        """
        self.runner=k
        global data_list

        run_l=list()
        answer_l=list()
        time_l=[0,0]
        #start time and stop time calcultes run time
        start=timeit.default_timer()
        
        population=self.generation()
        crossover=self.crossover(population)
        mutation = self.mutation(crossover)
        population=self.cost(population,crossover,mutation)

        for i in range(1,k+1):
            crossover =self.crossover(population)
            mutation = self.mutation(crossover)
            perent = self.cost([],crossover,mutation)
            data_uni=list()
            for data in data_list:
                if data not in data_uni:
                    data_uni.append(data)

            data_list=data_uni 
            cost=list()
            for ii in data_list:
                cost.append(ii['cost'])
                cost.sort()
            data_list=data_list[:200]
            stop =timeit.default_timer()
            time_c=(stop-start)+time_l[i]
            time_l.append((time_c))
            run_l.append(i)
            answer_l.append(cost.count(0))
        answer=self.solution(data_list)
        return run_l,answer_l,time_l,answer




