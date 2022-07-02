# regs2json.py

Convert a list of registers to an airhdl register map JSON object.

```
Usage:
  python regs2json.py input_file map_name

Arguments:
  input_file  path to a text file containing the register names (one name per line)
  map_name    name of the register map to be created

Output:
  The script creates an out.json file in the current working directory.
```

The script reads a list of register names from a text file such as the one in [test/registers.txt](test/registers.txt) and generates a register map JSON object that can be uploaded to [airhdl.com](https://airhdl.com) or used as an input to the airhdl [command line generator](https://airhdl.com/#/products). The output file, which is called `out.json`, is created in the current working directory. An example output file is available under [test/out.json](test/out.json).