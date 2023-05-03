#Name: Ishika Soni
#Email: ishika.soni97@myhunter.cuny.edu
#Date: October 8, 2021
#This program creates an image of khaki and rosy horizontal and vertical stripes.

import matplotlib.pyplot as plt
import numpy as np

size = int(input("Enter the size: "))
outputFile = input("Enter output file: ")

plaid = np.ones((size, size, 3))

#khaki
plaid[1::2,:,0] = 0.94
plaid[1::2,:,1] = 0.90
plaid[1::2,:,2] = 0.55

#rosy brown
plaid[:,1::2,0] = 0.73
plaid[:,1::2,1] = 0.56
plaid[:,1::2,2] = 0.56




#plaid[.94, .90, .55] = 0

#plt.imshow(plaid)
#plt.show()

plt.imsave(outputFile, plaid)



