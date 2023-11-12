import requests
from bs4 import BeautifulSoup
print()
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}
url1 = "https://www.amazon.com.tr/Acer-AN515-58-544K-Bilgisayar%C4%B1-i5-12450H-NH-QFJEY-007/dp/B0C85RJPZT?ref_=Oct_d_obs_d_12601898031_5&pd_rd_w=sBD3K&content-id=amzn1.sym.83bd1466-2982-4d16-b5c7-b9664a0e2c4f&pf_rd_p=83bd1466-2982-4d16-b5c7-b9664a0e2c4f&pf_rd_r=XWAXAXSG2P4AMWGPTG62&pd_rd_wg=iPZmB&pd_rd_r=e7e83119-677f-4de2-960f-2467aa69b41d&pd_rd_i=B0C85RJPZT"


def getData(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup
soup = getData(url1)
product = soup.find("table", attrs={"class" : "a-normal a-spacing-micro"}).getText().strip()
price = soup.find("span",attrs={"class" : "a-price-whole"}).getText().strip().replace(",","")

print(f"Ürün Bilgileri: {product}  Ürün Fiyatı: {price}")
print()



