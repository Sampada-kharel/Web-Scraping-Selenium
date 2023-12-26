import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



url="https://appbrewery.github.io/Zillow-Clone/"
response=requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

#creating list of links
link_info=soup.select(".StyledPropertyCardPhotoBody a")
link_data=[link['href'] for link in link_info]
print(link_data)

#creating list of address
address_info=soup.select(".StyledPropertyCardDataWrapper address")
address_data=[address.get_text().replace("|","").strip() for address in address_info]
print(address_data)



#creating list of price
price_info=soup.select(".PropertyCardWrapper__StyledPriceLine")
price_data=[price.get_text().replace("/mo","").replace("$","").split("+")[0] for price in price_info]
print(price_data)


#keeps browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)


for n in range(len(link_data)):

 driver.get("https://docs.google.com/forms/d/e/1FAIpQLSflUbgHvH9B72-OAUorfoiiZcAjM6HjWIcPZi0TnNo5CDLMmA/viewform")
 WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
 first_question=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
 second_question=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
 third_question=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
 Submit=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

 first_question.send_keys(address_data[n])
 second_question.send_keys(price_data[n])
 third_question.send_keys(link_data[n])
 Submit.click()

