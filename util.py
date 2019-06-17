from sklearn.feature_extraction.text import TfidfVectorizer



def get_target_passage_using_tfidf(passages, query):
	score = 0
	target = ''
	tfidf = TfidfVectorizer(stop_words=['and', 'the', 'of', 'for', 'was', 'is'])
	
	for p in passages:
		response = tfidf.fit_transform([p, query])
		res=response.toarray()[1]
		passage_score = sum(res)
		# print(passage_score)

		if passage_score > score:
			score = passage_score
			target = p
	print(score)
	# print(target)
	return target



# get_target_passage(["Ugrasrava, the son of Lomaharshana, surnamed Sauti, well-versed in the Puranas, bending with humility, one day approached the great sages of rigid vows, sitting at their ease, who had attended the twelve years' sacrifice of Saunaka, surnamed Kulapati, in the forest of Naimisha. Those ascetics, wishing to hear his wonderful narrations, presently began to address him who had thus arrived at that recluse abode of the inhabitants of the forest of Naimisha. Having been entertained with due respect by those holy men, he saluted those Munis (sages) with joined palms, even all of them, and inquired about the progress of their asceticism. Then all the ascetics being again seated, the son of Lomaharshana humbly occupied the seat that was assigned to him. Seeing that he was comfortably seated, and recovered from fatigue, one of the Rishis beginning the conversation, asked him, 'Whence comest thou, O lotus-eyed Sauti, and where hast thou spent the time? Tell me, who ask thee, in detail.'"], "who was son of Lomaharshana")