# Simporter Test Task

## Running(Docker)

```
$ git clone https://github.com/danik-tro/Simporter-Test-Task.git smtt && cd smtt
$ docker build . task
$ docker build -dp 5000:5000 task
> http://localhost:5000
```
 
## Running (Non-Docker)

### Requirements
> python 3.8

#### Installation
```
$ git clone https://github.com/danik-tro/Simporter-Test-Task.git smtt && cd smtt
$ python -m venv env && source env/bin/activate && pip install --no-cache-dir -r requirements.txt
$ python process_data.py
$ python main.py
```
