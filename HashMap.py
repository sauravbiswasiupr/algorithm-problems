# Algorithm to implement a hashmap. In this implementation
# if the a certain slot in the bucket list is not empty we
# skip by the value SKIP_SIZE


class HashMap:
	def __init__(self, slots=11, skip_size=1):
		self.slots = slots
		self.SKIP_SIZE = skip_size
		self.buckets = [None]*self.slots

	def hashfunction(self, item):
		if isinstance(item, int):
			length = 0
			n = item
			vals = []

			while (n > 0):
				r = n % 10
				n = n / 10
				vals.append(r)
				length = length + 1


			if length % 2 == 0:
				sum  = float(vals[n/2] + vals[n/2+1])/2
				sum = sum % self.slots
				return sum
			else:
				sum = float(vals[n/2]) % self.slots
				return sum
		elif type(item) == str:
			sum = 0
			for i in range(len(item)):
				sum = sum + (i+1)*ord(item[i])

			sum  = sum % self.slots
			return sum
		else:
			raise Exception("Not a string or integer item")

	def put(self, key, value):
		hashvalue = self.hashfunction(key)
		if self.buckets[hashvalue] == None:
			self.buckets[hashvalue] = [key, value]
		elif self.buckets[hashvalue][0] == key:
			self.buckets[hashvalue][1] = value
		else:
			skip = self.SKIP_SIZE
			hashvalue_new = (hashvalue + skip) % self.slots
			while hashvalue_new != hashvalue:
				if self.buckets[hashvalue_new] == None:
					self.buckets[hashvalue_new] = [key, value]
					break

				hashvalue_new = (hashvalue_new + skip) % self.slots

		return

	def get(self, key):
		hashvalue = self.hashfunction(key)
		if self.buckets[hashvalue] != None:
			return self.buckets[hashvalue][1]

		else:
			hashvalue_new = (hashvalue + self.SKIP_SIZE) % self.slots
			while hashvalue_new != hashvalue:
				if self.buckets[hashvalue_new] != None:
					return self.buckets[hashvalue_new][1]
					hashvalue_new = (hashvalue_new + self.SKIP_SIZE) % self.slots

	def __getitem__(self, key):
		return self.get(key)

	def __setitem__(self, key, value):
		self.put(key, value)


if __name__ == '__main__':
	hashmap = HashMap()

	hashmap["saurav"] = 1
	hashmap["biswas"] = 2
	print "hashmap now: ", hashmap.buckets

	hashmap["saurav"] = 3
	print "Hashmap now: ", hashmap.buckets