import requests
import time

class VK_ontakte:

    def get_images(self, vk_user_id, quantity=5):
        url = "https://api.vk.com/method/photos.get"
        params = {"access_token": TOKEN_VK, "v": '5.131', "owner_id": vk_user_id,
                  "extended": '1', "album_id": "profile", "count": quantity, "photo_sizes": 1
                  }
        res = requests.get(url, params=params).json()
        data = res['response']['items']
        photos_dict = {}
        for item in data:
            likes = str(item['likes']['count'])
            date = time.strftime('%Y-%B-%d %A-%H-%M-%S', time.localtime(item['date']))
            square = 0
            url = str()
            size = str()
            for element in item['sizes']:
                if element['height'] * element['width'] >= square:
                    square = element['height'] * element['width']
                    url = element['url']
                    size = element['type']
            if likes not in photos_dict:
                photos_dict[likes] = url, size
            else:
                photos_dict[f'{likes}{date}'] = url, size
            if len(photos_dict) == quantity:
                break
        return photos_dict
