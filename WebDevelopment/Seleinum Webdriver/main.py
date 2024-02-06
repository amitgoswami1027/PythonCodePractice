from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/Portable-Mechanical-Keyboard-MageGee-Backlit/dp/B098LG3N6R/ref=sr_1_1?_encoding=UTF8&content-id=amzn1.sym.12129333-2117-4490-9c17-6d31baf0582a&keywords=gaming+keyboard&pd_rd_r=8a65bb11-8339-4d57-bbcb-f8a2c49efa83&pd_rd_w=C0BBr&pd_rd_wg=st1iC&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=6F3XXPTP3XRMAPAQQG6P&qid=1707183362&sr=8-1")

#driver.close()
price_dollar= driver.find_element(By.CLASS_NAME,value="a-price-whole")
price_cent= driver.find_element(By.CLASS_NAME,value="a-price-fraction")

print(f"The price is {price_dollar.text}.{price_cent.text}")
driver.quit()



