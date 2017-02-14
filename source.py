import sys

sys.setrecursionlimit(20000)

class Pair:
	def __init__(self, first, second):
		self.missioneries, self.cannibals = first, second

	def __add__(self, other):
		return Pair(self.missioneries + other.missioneries, self.cannibals + other.cannibals)

	def __abs__(self):
		return Pair(abs(self.missioneries), abs(self.cannibals))

	def __ne__(self, other):
		return self.missioneries != other.missioneries or self.cannibals != other.cannibals

	def __eq__(self, other):
		return self.missioneries == other.missioneries and self.cannibals == other.cannibals


class Node:
	def __init__(self, value, parent, state = Pair(0, 0)):
		self.value = value
		self.state = state
		self.children = list()
		self.parent = parent

	def has_children(self, number = 0):
		try:
			return bool(self.children[number])
		except IndexError:
			return False

	def set_branch(self, node):
		self.children.append(node)


	def get_children(self):
		return self.children


def is_right_condition(pair):
	if pair.cannibals > 3 or pair.missioneries > 3:
		return False

	if pair.cannibals < 0 or pair.missioneries < 0:
		return False

	if 3 < (3 - pair.missioneries) < 0 or 3 < (3 - pair.cannibals) < 0:
		return False

	if pair.missioneries < pair.cannibals and pair.missioneries != 0:
		return False

	if (3 - pair.missioneries) < (3 - pair.cannibals) and (3 - pair.missioneries) != 0:
		return False

	if pair.missioneries == 0 and pair.cannibals == 0:
		return False
		
	return True

def get_path(node):
	path = list()
	while node != None:
		path.append((node.state.missioneries, node.state.cannibals))
		node = node.parent
	return reversed(path)

def exists(parent, node):
	while parent is not None:
		if parent.parent is not None:
			if parent.parent.value != Pair(0, 0):
				if parent.parent.state == node.state:
					return True
				elif parent.parent.parent is not None:
					parent = parent.parent.parent
				else: break
			else: break
		else: break
	return False

def depth_first_search(node):
	arrived = [Pair(0, 1), Pair(0, 2), Pair(1, 1), Pair(1, 0), Pair(2, 0)]
	leaved = [Pair(-2, 0), Pair(-1, 0), Pair(-1, -1), Pair(0, -2), Pair(0, -1)]

	if node is None:
		return None

	for arrived_pair in arrived:
		state = node.state + arrived_pair
		branch = Node(arrived_pair, node, state)
		if is_right_condition(state) and not exists(node, branch):
			node.set_branch(branch)

	children = node.get_children()
	for child in children:
		for leaved_pair in leaved:
			state = child.state + leaved_pair
			branch = Node(leaved_pair, child, state)
			if is_right_condition(state) and not exists(child, branch):
				child.set_branch(branch)

	for child in children:
		if child.state.cannibals == 3 and child.state.missioneries == 3:
			print(list(get_path(child)))
			return True
		if child.has_children():
			for grandson in child.children:
				depth_first_search(grandson)


if __name__ == '__main__':
	root = Node(Pair(0, 0), None)
	depth_first_search(root)
