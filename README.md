# SpeechTool

A speech to text tool using google api/pocketsphinix.

Speech Language:` Chinese-rpc`

## Using

Click the speech button, then speak.

This tool can insert text where your `text cursor` is.

Edit `config.yml` to change the api.

if there is no `config.yml`, create one:

```yaml
# google or sphinx
reco: google
```

## Building

Before doing this, you can create a virtual environment to provide a clean building place. 😄

```bash
# install deps
pip3 install -r requirements.txt

# build
# -D: use a folder to contain all things(DLL,EXE,etc)
# -w: do not show a command window
# add more options if you like
pyinstaller -D speech.py -w

# check your file under dist folder
# if you want to change the config, create a "config.yml" file
```
