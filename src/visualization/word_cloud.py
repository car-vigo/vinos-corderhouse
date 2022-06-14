from matplotlib import image
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS

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

def words_cloud_maskable_image(words_list, image_path):
    """
    Generate a word cloud from a list of words with shape of a mask image.
    """
    # Convert the image into a array
    mask = np.asarray(Image.open(image_path), dtype=np.uint8)
    # New mask to generate mask with 255 values
    maskable_image = np.ndarray((mask.shape[0],mask.shape[1],mask.shape[2]), np.int32)
    try: 
        for i in range(mask.shape[0]):
            for j in range(mask.shape[1]):
                maskable_image[i,j] = np.apply_along_axis(lambda arr: [255 if x == 0 else x for x in arr], 0, mask[i,j])
    except(ValueError):
        print(ValueError)
        print(f"row[i]: {i}")
        print(f"column[j]: {j}")
        print(f"mask_base_array[i,j]:\n {mask[i,j]}")
        print(f"maskable_final_array[i,j]:\n {maskable_image[i,j]}")

    text = " ".join(words_list)
    wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='#7C3030', colormap='Set2', collocations=False, stopwords = STOPWORDS, mask=maskable_image).generate(text)
    plt.figure(figsize=(20,10), facecolor="k")
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.imshow(wordcloud, interpolation='bilinear')

