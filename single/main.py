from calvin import *
#from postprocessor import *

# specify data file
calvin = CALVIN('calvin/data/dataRecharge2.csv')

# create pyomo model from specified data file
calvin.create_pyomo_model(debug_mode=False)

# solve the problem
calvin.solve_pyomo_model(solver='glpk', nproc=10, debug_mode=False)

# postprocess results to create time-series files
postprocess(calvin.df, calvin.model, resultdir='linksPerfect')
