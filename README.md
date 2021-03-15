# STAMP - Static API Markup Processor
A tool to generate static webpages from a given OpenAPI specification using Jinja templates.

### Usage
Using the [Petstore OpenAPI](https://github.com/OAI/OpenAPI-Specification/blob/master/examples/v3.0/petstore.yaml) example with the basic template
```
curl https://raw.githubusercontent.com/OAI/OpenAPI-Specification/master/examples/v3.0/petstore.yaml -o petstore.yaml
./stamp.py petstore.yaml templates/basic/
```

### Development
I recommend using a python virtual environment:
```bash
python -m venv ./venv/
. ./venv/Scripts/activate
```
