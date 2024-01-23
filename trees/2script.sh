#!/usr/bin/bash
rm run.py
touch run.py
chmod +x run.py
echo "#!/usr/bin/python3">run.py
cat "__init__.py">>"run.py"
cat "command_mode.py">>"run.py"
./run.py
