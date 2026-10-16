P = True #its Raining
Q = True # The road is wet

Knowledge = P and Q

print("its raining", P)
print("The Road is wet", Q)
print("Knowledge Base:",Knowledge)

print("P and Q", P and Q)
print("P or Q", P or Q)
# print("P Not Q", P not Q)
print("P Implies Q", (not P) or Q)