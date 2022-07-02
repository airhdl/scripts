# -------------------------------------------------------------------------------
#
#  Convert a list of registers to an airhdl register map JSON object.
# 
#  Usage:
#    python regs2json.py input_file map_name
# 
#  Arguments:
#    input_file  path to a text file containing the register names (one name per line)
#    map_name    name of the register map to be created
# 
#  Output:
#    The script creates an out.json file in the current working directory.
#
# -------------------------------------------------------------------------------
#
#  Copyright (c) 2022 Guy Eschemann
# 
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
# 
#      http://www.apache.org/licenses/LICENSE-2.0
# 
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# -------------------------------------------------------------------------------

import sys
import json

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: python regs2json.py input_file map_name")
        sys.exit(-1)
    input_file = sys.argv[1]
    output_file = "out.json"
    registermap_name = sys.argv[2]
    with open(input_file, 'r') as f, open(output_file, 'w', encoding='utf8') as ff:
        result = {}
        result["jsonVersion"] = 2
        register_map = {}
        register_map["name"] = registermap_name
        register_map["description"] = ""
        register_map["width"] = 32
        register_map["baseAddress"] = 0x0
        register_map["addrWidthBits"] = 32
        register_map["revision"] = 1
        register_map["generateRecordPorts"] = False
        register_map["registers"] = []
        register_address = 0x0
        for line in f:
            register_name = line.strip()
            register = {}
            register["type"] = "Register"
            register["name"] = register_name
            register["description"] = ""
            register["access"] = "READ_WRITE"
            register["addressOffset"] = register_address
            register["size"] = 32
            register["fields"] = []
            field = {}
            field["name"] = "value"
            field["description"] = ""
            field["bitWidth"] = 32
            field["bitOffset"] = 0
            field["reset"] = 0
            field["selfClear"] = False
            register["fields"].append(field)
            register_map["registers"].append(register)
            register_address += 4
        result["registerMap"] = register_map
        json.dump(result, ff, indent=2)
