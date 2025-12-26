#file paths
TRAIN_DATASET = datasets/dataset_train.csv
PREDICT_DATASET = datasets/dataset_predict.csv
VALIDATION_DATASET = datasets/dataset_predict.csv
GIVEN_DATASET = datasets/data-2.csv

PARAMS_OUTPUT = params.json
PREDICT_OUTPUT = predictions_output.txt

#separation settings
TRAIN_PERCENTAGE = 0.7

#training configs
EPOCHS = 200
LAYERS = 24 24
LEARNING_RATE = 0.0005
BATCH_SIZE = 30

sep:
	@python3 separate.py --givenFile ${GIVEN_DATASET} --trainFile ${TRAIN_DATASET} --predictFile ${PREDICT_DATASET} --trainPercentage ${TRAIN_PERCENTAGE}

train:
	@python3 train.py --trainFile ${TRAIN_DATASET} --outputFile ${PARAMS_OUTPUT} --layer ${LAYERS} --epochs ${EPOCHS} --learningRate ${LEARNING_RATE} --validationFile ${VALIDATION_DATASET} \
	--batchSize ${BATCH_SIZE}

predict:
	@python3 predict.py --paramsFile ${PARAMS_OUTPUT} --predictFile ${PREDICT_DATASET} --outputFile ${PREDICT_OUTPUT}

clean:
	rm datasets/dataset_train.csv datasets/dataset_predict.csv params.json

all: sep train predict