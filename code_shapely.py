__author__ = 'Li Bai'

import cplex
import sys
import numpy as np




# generators 0,1 demands 0,1 
# build a dictionary: 2^4=16  4 binaries: G0 G1 D0 D1; if the binary is 1, then the corresponding player joins the coalition
# for example, '1110' means G0, G1 and D0 form a coalition.
SW={
    '1111':3470,
    '1110':2720,
    '1101': 1150,
    '1011': 2520,
    '0111': 1600,
    '1100':0,
    '1010': 2520,
    '1001':1150,
    '0110':1600,
    '0101':750,
    '0011':0,
    '1000':0,
    '0100':0,
    '0010':0,
    '0001':0,
    '0000':0
}


# def generate_bin_S(digits):
#     """N players; first generate all possible coalition for N-1 players and then the last can
#      decide to join or not; digits=N-1"""
#     eles=[]
#     for k in range(2**digits):
#         ele=str(int(k/4))+str(int((k%4)/2))+str(int((k%4)%2))
#         eles.append(ele)
#     return eles

def generate_bin_S(digits):
    """N players; first generate all possible coalition for N-1 players and then the last can
     decide to join or not; digits=N-1"""
    eles=[]
    for k in range(2**digits):
        ele=''
        rest=k;
        for j in range(digits-1,-1,-1):
            ele=ele+str(int(rest/(2**j)))
            rest=int(k%(2**j))
        eles.append(ele)
    return eles

# select the elements of k "1"
def select_ones(eles, ones, idx):
    ele_with=[] # {S}
    ele_wo=[] # {S\j}
    for ele in eles:
        ele_list = list(ele)
        one_count=ele_list.count('1')
        if one_count==ones:
            ele_list_copy=ele_list.copy()
            ele_list_copy.insert(idx, '1')
            ele_with.append("".join(ele_list_copy))
            ele_list_copy=ele_list.copy()
            ele_list_copy.insert(idx, '0')
            ele_wo.append("".join(ele_list_copy))
    return ele_with, ele_wo
# ele_with, ele_wo= select_ones(eles, ones, idx)
import math
def payoff_shape_value(SW, eles):
    shapely_vals=[]
    for idx in range(0,N):
        value_sp=0
        for ss in range(1,N):
            coef=math.factorial(ss)*math.factorial(N-ss-1)/math.factorial(N)
            ele_with, ele_wo = select_ones(eles, ones=ss, idx=idx)
            sw_marg_ss=0
            for k in range(len(ele_with)):
                sw_marg_ss=sw_marg_ss+SW[ele_with[k]]-SW[ele_wo[k]]
            value_sp=value_sp+coef*sw_marg_ss
        shapely_vals.append(value_sp)
    return shapely_vals
def core_check(SW, shapely_vals):
    exs=[]
    for ele, val in SW.items():
        vs=val;
        sum_shapely_val=0.;
        for k in range(4):
            if ele[k]=='1':
                sum_shapely_val=sum_shapely_val+shapely_vals[k]
        exs.append(vs-sum_shapely_val)
    for exs_k in exs:
        if exs_k>ZEROTOL:
             print("at leat an excess is positive, shapely value is not in the core. SHAME!")
    return exs

ZEROTOL=1E-6
N=4 #number of players
eles=generate_bin_S(digits=N-1)
shapely_vals=payoff_shape_value(SW, eles)
exs=core_check(SW, shapely_vals)
print(exs)

# the utility function of all 4 players: G1, G2, D1, D2
Ws=[-90*12, -60*20, 100*40, 35*50]
# payment for each player
xs=(np.array(shapely_vals)-np.array(Ws)).tolist()
# VCG results
print("Shapely Payment G1:{}".format(shapely_vals[0]-Ws[0]))
print("Shapely Payment G2:{}".format(shapely_vals[1]-Ws[1]))
print("Shapely Payment D1:{}".format(shapely_vals[2]-Ws[2]))
print("Shapely Payment D2:{}".format(shapely_vals[3]-Ws[3]))


# VCG results
print("VCG Payment G1:{}".format(SW['1111']-SW['0111']-Ws[0]))
print("VCG Payment G2:{}".format(SW['1111']-SW['1011']-Ws[1]))
print("VCG Payment D1:{}".format(SW['1111']-SW['1101']-Ws[2]))
print("VCG Payment D2:{}".format(SW['1111']-SW['1110']-Ws[3]))


# ============================exercise 3=======================
name_var = ['x_G1', 'x_G2'] + ['x_D1', 'x_D2'] + ['Highest_x'];
bound_low=[0,0,0,0,-cplex.infinity]
bound_up=[cplex.infinity]*5
objective = [0, 0, 0, 0, 1]
rows = [];rhs = [];sense = [];name = [];
for ele, val in SW.items():
    array_a = [];
    array_b = []
    for k in range(4):
        if ele[k] == '1':
            array_b = array_b + [-1]
            array_a = array_a + [k]
    array_a = array_a + [4]
    array_b = array_b + [-1]

    rows.append((array_a, array_b))
    rhs.append(-val)
    sense.append('L')
    name.append("coalition" + ele)

rows=rows[1:-1];rhs=rhs[1:-1]; sense=sense[1:-1];name=name[1:-1]
# add the balance \sum_{X_i}=V(N)
rows.append([[0,1,2,3],[1,1,1,1]])
rhs.append(SW['1111'])
sense.append('E')
name.append("balance")

p = cplex.Cplex()
p.set_log_stream(sys.stdout)
p.set_results_stream(sys.stdout)
p.objective.set_sense(p.objective.sense.minimize)
p.variables.add(obj=objective,
                lb=bound_low,
                ub=bound_up,
                names=name_var)

p.linear_constraints.add(lin_expr=rows, senses=sense, rhs=rhs, names=name)
p.solve()
p.write("shapely.lp")
sol=p.solution.get_values()
for k_var, var in enumerate(name_var):
    print(var+"={}".format(sol[k_var]))

