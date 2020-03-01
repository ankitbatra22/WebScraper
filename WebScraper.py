import requests
from bs4 import BeautifulSoup


URL = input("Enter Your Amazon product URL!")

# headers = "ENTER YOUR COMPUTERS USER AGENT HERE"

SCOPES = ["https://mail.google.com/"]




def check_price():
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()

    price = soup.find(id= "priceblock_ourprice").get_text()

    index = price.index("\xa0")

    finalprice = price[index:]
    print(finalprice)

    price = str(price)
    lister = price.split(" ")
    print(lister)
    for x in lister:
        y = valuedate(x)
        if y is None:
            continue
        else:
            break
    converted_price = y
    print(y)



    print("Current price of selected product is:$",finalprice)
    return (title.strip())

check_price()


























   # lister = price.split(" ")
  #  converted_price = (lister[1])
  #  print(converted_price)

#    converted_price = float(price[5:11])

   # tempIndexStart = 0
  #  tempIndexEnd = 0
#
    #for i in range(len(price)):
  #      if price[i] == " ":
# #       if price[i] == " ":
       #     tempIndexEnd = i - 1

  #  converted_price = (price[tempIndexStart:tempIndexEnd])


  #  if (converted_price < 320):
 #       send_mail()