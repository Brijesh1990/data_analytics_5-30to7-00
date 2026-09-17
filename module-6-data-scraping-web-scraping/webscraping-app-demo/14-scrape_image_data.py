import requests
from bs4 import BeautifulSoup
import pandas as pd
# get url for scrap data 
url="https://examples-app-eta.vercel.app/gallery.html"
response=requests.get(url)
soup=BeautifulSoup(response.text, "html.parser")
# Create empty list to store image data
images_data = []
# get text of urls 
images=soup.find_all("img")
for image in images:
    src=image.get("src")
    alt=image.get("alt")
    
    print("Images :",src)
    print("Alt :",alt)
    
    images_data.append({
        "Images":src,
        "Alt":alt
    })
    
# Create DataFrame AFTER the loop
df = pd.DataFrame(images_data)

# Display DataFrame
print("\nDataFrame:")
print(df.to_string(index=False))

# --------------------------------
# Export to CSV
# --------------------------------
df.to_csv(
    "images_list.csv",
    index=False,
    encoding="utf-8"
)

# --------------------------------
# Export to Excel
# --------------------------------
df.to_excel(
    "images_list.xlsx",
    index=False,
    engine="openpyxl"
)

# --------------------------------
# Export to JSON
# --------------------------------
df.to_json(
    "images_list.json",
    orient="records",
    indent=4,
    force_ascii=False
)

print("\n===================================")
print("Files exported successfully!")
print("CSV   : images_list.csv")
print("Excel : images_list.xlsx")
print("JSON  : images_list.json")
print("===================================")


    
    
    


