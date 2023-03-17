ISSUE:
```
Python 3.8.10 (default, Jun 22 2022, 20:18:18) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import OpenSSL
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "$HOME/.local/lib/python3.8/site-packages/OpenSSL/__init__.py", line 8, in <module>
    from OpenSSL import rand, crypto, SSL
  File "$HOME/.local/lib/python3.8/site-packages/OpenSSL/rand.py", line 211, in <module>
    _lib.ERR_load_RAND_strings()
AttributeError: module 'lib' has no attribute 'ERR_load_RAND_strings'
Error in sys.excepthook:
Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/apport_python_hook.py", line 72, in apport_excepthook
    from apport.fileutils import likely_packaged, get_recent_crashes
  File "/usr/lib/python3/dist-packages/apport/__init__.py", line 5, in <module>
    from apport.report import Report
  File "/usr/lib/python3/dist-packages/apport/report.py", line 32, in <module>
    import apport.fileutils
  File "/usr/lib/python3/dist-packages/apport/fileutils.py", line 12, in <module>
    import os, glob, subprocess, os.path, time, pwd, sys, requests_unixsocket
  File "/usr/lib/python3/dist-packages/requests_unixsocket/__init__.py", line 1, in <module>
    import requests
  File "/usr/lib/python3/dist-packages/requests/__init__.py", line 95, in <module>
    from urllib3.contrib import pyopenssl
  File "/usr/lib/python3/dist-packages/urllib3/contrib/pyopenssl.py", line 46, in <module>
    import OpenSSL.SSL
  File "$HOME/.local/lib/python3.8/site-packages/OpenSSL/__init__.py", line 8, in <module>
    from OpenSSL import rand, crypto, SSL
  File "$HOME/.local/lib/python3.8/site-packages/OpenSSL/rand.py", line 211, in <module>
    _lib.ERR_load_RAND_strings()
AttributeError: module 'lib' has no attribute 'ERR_load_RAND_strings'

Original exception was:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "$HOME/.local/lib/python3.8/site-packages/OpenSSL/__init__.py", line 8, in <module>
    from OpenSSL import rand, crypto, SSL
  File "$HOME/.local/lib/python3.8/site-packages/OpenSSL/rand.py", line 211, in <module>
    _lib.ERR_load_RAND_strings()
AttributeError: module 'lib' has no attribute 'ERR_load_RAND_strings'
```
SOLUTION:
```
pip3 install pyopenssl==17.5.0
```

ISSUE:
```
Python 3.8.10 (default, Jun 22 2022, 20:18:18) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import OpenSSL
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "$HOME/.local/lib/python3.8/site-packages/OpenSSL/__init__.py", line 8, in <module>
    from OpenSSL import crypto, SSL
  File "$HOME/.local/lib/python3.8/site-packages/OpenSSL/crypto.py", line 1550, in <module>
    class X509StoreFlags(object):
  File "$HOME/.local/lib/python3.8/site-packages/OpenSSL/crypto.py", line 1570, in X509StoreFlags
    CB_ISSUER_CHECK = _lib.X509_V_FLAG_CB_ISSUER_CHECK
AttributeError: module 'lib' has no attribute 'X509_V_FLAG_CB_ISSUER_CHECK'
Error in sys.excepthook:
Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/apport_python_hook.py", line 72, in apport_excepthook
    from apport.fileutils import likely_packaged, get_recent_crashes
  File "/usr/lib/python3/dist-packages/apport/__init__.py", line 5, in <module>
    from apport.report import Report
  File "/usr/lib/python3/dist-packages/apport/report.py", line 32, in <module>
    import apport.fileutils
  File "/usr/lib/python3/dist-packages/apport/fileutils.py", line 12, in <module>
    import os, glob, subprocess, os.path, time, pwd, sys, requests_unixsocket
  File "/usr/lib/python3/dist-packages/requests_unixsocket/__init__.py", line 1, in <module>
    import requests
  File "/usr/lib/python3/dist-packages/requests/__init__.py", line 95, in <module>
    from urllib3.contrib import pyopenssl
  File "/usr/lib/python3/dist-packages/urllib3/contrib/pyopenssl.py", line 46, in <module>
    import OpenSSL.SSL
  File "$HOME/.local/lib/python3.8/site-packages/OpenSSL/__init__.py", line 8, in <module>
    from OpenSSL import crypto, SSL
  File "$HOME/.local/lib/python3.8/site-packages/OpenSSL/crypto.py", line 1550, in <module>
    class X509StoreFlags(object):
  File "$HOME/.local/lib/python3.8/site-packages/OpenSSL/crypto.py", line 1570, in X509StoreFlags
    CB_ISSUER_CHECK = _lib.X509_V_FLAG_CB_ISSUER_CHECK
AttributeError: module 'lib' has no attribute 'X509_V_FLAG_CB_ISSUER_CHECK'

Original exception was:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "$HOME/.local/lib/python3.8/site-packages/OpenSSL/__init__.py", line 8, in <module>
    from OpenSSL import crypto, SSL
  File "$HOME/.local/lib/python3.8/site-packages/OpenSSL/crypto.py", line 1550, in <module>
    class X509StoreFlags(object):
  File "$HOME/.local/lib/python3.8/site-packages/OpenSSL/crypto.py", line 1570, in X509StoreFlags
    CB_ISSUER_CHECK = _lib.X509_V_FLAG_CB_ISSUER_CHECK
AttributeError: module 'lib' has no attribute 'X509_V_FLAG_CB_ISSUER_CHECK'
```
SOLUTION:
```
pip3 install pyopenssl==22.0.0
```
