# Dont talk, scheme

More about this talk at [my website: tinthe.dev ](https://tinthe.dev/talks/schema-composition).
This is the repository for examples provided in the talk.

# Running the project

1. Fork the repo
2. Set up environment
```bash
virtualenv venv --python=python3
source venv/bin/activate
```
3. Install Connexion (or from requirements)
```bash
pip install connexion
pip install connexion[swagger-ui]
# ALTERNATIVELY
pip install -r requirements.txt
```
4. Run python scripts at `bird_keepers/app.py` and `bird_watchers/app.py`
