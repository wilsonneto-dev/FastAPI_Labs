## Python FastAPI Labs

### Virtual E#nvironents

Creating a virtual environment

```bash
python3 -m venv venv
```

Activating the virtual environment

```bash
source venv/bin/activate
```

### Installing dependencies

```bash
pip install -r requirements.txt
```

### FastAPI Simple example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/", tags=["posts"])
def list_all_posts():
    return [{ "title": "My first post", id: 1 }, { "title": "My second post", id: 2 }]
```

To run:

```bash
uvicorn main:app --reload
```

### Libraries

Jinja2 for HTML templating