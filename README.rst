onedrive-utility-cli
#############################



.. image:: https://travis-ci.org/pvnguyen123/onedrive-utility-cli.svg?branch=master
   :target: https://travis-ci.org/pvnguyen123/onedrive-utility-cli


Requirements
-------
1. Python 3.5
2. Pip
3. VirtualEnv
4. Register an App @ Microsoft App Registration Portal <https://apps.dev.microsoft.com/>.
Be sure to add file read/write access to your app permission. Keep track of App Client Id
and Client Secret, which is needed later.

Build
-------
1. Git Clone https://github.com/pvnguyen123/onedrive-utility-cli.git
2. cd onedrive-utility-cli
3. python3 -m venv venv
4. source venv/bin/activate
5. pip install -r requirements.txt
6. pip install -e .

Run
-------
li-onedrive -h

li-onedrive init --client-id [clientid] --client-secret [secret]

li-onedrive download '/attchment/somefile.csv'

License
-------

This code is licensed under the `MIT License`_.

.. _`MIT License`: https://github.com/pvnguyen123/onedrive-utility-cli/blob/master/LICENSE