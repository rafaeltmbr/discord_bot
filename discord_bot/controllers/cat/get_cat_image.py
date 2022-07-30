import httpx

CAT_API_URL = 'https://api.thecatapi.com/v1/images/search'

client = httpx.AsyncClient()

async def get_cat_image():
    response = await client.get(CAT_API_URL)
    images = response.json()
    return images[0]['url']