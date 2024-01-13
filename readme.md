# about 
utility script like npm init / git init
inits python repo with nessecary tools/files for pypi / pip distribution

## installation + usage
```bash
git clone "https://github.com/hashirkz/pyinit"
cd pyinit
./setup.sh

# yay now you can use pyinit anywhere after reloading ur zsh/bash
pyinit [-h] "repo name"
-h: flag to show the help message
```

### ex usage
```bash
sleepyzzz:/mnt/c/users/hashi/documents/temp$ pyinit something4
git init? (yn)? n
.venv init? (yn)? n
summary tbl
python3: Python 3.8.10
pip3: pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)
libraries
.
├── .dockerignore
├── .env
├── .gitignore
├── MANIFEST.in
├── __something4__
│   ├── __init__.py
│   ├── app.py
│   └── requirements.txt
├── build.sh
├── dockerfile
├── readme.md
├── requirements.txt
└── setup.py

1 directory, 12 files
```