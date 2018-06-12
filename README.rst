onedrive-utility-cli
#############################



.. image:: https://travis-ci.org/hpnguyen123/onedrive-utility-cli.svg?branch=master
   :target: https://travis-ci.org/hpnguyen123/onedrive-utility-cli


Requirements
-------
1. Python3
2. Pip
3. VirtualEnv
4. Microsoft Business Account

Register an App @ Microsoft App Registration Portal <https://apps.dev.microsoft.com/>.
Be sure to add file read/write access to your app permission, set callback URL as <http://localhost:8080>.
Keep track of App Client Id and Client Secret.

Build
-------
1. Git Clone https://github.com/hpnguyen123/onedrive-utility-cli.git
2. cd onedrive-utility-cli
3. python3 -m venv venv
4. source venv/bin/activate
5. pip install -r requirements.txt
6. pip install -e .

Run
-------
li-onedrive init --client-id [clientid] --client-secret [secret]

Commands
-------
1. init          Initialize CLI with application id and secret
2. authenticate  Reauthenticate user using Azure Oauth
3. download      Download a file from OneDrive
4. upload        Upload a file to OneDrive

License
-------

This code is licensed under the `MIT License`_.

.. _`MIT License`: https://github.com/pvnguyen123/onedrive-utility-cli/blob/master/LICENSE