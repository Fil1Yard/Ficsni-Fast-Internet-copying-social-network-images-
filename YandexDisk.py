from progress.bar import IncrementalBar
import requests
import time
import json

class Yandex_disk:

    def __init__(self, token):
        self.token = token

    def create_folder(self, folder_name):
        URL = 'https://cloud-api.yandex.net:443/v1/disk/resources'
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        params = {'path': folder_name}
        response = requests.put(URL, headers=headers, params=params)
        if response.status_code == 201:
            print(f'Папка{folder_name} успешно создано')
            return True
        if response.status_code == 409:
            return False
        response.raise_for_status()

    def _upload_images(self, folder_name, file_name):
        URL = 'https://cloud-api.yandex.net:443/v1/disk/resources'
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        params = {'path': folder_name, 'overwrite': 'true', 'url': file_name}
        response = requests.post(URL, headers=headers, params=params)
        if response.status_code == 401:
            return False
            response.raise_for_status()
        return True

    def upload_images(self, photos_dict, folder_name):
        saved_photos_list = []
        bar = IncrementalBar('Файлов загружено', max=len(photos_dict))
