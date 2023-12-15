# Project Setup

## Acknowledgements

- AutoKeras documentation - https://autokeras.com/tutorial/text_classification/

- TPOT API - https://epistasislab.github.io/tpot/api/

## Setup

1. Create a new environment for the experiments

   ```zsh
   conda activate base
   conda create -n automlenv python=3.8 anaconda
   conda activate automlenv
   ```

2. Get required AutoKeras dependencies

   ```zsh
   pip3 install autokeras
   ```

3. Get required TPOT dependencies

   ```zsh
   pip install tpot
   ```

4. Additional packages used in the project

   ```zsh
   conda install numpy scipy scikit-learn pandas joblib pytorch
   pip install deap update_checker tqdm stopit xgboost 
   ```

5. Alternatively, you can use the yml file provided in the setup folder

   ```zsh
   conda env create -f environment.yml
   conda activate automlenv
   ```
