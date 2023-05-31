# AITestKitchen

AITestKitchen is an unofficial Python library that provides access to the cutting-edge Imagen neural network via a non-disabled developer API. It allows you to generate and manipulate images using the powerful and creative capabilities of Imagen that has not been officially released yet. This library lets you explore the amazing potential of this artificial intelligence tool, with an easy-to-use interface that requires minimal setup.

## Features

- Generate images based on textual prompts
- Upscale generated images in high quality
- Save and display images locally
- Adjust the number of images to generate
- Specify the demo type (BRAINSTORM, WOBBLE, CITY_DREAMER)

## Installation

```
git clone https://github.com/0x7o/AITestKitchen
cd AITestKitchen
pip install -r requirements.txt
```

## Usage

To use AITestKitchen, you'll need a valid access token (bearer token) provided by the [AI Test Kitchen](https://aitestkitchen.withgoogle.com/).

### Imagen example:

```python
from src import Imagen

bearer = "YOUR_ACCESS_TOKEN"
prompt = "3D render of a cute tropical fish in an aquarium on a dark blue background"
demo = "BRAINSTORM"
count = 2

img = Imagen(bearer)
images = img.generate(prompt, demo, count)

for idx, image in enumerate(images):
    image.upscale()
    image.save(f"{prompt.replace(' ', '_').lower()}{idx + 1}.png")
```

This example generates two images based on the given prompt and saves them to your local machine after upscaling.

See the [examples](examples) folder for more examples.
## Contributing

AITestKitchen is an open-source project, and contributions are welcome! If you'd like to contribute, feel free to fork the repository, make changes, and submit a pull request. We appreciate your help in making this library better and more accessible for everyone!

## Disclaimer

Please note that this library is not officially supported by the creators of Imagen or their API. It's developed as a third-party library, and any changes in the Imagen service, API, or terms of use are beyond our control. Use at your own risk and ensure you comply with any terms and conditions required by [AI Test Kitchen](https://aitestkitchen.withgoogle.com/).

## License

AITestKitchen is released under the MIT License. See the [LICENSE](LICENSE) file for more details.