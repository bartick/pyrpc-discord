# pyrpc-discord
[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?logo=discord&logoWidth=15)](https://github.com/qwertyquerty/pypresence)
[![pypi](https://img.shields.io/badge/pypi-v1.1.1-blue.svg?logo=pypi&logoWidth=15)](https://pypi.org/project/pyrpc-discord/)
[![python](https://img.shields.io/badge/python-3.5%20|%203.6%20|%203.7%20|%203.8-blue.svg?logo=python&logoWidth=15)](https://pypi.org/project/pyrpc-discord/)

A fast and simple command line tool to start discord rich presence easily.

## Key Features
- [x] Easy and fast
- [x] Auto start feature. That auto starts rpc with the last used settings
- [ ] Change specific data of rich presence
- [x] Editable using only `pyrpc start`

## Installing
**Python 3.5 or higher is required**

To install the cli you are recomended to use Pypi though you can also use github
```bash
# Linux/macOS
python3 -m pip3 install pyrpc-discord

# Windows
py -3 -m pip install pyrpc-discord
```

## Quick Example/Documentation
Use all this commands in command prompt only

**1. Inital Start**
```bash
# For quick start 
pyrpc autostart

# For normal start
pyrpc start
```


**2. After Starting RPC**
```bash
# For new settings or new rpc
update

# For stoping rpc
end
```

**Note:** After using `pyrpc start` will ask you few question. Keep the field empty if you don't want the settings (Giving Proper Client ID is important). When you are prompt to ask do you want buttons or not you can only input yes/no (Putting it empty will consider it as no). Also button url must start with `https://`

### Inquires
Please open a issue to ask any question as I don't have any discord server to share it with you. Also if you are able to fix any issue in my program please open a pull request.