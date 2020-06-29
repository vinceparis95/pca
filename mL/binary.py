import tensorflow as tf
import numpy as np
import pandas as pd
from tensorflow import keras
from tensorflow.keras import layers


# pour the data into a frame
dataframe = pd.read_csv("/Users/vincentparis/dev/pca/mL/binarydata.csv")
# print(dataframe)
print(dataframe.shape)
print(dataframe.head())

# split training and testing dataframes
val_dataframe = dataframe.sample(frac=0.2, random_state=1337)
train_dataframe = dataframe.drop(val_dataframe.index)

print(
    "Using %d samples for training and %d for validation"
    % (len(train_dataframe), len(val_dataframe))
)

# convert dfs to Dataset
def dataframe_to_dataset(dataframe):
    dataframe = dataframe.copy()
    # pop the target
    labels = dataframe.pop("csec_risk")
    ds = tf.data.Dataset.from_tensor_slices((dict(dataframe), labels))
    ds = ds.shuffle(buffer_size=len(dataframe))
    return ds

train_ds = dataframe_to_dataset(train_dataframe)
val_ds = dataframe_to_dataset(val_dataframe)


#

for x, y in train_ds.take(1):
    print("Input:", x)
    print("Target:", y)

train_ds = train_ds.batch(32)
val_ds = val_ds.batch(32)


#

from tensorflow.keras.layers.experimental.preprocessing import Normalization
from tensorflow.keras.layers.experimental.preprocessing import CategoryEncoding


def encode_numerical_feature(feature, name, dataset):
    # Create a Normalization layer for our feature
    normalizer = Normalization()

    # Prepare a Dataset that only yields our feature
    feature_ds = dataset.map(lambda x, y: x[name])
    feature_ds = feature_ds.map(lambda x: tf.expand_dims(x, -1))

    # Learn the statistics of the data
    normalizer.adapt(feature_ds)

    # Normalize the input feature
    encoded_feature = normalizer(feature)
    return encoded_feature

def encode_integer_categorical_feature(feature, name, dataset):
    # Create a CategoryEncoding for our integer indices
    encoder = CategoryEncoding(output_mode="binary")

    # Prepare a Dataset that only yields our feature
    feature_ds = dataset.map(lambda x, y: x[name])
    feature_ds = feature_ds.map(lambda x: tf.expand_dims(x, -1))

    # Learn the space of possible indices
    encoder.adapt(feature_ds)

    # Apply one-hot encoding to our indices
    encoded_feature = encoder(feature)
    return encoded_feature

# categorical features
sex = keras.Input(shape=(1,), name="sex", dtype="int64")
num_cases = keras.Input(shape=(1,), name="num_cases", dtype="int64")
zipcode = keras.Input(shape=(1,), name="zipcode", dtype="int64")
social_media = keras.Input(shape=(1,), name="social_media", dtype="int64")
basic_need = keras.Input(shape=(1,), name="basic_need", dtype="int64")
safetysish = keras.Input(shape=(1,), name="safetysish", dtype="int64")
runaway = keras.Input(shape=(1,), name="runaway", dtype="int64")
race = keras.Input(shape=(1,), name="race", dtype="int64")
caregiver_MH = keras.Input(shape=(1,), name="caregiver_MH", dtype="int64")
rem_home = keras.Input(shape=(1,), name="rem_home", dtype="int64")

# Numerical features
age = keras.Input(shape=(1,), name="age", dtype="int64")
aperp_age = keras.Input(shape=(1,), name="aperp_age", dtype="int64")
age_diff = keras.Input(shape=(1,), name="age_diff", dtype="int64")




all_inputs = [
    age,
    sex,
    num_cases,
    aperp_age,
    age_diff,
    zipcode,
    social_media,
    basic_need,
    safetysish,
    runaway,
    race,
    caregiver_MH,
    rem_home
]

sex_encoded = encode_integer_categorical_feature(sex, "sex", train_ds)
numcase_encoded = encode_integer_categorical_feature(num_cases, "num_cases", train_ds)
zip_encoded = encode_integer_categorical_feature(zipcode, "zipcode", train_ds)
socmed_encoded = encode_integer_categorical_feature(social_media, "social_media", train_ds)
basicneed_encoded = encode_integer_categorical_feature(basic_need, "basic_need", train_ds)
safe_encoded = encode_integer_categorical_feature(safetysish, "safetysish", train_ds)
runaway_encoded = encode_integer_categorical_feature(runaway, "runaway", train_ds)
race_encoded = encode_integer_categorical_feature(race, "race", train_ds)
caremh_encoded = encode_integer_categorical_feature(caregiver_MH, "caregiver_MH", train_ds)
rem_encoded = encode_integer_categorical_feature(rem_home, "rem_home", train_ds)

        # Numerical features
age_encoded = encode_numerical_feature(age, "age", train_ds)
aperpage_encoded = encode_numerical_feature(aperp_age, "aperp_age", train_ds)
agediff_encoded = encode_numerical_feature(age_diff, "age_diff", train_ds)

all_features = layers.concatenate(
    [
        sex_encoded,
        numcase_encoded,
        zip_encoded,
        socmed_encoded,
        basicneed_encoded,
        safe_encoded,
        runaway_encoded,
        race_encoded,
        caremh_encoded,
        rem_encoded,
        age_encoded,
        aperpage_encoded,
        agediff_encoded,
    ]
)

x = layers.Dense(32, activation="relu")(all_features)
x = layers.Dropout(0.5)(x)
output = layers.Dense(1, activation="sigmoid")(x)
model = keras.Model(all_inputs, output)
model.compile("adam", "binary_crossentropy", metrics=["accuracy"])

keras.utils.plot_model(model, show_shapes=True, rankdir="LR",
                        to_file='/Users/vincentparis/dev/pca/mL/model.png')


model.fit(train_ds, epochs=50, validation_data=val_ds)


sample = {
    "age": 13,
    "sex": 0,
    "num_cases": 2,
    "aperp_age": 29,
    "age_diff": 16,

    "zipcode": 10,
    "social_media": 1,

    # should be a bunch of binary cols for basic needs
    "basic_need": 1,
    "safetysish": 0,
    "runaway": 0,
    "race": 0,
    "caregiver_MH": 1,
    "remhome": 1,
}

input_dict = {name: tf.convert_to_tensor([value]) for name, value in sample.items()}
# print(input_dict)
model.predict(input_dict)
