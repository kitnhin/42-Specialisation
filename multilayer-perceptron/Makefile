#file paths
TRAIN_DATASET = datasets/dataset_train.csv
PREDICT_DATASET = datasets/dataset_predict.csv
VALIDATION_DATASET = datasets/dataset_predict.csv
GIVEN_DATASET = datasets/data-2.csv

PARAMS_OUTPUT = params.json
PREDICT_OUTPUT = predictions_output.txt

#separation settings
TRAIN_PERCENTAGE = 0.7
SEED = -1 #SEED = -1 means no seed, random

#training configs
EPOCHS = 300
LAYERS = 24 24
LEARNING_RATE = 0.0008
BATCH_SIZE = 30
ACTIVATION_FT = sigmoid
WEIGHTS_INITIALISER = random

#nice configurations
# LAYERS = 24, 24, SEED = -1:
# af = sigmoid, wi = random, epoch = 300, lr = 0.0008
# af = sigmoid, wi = relu, epoch = 70, lr = 0.01
# LAYERS = 5 5, SEED = -1:
# af = relu, wi = random, epoch = 100, lr = 0.0008

#notes
# relu is more powerful, and can easily cause overfitting, normally used for larger datasets and deeper networks, causes gradients to update more drastically

sep:
	@python3 separate.py --givenFile ${GIVEN_DATASET} --trainFile ${TRAIN_DATASET} --predictFile ${PREDICT_DATASET} --trainPercentage ${TRAIN_PERCENTAGE}

train:
	@python3 train.py --trainFile ${TRAIN_DATASET} --outputFile ${PARAMS_OUTPUT} --layer ${LAYERS} --epochs ${EPOCHS} --learningRate ${LEARNING_RATE} --validationFile ${VALIDATION_DATASET} \
	--batchSize ${BATCH_SIZE} --activationFt ${ACTIVATION_FT} --weightsInitialiser ${WEIGHTS_INITIALISER} --seed ${SEED}

predict:
	@python3 predict.py --paramsFile ${PARAMS_OUTPUT} --predictFile ${PREDICT_DATASET} --outputFile ${PREDICT_OUTPUT}

clean:
	rm datasets/dataset_train.csv datasets/dataset_predict.csv params.json

all: sep train predict