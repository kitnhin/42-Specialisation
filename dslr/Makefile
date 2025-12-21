DESC_DATASET = datasets/dataset_train.csv

describe:
	@python3 describe.py ${DESC_DATASET}

hist:
	@python3 histogram.py ${DESC_DATASET}

scatter:
	@python3 scatter.py ${DESC_DATASET}

pair:
	@python3 pair_plot.py ${DESC_DATASET}

train:
	@python3 logreg_train.py ${DESC_DATASET}

all: describe