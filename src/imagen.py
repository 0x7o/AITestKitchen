from io import BytesIO
from PIL import Image
import requests
import base64
import uuid


class Imagen:
    def __init__(self, bearer) -> None:
        self.bearer = bearer
        self.domain = "https://content-aisandbox-pa.googleapis.com"
        self.headers = {
            "Authorization": f"Bearer {self.bearer}",
            "Content-Type": "application/json",
        }

    def generate(self, prompt: str, demo: str, count: int) -> list:
        data = {
            "demo": demo,
            "imageCount": count,
            "query": prompt,
            "sessionId": str(uuid.uuid4()),
            "imageSpec": {"inlineUpscale": False},
        }
        response = requests.post(
            f"{self.domain}/v1:imageDemo?alt=json", headers=self.headers, json=data
        )
        if response.status_code == 200:
            return [
                Img(image["imageData"], image["imageId"], self)
                for image in response.json()["images"]
            ]
        else:
            raise Exception(f"Error: {response.json()['error']['message']}")


class Img:
    def __init__(self, base: str, id: str, imagen: Imagen) -> None:
        self.id = id
        self.image = Image.open(BytesIO(base64.b64decode(base)))
        self.imagen = imagen

    def save(self, path: str) -> None:
        self.image.save(path)

    def show(self) -> None:
        self.image.show()

    def upscale(self) -> None:
        response = requests.post(
            f"{self.imagen.domain}/v1:upscaleImage?alt=json",
            headers=self.imagen.headers,
            json={
                "imageId": self.id,
            },
        )
        if response.status_code == 200:
            self.image = Image.open(
                BytesIO(base64.b64decode(response.json()["image"]["imageData"]))
            )
        else:
            raise Exception(f"Error: {response.json()['error']['message']}")
