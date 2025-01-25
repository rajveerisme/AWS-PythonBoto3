# AWS-PythonBoto3
Interacting with AWS using Python Boto3 Scripting

First move to the directory containing the Python Scripts, in my case it is PythonScripting so i will input
cd PythonScripting

then go into the folder containing all the files for interacting with aws,in my case it is my_ec2_scripts so i will input 
cd my_ec2_scripts

#use this command to create and activate a python virtual environment for the scripting(because in my case the python environment is externally managed by homebrew)

python3 -m venv myenv

#use this command to activate the python virtual environment 

source myenv/bin/activate

use this command to install boto3

pip install boto3

after installing boto3 you can simply run the python scripts using the command

python (file_name).py

replace (file_name) with the name of the file given for eg
i run 
python python list_ec2_instances.py
so this will display all the ec2 instances in the given format
Instance ID: , Instance Type: , Public IP: , State: 

all the files in this repository must be downloaded and stored in your pc with .py extension, and you need to use the same directories here.

Thank You For Visiting this repository
