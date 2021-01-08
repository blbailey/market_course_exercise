# market_course_exercise
cplex solver, shapely value based payoff calculation; core search

code_shapley.py 

shapley.lp is the output file from cplex solver, which presents the optimization problem in a concise way.

The results of the exercises:

at leat an excess is positive, shapley value imputation is not in the core. SHAME!


Shapley value based Payment G1:2190.0
Shapley value based Payment G2:1783.3333333333333
Shapley value based Payment D1:-2665.0
Shapley value based Payment D2:-1308.3333333333335

VCG Payment G1:2950
VCG Payment G2:2150
VCG Payment D1:-1680
VCG Payment D2:-1000

One imputation result in the core:
x_G1=600.0
x_G2=200.0
x_D1=2020.0
x_D2=650.0
Highest_x=-100.0



