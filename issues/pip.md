ISSUE:
```
. .venv/bin/activate; pip3 install  -e ".[cli,runtime,test,dev]"
Traceback (most recent call last):
  File "$HOME/localstack/.venv/bin/pip3", line 8, in <module>
    sys.exit(main())
  File "$HOME/localstack/.venv/lib/python3.10/site-packages/pip/_internal/cli/main.py", line 73, in main
    command = create_command(cmd_name, isolated=("--isolated" in cmd_args))
  File "$HOME/localstack/.venv/lib/python3.10/site-packages/pip/_internal/commands/__init__.py", line 96, in create_command
    module = importlib.import_module(module_path)
  File "/usr/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "$HOME/localstack/.venv/lib/python3.10/site-packages/pip/_internal/commands/install.py", line 24, in <module>
    from pip._internal.cli.req_command import RequirementCommand
  File "$HOME/localstack/.venv/lib/python3.10/site-packages/pip/_internal/cli/req_command.py", line 15, in <module>
    from pip._internal.index.package_finder import PackageFinder
  File "$HOME/localstack/.venv/lib/python3.10/site-packages/pip/_internal/index/package_finder.py", line 21, in <module>
    from pip._internal.index.collector import parse_links
  File "$HOME/localstack/.venv/lib/python3.10/site-packages/pip/_internal/index/collector.py", line 12, in <module>
    from pip._vendor import html5lib, requests
ImportError: cannot import name 'html5lib' from 'pip._vendor' ($HOME/localstack/.venv/lib/python3.10/site-packages/pip/_vendor/__init__.py)
make: *** [Makefile:50: install-dev] Error 1
```

SOLUTION:
```
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10
```
