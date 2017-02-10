def init():
	return [0, 0]


def count(missioneries, cannibals):
	return True if missioneries >= cannibals else False

def response(child):
	t = []
	for pair in [[0, 1], [0, 2], [1, 0], [1, 1], [2, 0], [0, -1], [0, -2], [-1, 0], [-1, -1], [-2, 0]]:
		miss = pair[0]
		cannib = pair[1]

		
		if count(child[0] + miss, child[1] + cannib) and count(3 - child[0] + miss, 3 - child[1] + cannib):
			child[0] += miss
			child[1] += cannib
			print(child)
			response(child)
			return t


def main():
	parent = init()
	res = response(parent)

	

if __name__ == '__main__':
	main()


