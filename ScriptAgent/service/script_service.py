import subprocess
from schema.all_schema import CommandInfo
import BaseConfig
# 运行脚本
# command是脚本文件名称
# args是脚本参数
def run_script(ci: CommandInfo):
    script_target=BaseConfig.SCRIPTS_PATH+"/"+ci.command+".py"
    args_target=ci.arguments
    result = subprocess.run(['python', script_target], capture_output=True, text=True)
    if result.returncode != 0:
        print("Error:", result)
    else:
        print("Output:", result)

# 向数据库中添加新的脚本
def add_script(command,args):
    pass
