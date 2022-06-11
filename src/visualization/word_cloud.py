import matplotlib.pyplot as plt
from wordcloud import WordCloud

def words_cloud(words_list):
    """
    Generate a word cloud from a list of words.
    """
    text = " ".join(words_list)
    wordcloud = WordCloud(width=800, height=400, max_font_size=200, background_color='white').generate(text)
    plt.figure(figsize=(10, 7))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()  # show the plot

