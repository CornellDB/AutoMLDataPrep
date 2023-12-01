# Datasets used for experiments

## IRIS

A small classic dataset from Fisher, 1936. One of the earliest known datasets used for evaluating classification methods. [Link to source](https://archive.ics.uci.edu/dataset/53/iris), [Link to dataset](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)

|Specification|Value|
|----|----|
|Dataset Characteristics|Tabular|
|Subject Area|Biology|
|Associated Tasks|Classification|
|Feature Type|Real|
|# Instances|150|
|# Features|4|

## IMDB

This is a dataset for binary sentiment classification containing substantially more data than previous benchmark datasets. We provide a set of 25,000 highly polar movie reviews for training, and 25,000 for testing. [Link to source](https://ai.stanford.edu/~amaas/data/sentiment/).

|Specification|Value|
|----|----|
|Dataset Characteristics|Tabular|
|Subject Area|Entertainment|
|Associated Tasks|Classification|
|Feature Type|Real|
|# Instances|50,000|
|# Features|1|

## Addition of Noise into the Data

To evaluate the performance of AutoML suggested algorithms with two different kinds of data, we added noise into the original data.

We looked at multiple ways of adding the noise.

1. Gaussian Noise:
2. Impulse Noise:
3. Salt-and-Pepper Noise:
4. Random Noise:

The random noise approach was finalized as is more realistic than other synthetic approaches discussed above. Since it is also random, there is no traceability or pattern that the model can potentially learn, leading to data leakage.
