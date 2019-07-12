import yaml


def get_list():
    with open("../data/data.yaml", "r") as f:
        return yaml.load(f)


if __name__ == '__main__':
    list = []
    for i in get_list().values():
        list.append(tuple(i.values()))
        print(list)