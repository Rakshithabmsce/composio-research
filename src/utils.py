import json
import os


def ensure_dir(path):

    if not os.path.exists(path):

        os.makedirs(path)


def save_json(path, data):

    with open(path, "w", encoding="utf8") as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )


def load_json(path):

    with open(path, encoding="utf8") as f:

        return json.load(f)