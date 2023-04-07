import random

COMPARTMENTS_CNT = 4
IN_CONTAINER_PROB = 0.80
ITERATIONS = 100000

conditionsMet_cnt = 0
inCompartment1_cnt = 0
inCompartment2_cnt = 0
inCompartment3_cnt = 0
inCompartment4_cnt = 0
notInContainer_cnt = 0

class Container:
	def __init__(self, compartments_cnt):
		self.compartments = [False] * compartments_cnt

for _ in range(ITERATIONS):

	# fill one of the compartments or leave empty based on IN_CONTAINER_PROB
	container = Container(COMPARTMENTS_CNT)
	if random.random() < IN_CONTAINER_PROB:
		container.compartments[random.randrange(COMPARTMENTS_CNT)] = True

	# if there's 4 compartments, gather data for each case
	if COMPARTMENTS_CNT == 4:
		if container.compartments[0] == True:
			inCompartment1_cnt += 1
		elif container.compartments[1] == True:
			inCompartment2_cnt += 1
		elif container.compartments[2] == True:
			inCompartment3_cnt += 1
		else: # 1st three containers were empty
			conditionsMet_cnt += 1
			if container.compartments[3] == True:
				inCompartment4_cnt += 1
			else:
				notInContainer_cnt += 1

if COMPARTMENTS_CNT == 4:
	print()
	print(f'inCompartment1 (unconditional): {round(inCompartment1_cnt/ITERATIONS*100, 2)}%')
	print(f'inCompartment2 (unconditional): {round(inCompartment2_cnt/ITERATIONS*100, 2)}%')
	print(f'inCompartment3 (unconditional): {round(inCompartment3_cnt/ITERATIONS*100, 2)}%')
	print(f'inCompartment4 (unconditional): {round(inCompartment4_cnt/ITERATIONS*100, 2)}%')
	print(f'notInContainer (unconditional): {round(notInContainer_cnt/ITERATIONS*100, 2)}%')
	print()
	print(f'inCompartment4 (conditional): {round(inCompartment4_cnt/conditionsMet_cnt*100, 2)}%')
	print(f'notInContainer (conditional): {round(notInContainer_cnt/conditionsMet_cnt*100, 2)}%')
	print()
