from webapp import Server
from webapp.model import userinp
from flask import abort

#Wordcloud imports
import os
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS

class Brain:

	def __init__(self):
		self.db = Server().db
		self.path = os.path.dirname(os.path.abspath(__file__))

	def store_words(self,w1,w2,w3,w4,uip):
		try:
			userinput = userinp.Userinp(w1,w2,w3,w4,uip)
			self.db.session.add(userinput)
			self.db.session.commit()
			self.db.session.close()
		except:
			abort(500)

	def store_feed(self,feed,uip):
		try:
			userinput = userinp.Userfeed(feed,uip)
			self.db.session.add(userinput)
			self.db.session.commit()
			self.db.session.close()
		except Exception as e:
			print(e)
			abort(500)

	def extract_words(self):
		result = self.db.engine.execute("SELECT w1,w2,w3,w4 from userinp")
		data = [i[j] for i in result for j in range(4)]
		data = ' '.join(data)
		return data

	def word_cloud(self,data):
		mask = np.array(Image.open(os.path.join(self.path,"../static/files/cloud.png")))	
		stopwords = set(STOPWORDS)
		wc = WordCloud(background_color="white",
						max_words=50, 
						mask=mask,
		               	stopwords=stopwords)
		wc.generate(data)
		wc.to_file(os.path.join(self.path,"../static/files/wc.png"))

