import tensorflow as tf 
from tensorflow.keras import layers

def simple_model(em):
    model = tf.keras.Sequential([
        layers.Dense(em),
        layers.Dense(1)
    ])
    return model

def simple_compiler(model):
    return model.compile(loss = tf.keras.losses.mae , 
                        optimizer = tf.keras.optimizers.Adam(), 
                        metrics = ['mae'])

def fit_model(compile_model , epochs):
    history = compile_model.fit(X , y , 
    epochs = epochs)

    