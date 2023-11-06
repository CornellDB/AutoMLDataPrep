# Installation

## Acknowledgements

- AutoKeras documentation - https://autokeras.com/tutorial/text_classification/

## Steps

1. Identify the dataset
   1. IMDB dataset for text classification
   2. IRIS dataset for text classification
2. Identify the AutoML libraries
   1. Auto Keras
   2. TPOT

## Setup

```zsh
# Create a new environment for the experiments
conda activate base
conda create -n automlenv python=3.8 anaconda
conda activate automlenv

# Get required AutoKeras dependencies
pip3 install autokeras

# Get required TPOT dependencies
conda install numpy scipy scikit-learn pandas joblib pytorch
pip install deap update_checker tqdm stopit xgboost 
pip install tpot                                       
```
