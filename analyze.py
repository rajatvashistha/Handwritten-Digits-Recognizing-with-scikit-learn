from sklearn import svm
svc = svm.SVC(gamma=0.001, C=100.)
from sklearn import datasets
digits = datasets.load_digits()
print(digits)
print(digits.DESCR)
digits.images[0]
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.imshow(digits.images[0], cmap=plt.cm.gray_r, interpolation='nearest')
dir(digits)
print(type(digits.images))
print(type(digits.target))
digits.images.shape
digits.target
digits.target.shape
digits.target.size
