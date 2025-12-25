#file paths
TRAIN_DATASET = datasets/dataset_train.csv
PREDICT_DATASET = datasets/dataset_predict.csv
GIVEN_DATASET = datasets/data-2.csv

PARAMS_OUTPUT = params.json

#training configs
EPOCHS = 70
LAYERS = 24 24 24
LEARNING_RATE = 0.01

#customaisable settings
TRAIN_PERCENTAGE = 0.7

sep:
	@python3 separate.py --givenFile ${GIVEN_DATASET} --trainFile ${TRAIN_DATASET} --predictFile ${PREDICT_DATASET} --trainPercentage ${TRAIN_PERCENTAGE}

train:
	@python3 train.py --trainFile ${TRAIN_DATASET} --outputFile ${PARAMS_OUTPUT} --layer ${LAYERS} --epochs ${EPOCHS} --learningRate ${LEARNING_RATE}

clean:
	rm datasets/dataset_train.csv datasets/dataset_predict.csv

all: sep