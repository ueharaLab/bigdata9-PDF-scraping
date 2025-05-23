from utils import mnist_reader
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

X_train, y_train = mnist_reader.load_mnist('data/fashion', kind='train')
X_test, y_test = mnist_reader.load_mnist('data/fashion', kind='t10k')
print("x_train shape:",X_train.shape)
print("y_train shape:",y_train.shape)

labels = {0:'T-shirt/top', 1:'Trouser',2:'Pullover',3:'Dress',4:'Coat', 5:'Sandal',6:'Shirt',7:'Sneaker',8:'Bag',9:'Ankle boot'}

# https://collatz.hatenablog.com/entry/2022/04/26/161713
 
fig = plt.figure(figsize=(10,10))

for i,(img, label) in enumerate(zip(X_train, y_train)):
    
        
    plt.subplots_adjust(wspace=0.2, hspace=0.5)
    plt.tick_params(bottom=False,left=False,right=False,top=False)
    plt.tick_params(labelbottom=False,labelleft=False,labelright=False,labeltop=False)
    plt.subplot(5,4,i+1)
    image = Image.fromarray(img.reshape(28,28))
    plt.imshow(image)
    
    fasion_item=labels[label]
    
    plt.title(fasion_item,fontsize=8)
    
    if i==19:
        break
plt.show()