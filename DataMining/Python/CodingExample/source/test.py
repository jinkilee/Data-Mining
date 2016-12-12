
import som
import numpy as np
import preprocess

from matplotlib import pyplot as plt
 
#Training inputs for RGBcolors
data, label, ip = preprocess.get_data("../data/")
color_names = ['black', 'blue', 'darkblue', 'skyblue',
     'greyblue', 'lilac', 'green', 'red', 'cyan', 'violet', 'yellow', 'white', 'darkgrey', 'mediumgrey', 'lightgrey'
]

datasize, numfeat = data.shape
 
#Train a 20x30 SOM with 400 iterations
som = som.SOM(30, 30, numfeat, 400)
som.train(data)
exit()
 
#Get output grid
image_grid = som.get_centroids()
 
#Map colours to their closest neurons
mapped = som.map_vects(colors)
 
#Plot
plt.imshow(image_grid)
plt.title('Color SOM')
for i, m in enumerate(mapped):
    plt.text(m[1], m[0], color_names[i], ha='center', va='center',
             bbox=dict(facecolor='white', alpha=0.5, lw=0))
plt.show()
