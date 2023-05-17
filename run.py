import ssl
import time
from urllib.request import urlopen

# Disable SSL certificate verification
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# Specify the URL
url = "https://www.merfolkslullaby.com/map?&tab=weather"

# Open the URL with SSL certificate verification disabled
page = urlopen(url, context=ssl_context)

# Wait for 10 seconds
time.sleep(10)

# Read the content of the page
content = page.read()
# Specify the output file name
output_file = "codeoutput.txt"

# Write the content to the output file with UTF-8 encoding
with open(output_file, "w", encoding="utf-8") as file:
    file.write(content.decode("utf-8"))

print(f"Output saved to '{output_file}'")