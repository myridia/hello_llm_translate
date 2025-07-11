# hello_llm_translate

Example to translate with Large Language Models 

## Setup an Account at https://huggingface.co
* Get and Access Token, so the script can download all the models databases
* Login
``
huggingface-cli login
``


## Setup the Enviroment
```
python3.13 -m env env 
source env/bin/activate
pip install pip --upgrade
pip install -r requirements
```

## Example from English to German
```
cd Helsinki-NLP/opus-mt-en-de/
./main.py 
```


