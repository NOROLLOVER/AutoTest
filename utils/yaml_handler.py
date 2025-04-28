import yaml

from configs.setting import FILE_PATH


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
        with open(file_path, "w"):
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


def extract_yaml(node_name, sub_node_name=None):
    file_path = None
    try:
        file_path = FILE_PATH["extract"]
        with open(file_path, "r", encoding="utf-8") as file:
            yaml_file = yaml.safe_load(file)
            if node_name is not None:
                result = yaml_file.get(node_name, {})
                if sub_node_name is not None:
                    return result.get(sub_node_name)
                else:
                    return result
            else:
                return {}
    except KeyError:
        print("yaml文件不存在")
        return {}
    except FileNotFoundError:
        print(f"文件{file_path}不存在")


def main(text: list) -> dict:
    if not isinstance(text, list):
        return {
            "result": "输出必须是一个列表"
        }
    data = []
    for item in text:
        if not isinstance(item, dict) or "content" not in item:
            return {
                "result": "不是字典或不包含 \"content\" 键"
            }
        i = item["content"]
        data.append(i)
    return {
        "result": data
    }


if __name__ == '__main__':
    # value = {"123": "456"}
    # write_yaml(value)
    # read_yaml(".././extract.yaml")

    print(extract_yaml("user_id", "user_ids"))
