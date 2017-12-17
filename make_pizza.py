def make_pizza(size, weight, **toppings):
	all_info = {}
	all_info['size'] = size
	all_info['weight'] = weight
	for m, n in toppings.items():
		all_info[m] = n
	return all_info


def show():
	print('Hello!')
