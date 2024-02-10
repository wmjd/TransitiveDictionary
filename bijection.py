import types

class TransDict:
	''' usage:
	from transdict import TransDict

	labels = (“color”,”int”,”float”)
	relations = [
		(“Red”, 1, 43.0)
		(“Green”, 2, 99.9)
		(“Blue, 3, 101.0)]
 
	td = TransDict(labels, relations)

	td[“Red”]			// 1
	td[1]				// 43.0
	td[43.0]			// “Red”
	td.colorOf(1)		// "Red"
	td.colorOf(99.9)	// "Green"

	'''

	def __init__(self, labels, relations):
		self.labels = labels
		self.directory = dict()
		for label in labels:
			setattr(self, label, dict())
		for relation in relations:
			for i,x in enumerate(relation):
				self.directory[x] = getattr(self, self.labels[i])
				self.directory[x][x] = relation[(i+1) % len(relation)]
		for i, label in enumerate(labels):
			setattr(self, label + 'Of', types.MethodType(self.methodGen(i), self))	

	def __getitem__(self, key):
		return self.directory[key][key]

	def methodGen(self, i):
		dstTable = getattr(self, self.labels[(i-1) % len(self.labels)])
		def inner(self, key): 
			srcTable = self.directory[key]
			if key in dstTable:
				return self[key]
			while key not in dstTable:
				key = self[key]
			return self[key]
		return inner

	def add(self, relation):
		if len(relation) != len(self.labels):
			raise Exception("sequence length mismatch")
		elif any([key in getattr(self, self.labels[i]) for i,key in enumerate(relation)]):
			raise Exception("duplicate key") 
		else:
			for i,x in enumerate(relation):
				self.directory[x] = getattr(self, self.labels[i])
				self.directory[x][x] = relation[(i+1) % len(relation)]

	print("Coming to you from the Transitive Dictionary module!")
