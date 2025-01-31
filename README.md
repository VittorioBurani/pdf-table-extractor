# PDF Table Extractor

This repo let's you extract all the tables present in a list of PDFs as CSVs.

*It will be assumed that have already installed [**Python 3**](https://www.python.org/downloads/) on your PC.*

<hr>

## Requirements Installation:
### **Windows:**
*It will be assumed that you cloned **PDF Table Extractor** repo at a certain path: ex. "C:/Users/Username/Github/". It will be used the more general "/path/to/" alias to refer to the specific path.*

Install *python virtualenv*:
```
pip install venv
```
Create a new python virtual environment inside the holygrail repo (insert its neme in the .gitignore file):
```
cd /path/to/pyfanta/
python -m venv venv
```
Activate the newly created virtual environment:
```
venv/Scripts/activate
```
Install all python requirements through *pip install*:
```
cd /path/to/repo/
pip install -r requirements.txt
```
Check if there are broken requirements:
```
pip check

> No broken requirements found.
```
**If the output is different from the one above**, install the packages listed in the output through *pip install*:
```
pip install <missing-module-1> <missing-module-2> <...>
```
<br>

### **Ubuntu/Debian Linux:**
*It will be assumed that you cloned **PDF Table Extractor** repo in your home directory.*
Install *pip3*:
```
sudo apt update
sudo apt install python3-pip
```
**Optional (Recommended):** Install *python3-venv* for python3 virtual environment management:
```
sudo apt install python3-venv
```
**Optional (Recommended):** Create a new python3 virtual environment inside the holygrail repo (insert its name in the .gitignore file):
```
cd /path/to/repo/
python3 -m venv venv
```
**Optional (Recommended):** Activate the newly created virtual environment:
```
source venv/bin/activate
```
**Warning:** if you followed these steps it is possible you will have to call just **"pip"** and not **"pip3"**.

Install all python3 requirements through *pip3 install*:
```
cd /path/to/repo/
pip3 install -r requirements.txt
```
Check if there are broken requirements:
```
pip3 check

> No broken requirements found.
```
**If the output is different from the one above**, install the packages listed in the output through *pip3 install*:
```
pip3 install <missing-module-1> <missing-module-2> <...>
```
<br>

### **MacOS:**
*It will be assumed that you cloned **holygrail** repo in your home directory.*
*It will be assumed that you have already installed **homebrew** on your Mac.*

*pip3* is installed along with *python3*:
```
brew install python3
```
If you have a version of Homebrew prior to 1.5, you may need to launch also:
```
brew postinstall python3
```
**Optional (Recommended):** Install *python3 virtualenv* for python3 virtual environment management:
```
pip3 install virtualenv
```
**Optional (Recommended):** Create a new python3 virtual environment inside the holygrail repo (insert its name in the .gitignore file):
```
cd /path/to/repo/
python3 -m venv venv
```
**Optional (Recommended):** Activate the newly created virtual environment:
```
source venv/bin/activate
```
**Warning:** if you followed these steps it is possible you will have to call just **"pip"** and not **"pip3"**.

Install all python3 requirements through *pip3 install*:
```
cd /path/to/repo/
pip3 install -r requirements.txt
```
Check if there are broken requirements:
```
pip3 check

> No broken requirements found.
```
**If the output is different from the one above**, install the packages listed in the output through *pip3 install*:
```
pip3 install <missing-module-1> <missing-module-2> <...>
```


<hr>

## Usage:

The script accepts a `--file` argument equivalent of a list of pdf-file paths `\n` separated:

```bash
./pdf_to_csvs.py -f <list of pdf-paths \n separated>
```

This enables for shell scripting using something similar to Unix's `find`.

### **Windows:**
Run the main script *"pdf_to_csvs.py*" (from `powershell`):
```
cd /path/to/repo/
python pyfanta.py $(dir /s /b <base_search_path><pdf_names_pattern>)
```
### **Linux or MacOS:**
Run the main script *"pdf_to_csvs.py*" (from `shell`):
```
cd /path/to/repo/
./pyfanta.py $(find <base_search_path> -name <pdf_names_pattern>)
```
