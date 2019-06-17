import util
import bert

class RTE:
	doc = ''
	passages = []
	def __init__(self):
		print("loading...")		
		self.m = bert.Bert_trained_model()
		

	def get_score(self, s1, s2):				
		return self.m.predict(s1, s2)
		