#%%
import numpy as np

# GAMMA = 0.9

P = np.array([[0.2, 0.6], [0.8, 0.4]])
R = np.array([[6, 1], [1, -2]])
q = np.sum(P * R, axis=1)

def value_function(v, P, q, t=100):
    for _ in range(t):
        v = q + np.dot(v, P)
    return v

v_initial = np.array([0, 0])
v_result = value_function(v_initial, P, q)
print(v_result)
# %%
