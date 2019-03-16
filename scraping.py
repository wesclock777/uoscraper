from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver import ActionChains

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=/home/wesley/.config/google-chrome/") #Path to your chrome profile
try:
    driver = webdriver.Chrome(chrome_options = options)
except Exception as e:
    pass
driver.get("https://www.freepeople.com")

def wait_to_complete_id(driver):
    return

def login(driver):
    driver.get("https://www.urbanoutfitters.com/login?url=/account/dashboard")
    email = driver.find_element_by_id("email")
    password = driver.find_element_by_id("password")
    submit = driver.find_element_by_css_selector("button[type='submit']")
    email.send_keys("wesleyklock@gmail.com")
    password.send_keys("appletree")
    submit.click()

def OU(driver):
    cat = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[1]/div/div[3]/div/div/nav/ul/li[1]/a/span")


    # hover over the women's category
    cat.click()
    links= [
        #"https://www.urbanoutfitters.com/dresses",
        #"https://www.urbanoutfitters.com/womens-tops",
        #"https://www.urbanoutfitters.com/jackets-coats-for-women",
        #"https://www.urbanoutfitters.com/womens-bottoms",
        #"https://www.urbanoutfitters.com/womens-intimates",
        #"https://www.urbanoutfitters.com/womens-swimwear",
        #"https://www.urbanoutfitters.com/vintage-womens-clothing",
        #"https://www.urbanoutfitters.com/womens-beauty-products",
        #"https://www.urbanoutfitters.com/women-accessories",
        "https://www.urbanoutfitters.com/shoes-for-women",
        "https://www.urbanoutfitters.com/graphic-tees-for-men",
        "https://www.urbanoutfitters.com/mens-tops",
        "https://www.urbanoutfitters.com/mens-jackets",
        "https://www.urbanoutfitters.com/mens-bottoms",
        "https://www.urbanoutfitters.com/mens-suits",
        "https://www.urbanoutfitters.com/mens-shoes",
        "https://www.urbanoutfitters.com/mens-accessories",
        "https://www.urbanoutfitters.com/underwear-socks-for-men",
        "https://www.urbanoutfitters.com/vintage-mens-clothing",
        "https://www.urbanoutfitters.com/mens-grooming",
        "https://www.urbanoutfitters.com/bedding",
        "https://www.urbanoutfitters.com/furniture",
        "https://www.urbanoutfitters.com/apartment-room-decor",
        "https://www.urbanoutfitters.com/rugs-curtains",
        "https://www.urbanoutfitters.com/lighting",
        "https://www.urbanoutfitters.com/dinnerware",
        "https://www.urbanoutfitters.com/bathroom-decor",
        "https://www.urbanoutfitters.com/vintage-home-decor",
        "https://www.urbanoutfitters.com/vinyl-records-cassettes",
        "https://www.urbanoutfitters.com/audio",
        "https://www.urbanoutfitters.com/cameras-film",
        "https://www.urbanoutfitters.com/cell-phone-accessories",
        "https://www.urbanoutfitters.com/stationery-desk-supplies",
        "https://www.urbanoutfitters.com/party-supplies-games",
        "https://www.urbanoutfitters.com/pet-supplies-accessories",
        "https://www.urbanoutfitters.com/wellness-products",
        "https://www.urbanoutfitters.com/skate-shop",
        "https://www.urbanoutfitters.com/makeup",
        "https://www.urbanoutfitters.com/skin-care-products",
        "https://www.urbanoutfitters.com/perfume-fragrance",
        "https://www.urbanoutfitters.com/bath-body-products",
        "https://www.urbanoutfitters.com/hair-products",
        "https://www.urbanoutfitters.com/nail-products",
        "https://www.urbanoutfitters.com/health-wellness-products",
        "https://www.urbanoutfitters.com/beauty-makeup-accessories",
        "https://www.urbanoutfitters.com/mens-grooming-products",
        "https://www.urbanoutfitters.com/makeup-gift-sets"
    ]

    for link in links:
        item_links=[]
        driver.get(link)
        pages = driver.find_element_by_xpath("//*[@id='u-skip-anchor']/div[2]/div[1]/div[2]/div[2]/div/nav/ul/li[4]")
        pages = int(pages.get_attribute("innerHTML"))
        print(pages)
        for i in range(pages):
            items = driver.find_element_by_xpath("//*[@id='u-skip-anchor']/div[2]/div[2]")
            items = items.find_elements_by_css_selector("meta[itemprop='url']")
            for item in items:
                actions = ActionChains(driver)
                actions.move_to_element(item).perform()
                item_links.append(item.get_attribute("content"))
            driver.get(link+"?page="+str(i+2))

        subcat = link.split("/")[-1]
        f = open("data/"+subcat+".txt", "w")
        for l in item_links:
            f.write(l+"\n")
login(driver)
OU(driver)
