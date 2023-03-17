ISSUE:
```
/usr/lib/python3/dist-packages/paramiko/transport.py:219: CryptographyDeprecationWarning: Blowfish has been deprecated
  "class": algorithms.Blowfish,
```

SOLUTION:
```
pip3 install paramiko==2.11.0
```
