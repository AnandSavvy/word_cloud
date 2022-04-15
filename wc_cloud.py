from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt # to display our wordcloud
from PIL import Image # to load our image
import numpy as np # to get the color of our image

#contnet-releated
text = open('self intro.csv', 'r').read()
stopwords = set(STOPWORDS)

#Appearance-related
wc = WordCloud(background_color = 'white', max_font_size = 50)

wc.generate(text)

#plotting
plt.imshow(wc, interpolation = 'bilinear')
plt.axis('off')
plt.show()
