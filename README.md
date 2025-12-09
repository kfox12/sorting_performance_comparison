# Project Logistics 
- The program's source code can be found in the sorting_performance_comparison --> final_project folder
- The two sythetic player data sets of size 10 and 1000 are generated when *make test* is run, and placed in teh sorting_performance_comparison folder
    - The real player data set of size 217 is in the final_project folder
- The Matplotlib timing graph that is generated can be found in the sorting_performance_comparison folder
- Numpy and Matplotlib are dependencies required to run the *make test* and *make demo* targets
# About the Project
- This project analyzes the run-time complexities of three different sorting algorithms, insertion sort, heapsort, and Numpy's built in sorting algorithm, called numpy.argsort()
- Unit testing (*make test*) was implemented to ensure the sorting algorithms worked properly
- NBA player data from the 2022-2023 NBA playoffs was compiled into a csv file, and then parsed in the data_loader.py file, creating Player objects with attributes of player name, team name, points per game (ppg), etc
    - Two additional data sets of size 10 and 1000 were synthetically generated with random statistic values within a reasonsable range
- The player objects are compiled into a list, and then sorted on a chosen attribute (default is ppg)
- The *make demo* target in the Makefile sorts the three different sized data sets with each of the three different sorting algorithms, five times each (total of 45 sorts)
    - The average run time of each algorithm for each data set size is computed, and added to the visual plot in the timing_results_demo.png file
- As expected, the highly-optimized numpy sort algorithm outperformed both heapsort and insertion sort, with insertion sort following an exponential growth curve for increasingly large data sets

# Testing
- *make test*
- *make demo*