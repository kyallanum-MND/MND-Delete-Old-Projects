[![Logo](https://whitesource-resources.s3.amazonaws.com/ws-sig-images/Whitesource_Logo_178x44.png)](https://www.whitesourcesoftware.com/)  
[![License](https://img.shields.io/badge/License-Apache%202.0-yellowgreen.svg)](https://opensource.org/licenses/Apache-2.0)

# [Mend Delete Old Projects Tool](https://github.com/kyallanum-MND/MND-Delete-Old-Projects)
This tool allows you to delete old projects that have not been scanned in awhile.

## Prerequisites
* Python 3.6+

## Installation and Execution by cloning this repo:
1. Clone the repo:
```shell
git clone https://github.com/kyallanum-MND/MND-Delete-Old-Projects.git
```

2. Run setup.py
```shell
cd MND-Delet-Old-Projects
python -m pip install -e .
```

3. Execution
```shell
mnd_delete_old_projects
```

## Usage:
This tool allows you to delete old projects that have not been scanned in awhile. In order to do this, you have to provide the tool with the appropriate information for the organization, and the number of days that you want the projects deleted to be OLDER than. (e.g. If you set 30 days, then projects that have not been scanned in 31 days or more will be deleted.)