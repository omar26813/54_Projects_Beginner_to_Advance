import requests
from bs4 import BeautifulSoup
import json
import csv
#for i in range(11)

json_dict=[]
csv_data=[]
for i in range(1,11):
    url=f"https://quotes.toscrape.com/page/{i}/"
    page=requests.get(url)
    #print(page.text)
    
    soup=BeautifulSoup(page.content, "html.parser")
    
    #print(soup.text)
    
    pages=soup.find_all("div", class_="quote")
    
    
    for  page in pages:
        quote=page.find("span", class_="text").get_text(separator=" ")
        author=page.find("small", class_="author").get_text(separator=" ").title()
        tags=[tag.get_text() for tag in page.find_all("a", class_="tag")]
        tags_str = ", ".join(tags)
    
    
        print(f'Quote-{i}\n{quote}')
        print(f'Author- {author}')    
        print(f'Tags:{tags_str}\n\n')
    
        csv_data.append([i, quote, author, tags_str])

        json_dict.append(    
        {    
            "Pages":i      ,
            "Quotes":quote ,   
            "Author":author ,   
            "Tags":tags    
    
    
        }    
    )    
    
with open("quote.json","w", encoding="utf-8") as f:
    json.dump(json_dict,f,ensure_ascii=False, indent=4,)    
    
# Save to CSV file
with open("quotes.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Page", "Quote", "Author", "Tags"])
    writer.writerows(csv_data)