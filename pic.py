from PIL import Image
import numpy as np
message=Image.open('timg1.jfif')
message_R=np.array(message)[:,:,0]
message_G=np.array(message)[:,:,1]
message_B=np.array(message)[:,:,2]
polarity=((message_R>=128)*(message_G>=128)*(message_B>=128))*255
polarity_2=Image.fromarray(polarity)
np.shape(polarity)
#polarity_2.show()
polarity_2=polarity_2.convert('RGB')
polarity_2.save('firstresult.tif')
#target img has already convert as black or white
cover=Image.open('timg.jfif')
cover_R=np.array(cover)[:,:,0]
for i in range(849):
    for j in range(1279):
        if polarity[i,j]==255:
            cover_R[i,j]=cover_R[i,j]-cover_R[i,j]%2
        else:
            cover_R[i,j]=cover_R[i,j]-cover_R[i,j]%2+1
cover_2=np.zeros((850,1280,3))
cover_2[:,:,0]=np.copy(cover_R)
cover_2[:,:,1]=np.copy(np.array(cover)[:,:,1])
cover_2[:,:,2]=np.copy(np.array(cover)[:,:,2])
cover_3=Image.fromarray(cover_2.astype('uint8'))
#cover.show()
cover_3.save('hided.tif')#BUG:I just save the wrong variable
#message have already hided in the cover img
recover=Image.open('hided.tif')
recover_R=np.array(recover)[:,:,0]
tmp=np.zeros((850,1280))
for i in range(849):
    for j in range(1279):
        if recover_R[i,j]%2==0:
            tmp[i,j]=255
        else:
            tmp[i,j]=0
result=Image.fromarray(tmp)
result=result.convert('RGB')
result.show()
result.save('finalresult.tif')
