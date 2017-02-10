def init():
	return [0, 0]


def count(missioneries, cannibals):
	return True if missioneries >= cannibals else False

def response(child):
	t = []
	for pair in [[0, 1], [0, 2], [1, 0], [1, 1], [2, 0], [0, -1], [0, -2], [-1, 0], [-1, -1], [-2, 0]]:
		missioneries = pair[0]
		cannibals = pair[1]

		
		if count(child[0] + missioneries, child[1] + cannibals) and count(3 - child[0] + missioneries, 3 - child[1] + cannibals):
			child[0] += missioneries
			child[1] += cannibals
			print(child)
			response(child)
			return t


def main():
	parent = init()
	res = response(parent)

	

if __name__ == '__main__':
	main()


