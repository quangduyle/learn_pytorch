import torch
import numpy as np

a = np.random.rand(6,2)
b = torch.rand(4,3)
c = torch.rand(3,4)

print(b)
#tensor to numpy
a1 = torch.from_numpy(a)
print('convert numpy array to tensor: ', a1)

#tensor reshape
a2 = torch.reshape(a1,(3,4))
print('tensor reshape: ', a2)


#transpose
b1 = torch.transpose(b, 0, 1)
print('transpose tensor: ', b1)

#addition
e = a2 +b1
print('sum tensor: ', e)

#element-wise
ew = e*c
print('element-wise: ', ew)

#multi 
mm = torch.matmul(e, torch.transpose(c, 0, 1).double())
print('multi tensor: ', mm)

