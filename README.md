# Project Title

This repository contains the authors' implementation of ...

- [Features](#features)
- [Results](#results)
- [Install](#install)
- [Usage](#usage)
- [Licenses](#license)



## Features
TBD


## Results
TBD


## Install
**Requirements**:
- Python
- PyTorch >= 2.0 : https://pytorch.org/get-started/locally
- tqdm: `conda install tqdm`

**Download and Install**:
1. Download the repository;
2. Modify the dataset paths in `placeholder/paths.py`.
3. pip install the repository (in development mode): `python -m pip install -e .`


## Usage
### Pre-trained models
```python
from placeholder import get_model
model = get_model('name', pretrained=True) # weights will be downloaded automatically
model.eval()
```

### Minimal Example
TBD


### Datasets
TBD

### Evaluation
TBD

### Training
TBD


## License
Code in this repository is freely available for non-commercial use.
