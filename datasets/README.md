# Dataset used for experiments

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

   Gaussian noise is a type of random noise that follows Gaussian distribution. It is defined based on the mean and standard deviation provided and hence can be controlled. This type of noise resembles natural noise that occurs in nature. Below is the snippet of the code implemented to generate random noise. The noise is added to the text at the character level.

2. Random Noise:

    The (true) random noise approach was finalized as it is more realistic than other synthetic approaches discussed above. Since it is also random, there is no traceability or pattern that the model can potentially learn, leading to data leakage. Below is the snippet of the code implemented to generate random noise.
