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
