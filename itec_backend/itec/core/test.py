# import requests
# url = 'https://api.openai.com/v1/images/generations'

# key = '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'
# data = {
#     "model": "image-alpha-001",
#     "prompt": "a bird made of flowers",
#     "api_key": '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'
#     Authorization: Bearer YOUR_KEY
# }

# response = requests.post(url, json=data)

# # image_url = response.json()['data'][0]['url']
# print(response.json())
import requests
url = 'https://api.openai.com/v1/images/generations'
data = {
    'model': 'image-alpha-001',
    'prompt': 'a bird made of flowers',
    'num_images': 1,
    'size': '512x512',
}
headers = {
    'Authorization': 'Bearer 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',
}

response = requests.post(url, json=data, headers=headers)
print(response.json()['data'][0]['url'])