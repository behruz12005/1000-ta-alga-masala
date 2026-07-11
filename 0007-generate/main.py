def generate(n: int) -> list:
	paskal = []
	for row in range(n):
		row_list = []
		if row == 0:
			paskal.append([1])
		else:
			for added in range(len(paskal[-1])):
				if len(row_list) == 0:
					row_list.append(paskal[-1][added])
					row_list.append(paskal[-1][added])
				else:
					row_list[-1] += paskal[-1][added]
					row_list.append(paskal[-1][added])
			paskal.append(row_list)
	return paskal