from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Define the network structure
model = BayesianNetwork([('A', 'B'), ('B', 'C')])

# Define the CPDs
cpd_a = TabularCPD(variable='A', variable_card=2, values=[[0.6], [0.4]])
cpd_b = TabularCPD(variable='B', variable_card=2, values=[[0.7, 0.2], [0.3, 0.8]], evidence=['A'], evidence_card=[2])
cpd_c = TabularCPD(variable='C', variable_card=2, values=[[0.9, 0.4], [0.1, 0.6]], evidence=['B'], evidence_card=[2])

# Add CPDs to the model
model.add_cpds(cpd_a, cpd_b, cpd_c)

# Perform exact inference
inference = VariableElimination(model)
result = inference.query(variables=['C'], evidence={'A': 0})
print(result)
