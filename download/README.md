# download.py

Download generated files from [airhdl.com](https://airhdl.com)

```
Usage:
   python download.py register_map_id file_type

 Arguments:
   register_map_id  ID of the airhdl register map
   file_type        type of the file to download (e.g. dlComponent)

 Example:
   python download.py 176820 vhdlComponent
```

The `register_map_id` argument is the ID of the airhdl register map, which you can extract from the URL of the corresponding register map view in `airhdl.com`. For example the register map view at `https://airhdl.com/#/registerMap/176820` corresponds to the register map ID `176820`.

List of supported values for the `file_type` argument:

| `file_type` | Description |
| ----------- | ----------- |
| `cHeader` |  C header |
| `cppHeader` | C++ header |
| `svPackage` | SystemVerilog package |
| `svModule` | SystemVerilog module |
| `svTestbench` | SystemVerilog testbench | 
| `vhdlPackage` | VHDL package |
| `vhdlComponent` | VHDL component |
| `vhdlInstance` | VHDL instantiation template |
| `vhdlTestbench` | VHDL testbench |
| `htmlDoc` | HTML documentation |
| `mdDoc` | Markdown documentation |
| `ipxact` | IP-XACT XML | 
| `json` | JSON |
| `all` | all files (zip archive) |

In your local copy of the `download.py` script, please make sure to update the following variables with your `airhdl.com` credentials before using the script:

```python
USERNAME = "XXX"
PASSWORD = "XXX"
```
