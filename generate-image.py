import openai
import urllib.request
import time
import re
import sys

def replace_non_alphanumeric(input_string):
	return re.sub(r'[^a-zA-Z0-9_]', '_', input_string)

if len(sys.argv) < 2:
    print("Usage: python3", sys.argv[0], "<prompt>")
    sys.exit(1)

prompt = sys.argv[1]

response = openai.Image.create(
  prompt=prompt,
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']

current_time = time.strftime("%Y%m%d-%H%M%S")
pr=replace_non_alphanumeric(prompt)
filename = 'output-' + current_time + '_' + pr + '.png'
urllib.request.urlretrieve(image_url, filename)

print(filename)
