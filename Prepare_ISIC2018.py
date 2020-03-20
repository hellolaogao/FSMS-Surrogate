# Abdur. R. Fayjie, R. Azad, Claude Kauffman, Ismail Ben Ayed, Marco Pedersoli and Jose Dolz "Semi-supervised Few-Shot Learning for Medical Image Segmentation", arXiv preprint arXiv, 2020
import h5py
import numpy as np
import scipy.io as sio
import scipy.misc as sc
import glob

# Parameters
height = 224
width  = 224
channels = 3

############################################################# Prepare ISIC 2018 data set #################################################
Dataset_add = '/home/maryam/Maryam/Medical/ISIC2018/'
Tr_add = 'ISIC2018_Task1-2_Training_Input'

Tr_list = glob.glob(Dataset_add+ Tr_add+'/*.jpg')
# It contains 2594 training samples
Data_train_2018    = np.zeros([2594, height, width, channels])
Label_train_2018   = np.zeros([2594, height, width])

print('Reading ISIC 2018')
for idx in range(len(Tr_list)):
    print(idx+1)
    img = sc.imread(Tr_list[idx])
    img = np.double(sc.imresize(img, [height, width, channels], interp='bilinear', mode = 'RGB'))
    Data_train_2018[idx, :,:,:] = img

    b = Tr_list[idx]    
    a = b[0:len(Dataset_add)]
    b = b[len(b)-16: len(b)-4] 
    add = (a+ 'ISIC2018_Task1_Training_GroundTruth/' + b +'_segmentation.png')    
    img2 = sc.imread(add)
    img2 = np.double(sc.imresize(img2, [height, width], interp='bilinear'))
    Label_train_2018[idx, :,:] = img2    
         
print('Reading ISIC 2018 finished')

################################################################ Make the train and test sets ########################################    
# We consider 1000 samples for test and rest for training the unsupervised network

Train_img      = Data_train_2018[0:1000]
Test_img       = Data_train_2018[1000:]
Test_mask      = Label_train_2018[1000:]

np.save('data_train_isic', Train_img)
np.save('data_test_isic' , Test_img)
np.save('mask_test_isic' , Test_mask)
