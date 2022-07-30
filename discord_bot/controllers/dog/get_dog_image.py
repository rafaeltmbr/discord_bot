import httpx

DOG_API_URL = 'https://api.thedogapi.com/v1/images/search'

client = httpx.AsyncClient()

async def get_dog_image():
    response = await client.get(DOG_API_URL)
    images = response.json()
    return images[0]['url']