from pywebio.output import *
from pywebio.input import *
from pywebio import start_server
import re
import time

put_markdown('# Welcome to the Data Extraction App')
with use_scope('below_header'):
    put_markdown('### Brought to you by Akshay Jadiya')

def check_username_and_password(username_password):
    if(len(re.findall('[cC]\d{6}',username_password['username'])) == 0):
        return ('username','The username must be of the form C303887 (c/C followed by 6 digits)')

    if(username_password['password'] != 'password'):
        return ('password','The password is incorrect')


username_password = input_group("Enter your ERT/FNSH/ODS username and password",
[
  input('Input your username',
        name='username' ,
        placeholder='username',
        required=True),
  input('Input your password',
        name='password' ,
        placeholder='password' ,
        required=True)
],
validate = check_username_and_password)

toast('Connected to Lilly databases',
        position='middle',
        color='#2188ff',
        duration=0)

with use_scope('below_header' , clear = True):
    put_markdown('### Choose the dataset you want to extract')

dataset_list = ['Brand Value' ,
                'Adoption Ladder' ,
                'Interaction Data' ,
                'Call Commitment' ,
                'Tier' ,
                'HCP Universe']

choice_of_dataset = select('Choose dataset type', dataset_list)
