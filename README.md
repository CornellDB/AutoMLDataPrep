# Empirical Performance Analysis of AutoML Frameworks on Clean and Noisy Data

Automated Machine Learning (AutoML) enables the automation of crucial machine learning (ML) steps such as data cleaning, feature engineering, model selection, and hyperparameter tuning. This project aims to evaluate the impact of clean data and noisy data on the performance of AutoML frameworks. The results help us show that additional data-cleaning techniques are essential even for the AutoML frameworks to be accurate.

In this project, we evaluate the performance of two AutoML frameworks namely, [AutoKeras](https://autokeras.com/) and [TPOT](https://epistasislab.github.io/tpot/) on text classification tasks. We provide the same dataset as input to both frameworks and assess their performance using metrics such as precision, recall, and F1-score. With the help of this evaluation, we prove the need for additional cleaning of the dataset before it is fed into AutoML frameworks as input. Further, this also proves the need for the development of an efficient data-cleaning technique that co-exists and boosts AutoML performance.

## Project Setup

Detailed setup instructions are available in the [setup](setup/README.md) folder.

## Code Flow

1. Problem statement: 
   - Binary text classification
2. Get the dataset:
   - [IMDB movie reviews](https://ai.stanford.edu/~amaas/data/sentiment/) dataset.
   - Dataset is stored in [datasets](datasets/) folder
   - More information on datasets in available [here](datasets/README.md)
3. Ensure the AutoML frameworks are installed:
   - Auto Keras
   - TPOT
4. Notebooks:

   The general layout of the notebooks is as below:
   - Experiment specific details
   - Loading required packages
   - Loading and pre-processing dataset
   - Training the mode and generating predictions
   - Evaluating the model

5. Additional scripts: 

   There are also additional scripts created for easy access and repeat use. 
   - [add_noise.py](notebooks/scripts/add_noise.py): Adds Gaussian or Random noise to the text data.
   - [data_prepocess.py](notebooks/scripts/data_preprocess.py): Pre-processes and cleans the data using basic NLP approaches.  
   - [plot_model_scores.py](notebooks/scripts/plot_model_scores.py): Creates plots for comparing evaluation scores (F1, Recall, Precision) for various models.
  
## Experiments

### On Clean Data

1. [TextClassification-CleanData-AutoKeras](notebooks/textclf_cleandata_autokeras.ipynb)
2. [TextClassification-CleanData-NaiveBayes](notebooks/textclf_cleandata_naivebayes.ipynb)
3. [TextClassification-CleanData-TPOT](notebooks/textclf_cleandata_tpot.ipynb)

### On Noisy Data

1. [TextClassification-NoisyData-AutoKeras](notebooks/textclf_noisydata_autokeras.ipynb)
2. [TextClassification-NoisyData-NaiveBayes](notebooks/textclf_noisydata_naivebayes.ipynb)
3. [TextClassification-NoisyData-TPOT](notebooks/textclf_noisydata_tpot.ipynb)

## Results

Details on the implementation and the results can also be found on the project report [here](report/main.pdf).
