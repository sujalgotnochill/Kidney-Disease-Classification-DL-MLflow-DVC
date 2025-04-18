# Kidney-Disease-Classification-DL-MLflow-DVC



## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml
10. app.py

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/sujalgotnochill/Kidney-Disease-Classification-DL-MLflow-DVC
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n cnncls python=3.8 -y
```

```bash
conda activate cnncls
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

### STEP 03- Train the model (Edit params.yaml)
```bash
python main.py
```

### STEP 04- Run the app
```bash
python app.py
```

### To use DVC

```bash
dvc init
```
```bash
dvc reppro
```
```bash
dvc dag
```