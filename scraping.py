# Scraping 123
import requests  
from bs4 import BeautifulSoup  

# Step 1: Send a GET request to the website  
url = 'https://example.com/news'  # Replace with the target website URL  
response = requests.get(url)  

# Step 2: Check if the request was successful  
if response.status_code == 200:  
    # Step 3: Parse the page content  
    soup = BeautifulSoup(response.content, 'html.parser')  
    
    # Step 4: Find all article titles (replace 'h2' and 'title-class' with actual HTML tags/classes)  
    titles = soup.find_all('h2', class_='title-class')  

    # Step 5: Print the titles  
    for title in titles:  
        print(title.get_text(strip=True))  
else:  
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")  