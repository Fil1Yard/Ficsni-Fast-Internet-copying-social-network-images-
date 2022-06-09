from YandexDisk import Yandex_disk
from VKontakte import VK_ontakte
import requests
import time

TOKEN_YANDEX = "AQAAAABB2LhNAADLW13hgmCKFkipuqBAjwFBZq4"
TOKEN_VK = "a67f00c673c3d4b12800dd0ba29579ec56d804f3c5f3bbcef5328d4b3981fa5987b951cf2c8d8b24b9abd"

class Yandex_disk:

    def __init__(self, token):
        self.token = token

    def get_header_yandex(self):
        return {
            'Accept': 'application/json',
            'Authorization': f'OAuth {TOKEN_YANDEX}'
        }

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




if __name__ == "__main__":
    ya = Yandex_disk('AQAAAABB2LhNAADLW13hgmCKFkipuqBAjwFBZq4')
    print(ya)




