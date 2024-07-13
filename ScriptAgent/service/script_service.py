# 创建子进程运行脚本
import os
import signal
import subprocess
# 信息传输类
from schema.all_schema import CommandInfo
# 根路径
import BaseConfig
# yaml配置格式读取
import yaml

# 管理运行的脚本
processList = {}


# 运行脚本
# command是脚本文件名称
# args是脚本参数
def get_script_name(ci: CommandInfo, dirName="My_test"):
    script_target = BaseConfig.SCRIPTS_PATH + "/" + dirName + "/" + ci.pattern + "/" + ci.command + ".py"
    return script_target

def run_script(ci: CommandInfo):
    script_target = get_script_name(ci)
    result = subprocess.run(['python', script_target], capture_output=True, text=True)
    if result.returncode != 0:
        print("Error:", result)
    else:
        print("Output:", result)


def get_script_process(ci: CommandInfo):
    script_target = get_script_name(ci)
    print(ci)
    arg_list = []
    for item in ci.arguments:
        res = item.items()
        for key, value in res:
            arg_list.append("--" + key)
            if type(value) is list:
                for v in value:
                    arg_list.append(str(v))
            if type(value) is int or type(value) is str:
                arg_list.append(str(value))
    command = ["python", script_target] + arg_list
    print(command)
    result = subprocess.Popen(command, start_new_session=True, )
    print(result.pid)
    global processList
    processList[script_target] = result


# 停止脚本
# 根据CommandInfo停止脚本,只需要command与pattern对应即可
def stop_script(ci: CommandInfo):
    global processList
    print(processList)
    processName = get_script_name(ci)
    print(processName)
    nameList = processList.keys()
    if processName in nameList:
        os.kill(processList[processName].pid, signal.SIGTERM)
        processList.pop(processName)

# 根据配置文件获取全部的脚本信息
def get_script(config_file="config"):
    config_target = BaseConfig.SCRIPTS_PATH + "/" + config_file + ".yaml"
    with open(config_target, encoding="utf-8") as f:
        config = yaml.safe_load(f)

    for item in config['config']['patterns']:
        for command in item['pattern']['commands']:
            for idx,file in enumerate(command["command"]["files"]):
                command["command"]["files"][idx]=file[0:-3]
        #     item['pattern']['files'][idx] = file[0:-3]
    return config
