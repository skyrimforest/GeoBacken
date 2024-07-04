import yaml
import json

if __name__ == '__main__':
    with open('config.yaml',encoding="utf-8") as f:
        config = yaml.safe_load(f)
        print(config)
