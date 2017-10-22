import json
from einstein.vision.dataset import DataSet
from einstein.constants import ACCESS_TOKEN
from einstein.constants import TYPE_IMAGE


def main():
    access_token = ACCESS_TOKEN
    dataset = DataSet(access_token=access_token)
    path = 'http://metamind.io/images/mountainvsbeach.zip'
    response = dataset.create_dataset(path, TYPE_IMAGE)
    print(json.dumps(response, indent=4, sort_keys=True))

if __name__ == "__main__":
    main()
