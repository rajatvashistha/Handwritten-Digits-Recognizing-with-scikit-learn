import matplotlib.pyplot as plt
def plot_multi(i):
    #'''Plots 10 digits, starting with digit i'''
    nplots = 10
    fig = plt.figure(figsize=(9,9))
    for j in range(nplots):
        plt.subplot(4,5,j+1)
        plt.imshow(digits.images[i+j], cmap='binary')
        plt.title(digits.target[i+j])
        plt.axis('off')
    plt.show()
plot_multi(0)

#Range of training set: [401:1790] & validation set: [1791:1796]

get_ipython().run_line_magic('matplotlib', 'inline')
plt.subplot(321)
plt.imshow(digits.images[1791], cmap=plt.cm.gray_r, interpolation='nearest')
plt.subplot(322)
plt.imshow(digits.images[1792], cmap=plt.cm.gray_r, interpolation='nearest')
plt.subplot(323)
plt.imshow(digits.images[1793], cmap=plt.cm.gray_r, interpolation='nearest')
plt.subplot(324)
plt.imshow(digits.images[1794], cmap=plt.cm.gray_r, interpolation='nearest')
plt.subplot(325)
plt.imshow(digits.images[1795], cmap=plt.cm.gray_r, interpolation='nearest')
plt.subplot(326)
plt.imshow(digits.images[1796], cmap=plt.cm.gray_r, interpolation='nearest')
