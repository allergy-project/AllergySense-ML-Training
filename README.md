# AllergySens-ML-Training
Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 conv2d (Conv2D)             (None, 54, 54, 16)        448       
                                                                 
 max_pooling2d (MaxPooling2D  (None, 27, 27, 16)       0         
 )                                                               
                                                                 
 conv2d_1 (Conv2D)           (None, 25, 25, 32)        4640      
                                                                 
 max_pooling2d_1 (MaxPooling  (None, 12, 12, 32)       0         
 2D)                                                             
                                                                 
 conv2d_2 (Conv2D)           (None, 10, 10, 64)        18496     
                                                                 
 max_pooling2d_2 (MaxPooling  (None, 5, 5, 64)         0         
 2D)                                                             
                                                                 
 flatten (Flatten)           (None, 1600)              0         
                                                                 
 dense (Dense)               (None, 512)               819712    
                                                                 
 dropout (Dropout)           (None, 512)               0         
                                                                 
 dense_1 (Dense)             (None, 2)                 1026      
                                                                 
=================================================================
Total params: 844,322
Trainable params: 844,322
Non-trainable params: 0
# Dataset (Last Usage June 2023)
- https://www.kaggle.com/datasets/henriqueolivoantonio/allergy-degrees
- https://www.kaggle.com/datasets/ismailpromus/skin-diseases-image-dataset
- https://www.kaggle.com/datasets/amellia/face-skin-disease
- https://www.kaggle.com/datasets/boltcutters/food-allergens-and-allergies 
