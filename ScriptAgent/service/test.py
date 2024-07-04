from schema import all_schema
import script_service
import subprocess
import BaseConfig
import os
import time

res=script_service.get_script()
print(res)

# print(os.getpid())
#
# res={
#     "command": "mynettest",
#     "arguments": [{"end":20},{"numbers":[30,40,50]}],
#     "pattern": "/My_test/pattern01",
#     "power": ""
# }
#
# ci=all_schema.CommandInfo(**res)
# script_service.get_script_process(ci)
# print(script_service.processList)
#
#
# time.sleep(3)
#
# script_service.stop_script(ci)

# script_target=BaseConfig.SCRIPTS_PATH+"/"+ci.command+".py"
#     args_target=ci.arguments
#     result = subprocess.run(['python', script_target], capture_output=True, text=True)
#     if result.returncode != 0:
#         print("Error:", result)
#     else:
#         print("Output:", result)