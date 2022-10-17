# quick-pickups

## Installation

First, clone the repository:

```
git clone https://github.com/remoteree/quick-pickups.git
```

We recommend using a virtual environment `virtualenv` for development:
- If you do not have `virtualenv`, install:
```
pip install virtualenv
```
- After installation, access project folder
```
cd quick-pickups
```
- Create a virtual environment
```
python -m venv venv_name
```
Note: `venv_name` can be anything, a common convention is `venv`
- Enable the virtual environment
```
source venv_name/bin/activate
```
- Install all dependencies associated with the project
```
pip install -r requirements.txt
```
- If more dependencies are added inside the `virtualenb`, update requirement.txt
```
python -m pip freeze > requirements.txt
```


