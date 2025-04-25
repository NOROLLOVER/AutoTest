import yaml

from config.system import FILE_PATH


def read_yaml(file_path):
    """
    读取yaml文件
    :return:
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            yaml_data = yaml.safe_load(f)
    except Exception as e:
        print(f"文件读取异常，原因：{e}")
    return yaml_data


def write_yaml(value):
    """
    写入yaml文件
    :param file_path:
    :param value:
    :return:
    """

    file_path = FILE_PATH["extract"]
    if not file_path:
        with open(file_path,"w"):
            pass
    try:
        if isinstance(value, dict):
            with open(file_path, "a", encoding="utf-8") as f:
                write_data = yaml.dump(value)
                f.write(write_data)
        else:
            print("请写入dict类型数据")
    except Exception as e:
        print(f"文件写入异常，原因{e}")


if __name__ == '__main__':
    value = {"123": "456"}
    write_yaml(value)
    read_yaml(".././extract_data.yaml")
