SUDOKU SOLVING GENETIC ALGORITHM
(author: ElCresp0)

as mentioned in the code, one idea (of restarting the population in some
cases) has been taken from: 
http://micsymposium.org/mics_2009_proceedings/mics2009_submission_66.pdf

in the file main.py the parameters of the algorithm are set as follows:
> size of population: 500 (usually the bigger the better)
> number of generations: 500 (same rule applies)
both of the parameters mentioned above have a strong impact on time of
execution
> elite size: 5
during the testing I have decided not to set it to high values as it makes it
harder for the new populations to actually improve the solution (restarting)
> mutation rate: 0.05 (probability of mutation, I have tried setting it to
high values and even got some decent results, nonetheless the low rate
seems more suited imo
> restart_after: 20
this one specifies how long should the algorithm wait untill restarting
the population when the fitness of the best solution does not get better
in my implementation this field is actually going to be increased everytime
the restarting happens, so that new generations get more time to adapt to
the further developed elite

These might not be the most effective values, but it takes much time to
determine them accurately through the testing.


The fitness evaluation of a solution simply counts up the excessive
numbers in each vertical, horizontal line and box.
That means the evaluation grows for the worse solutions, and for that reason
the function in geneticSolver.py is called reversed_fitness, and its values
are multiplied by (-1) in some situations to make it more intuitive in use.

SELECTION
From the i-th generation the elite and some other solutions are selected.
The odds of being selected are better for the solutions with a higher fitness value
(roulette wheel method)

CROSSING
When crossing, each gene is chosen from one of two parents randomly if it's possible within
available numbers, otherwise the algorithm searches for an optimal number
(see the last paragraph of this readme file). Mindfull selection of the better genes from both
parents has been tried but it takes much more time and sometimes even gives worse results.

MUTATION
Random two numbers of the solution are selected and switched,
the initial numbers of the input are always preserved.

In the functions that modify a solution, such as mutation, crossing
or generation, the care is taken to make sure that the distribution of used
numbers is even (9x1, 9x2, ...). In the earlier versions of the project it was
more randomised, which also had its advantages. When such limitations take
place, it may potentially make it harder to achieve the correct solution.

Lastly but not leastly: when filling the gaps (for example during the
generation of a solution) the function get_optimal_number finds its use.
It simply looks through the sets (lines, boxes) containing the current
slot in order to evaluate which values would match it better than the others.
