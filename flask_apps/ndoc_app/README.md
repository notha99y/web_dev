# Leaderboard Using Flask
## Setup using Anaconda
1. Create conda environment
```bash
conda env create -f environment.yml
```
2. Activate conda environment
```bash
conda activate ndoc_app
```

## Exporting Flask App
```bash
export FLASK_APP=ndoc_app.py
```

## DB migration
1. Initiate database
```bash
flask db init
```
2. First db migration
1. Upgrade
```bash
flask db upgrade
```
2. Downgrade
```bash
flask db downgrade
```

## Running Flask App
```bash
flask run
```
