import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from tensorflow import keras
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow import keras
from keras.preprocessing.image import ImageDataGenerator
from tensorflow import keras
from keras.callbacks import EarlyStopping

# define directories for training, validation, and test data
train_dir = 'train_og/'
valid_dir = 'validate_og/'
test_dir = 'test_og/'

# define image data generator for preprocessing and data augmentation
train_datagen = ImageDataGenerator(rescale=1./255,
                                   rotation_range=40,
                                   width_shift_range=0.2,
                                   height_shift_range=0.2,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True)
valid_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

# define batch size and image dimensions
batch_size = 32
img_width, img_height = 150, 150

# create generators for training, validation, and test data
train_generator = train_datagen.flow_from_directory(train_dir, 
                                                    target_size=(img_width, img_height), 
                                                    batch_size=batch_size, 
                                                    class_mode='binary')
valid_generator = valid_datagen.flow_from_directory(valid_dir, 
                                                    target_size=(img_width, img_height), 
                                                    batch_size=batch_size, 
                                                    class_mode='binary')
test_generator = test_datagen.flow_from_directory(test_dir,
                                                  target_size=(img_width, img_height),
                                                  batch_size=batch_size,
                                                  class_mode='binary')

# define the model architecture with dropout regularization
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(img_width, img_height, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.2))
model.add(Conv2D(64, (3, 3), activation='relu', kernel_regularizer=tf.keras.regularizers.L2(0.001)))
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.3))
model.add(Flatten())
model.add(Dense(64, activation='relu', kernel_regularizer=tf.keras.regularizers.L2(0.001)))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

# compile the model with a lower learning rate
model.compile(loss='binary_crossentropy', 
              optimizer=tf.keras.optimizers.Adam(lr=0.0001), 
              metrics=['accuracy'])

# add early stopping to prevent overfitting
early_stopping = EarlyStopping(monitor='val_loss', patience=5)

# train the model with data augmentation and early stopping
history = model.fit(train_generator, 
                    steps_per_epoch=len(train_generator), 
                    epochs=50, 
                    validation_data=valid_generator, 
                    validation_steps=len(valid_generator), 
                    callbacks=[early_stopping])

# evaluate the model on the test data
test_loss, test_acc = model.evaluate(test_generator, steps=len(test_generator))
print('Test accuracy:', test_acc)
