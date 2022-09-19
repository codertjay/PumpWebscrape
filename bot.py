import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://petrolpump.hpretail.in/location/karnataka"


class PetrolPump:
    def __init__(self, teardown=True):
        s = Service(ChromeDriverManager().install())
        self.options = webdriver.ChromeOptions()
        # self.options.add_argument('headless')
        self.teardown = teardown
        # keep chrome open
        self.options.add_experimental_option("detach", True)
        self.options.add_experimental_option(
            "excludeSwitches",
            ['enable-logging'])
        self.driver = webdriver.Chrome(
            options=self.options,
            service=s)
        self.driver.implicitly_wait(50)
        self.petrol_pumps = []
        super(PetrolPump, self).__init__()

    def __enter__(self):
        self.driver.get(BASE_URL)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.driver.quit()

    def land_first_page(self):
        self.driver.get(BASE_URL)

    def get_petrol_pumps(self):
        """
        this is used to loop through all petrol pump in a page and get their details but it is not getting  the detail
        """
        elements = self.driver.find_element(by=By.CSS_SELECTOR, value='div[class="outlet-list"]')
        #  the petrol pumps element
        petrol_pumps = elements.find_elements(by=By.CSS_SELECTOR, value='div[class="store-info-box"]')
        for item in petrol_pumps:
            # getting the value from each petrol pumps
            name = item.find_element(by=By.CSS_SELECTOR, value='li[class="outlet-alternate-name"]').find_element(
                value='div[class="info-text"]', by=By.CSS_SELECTOR).text
            address = item.find_element(by=By.CSS_SELECTOR, value='li[class="outlet-address"]').find_element(
                value='div[class="info-text"]', by=By.CSS_SELECTOR).text
            phone = item.find_element(by=By.CSS_SELECTOR, value='li[class="outlet-phone"]').find_element(
                value='div[class="info-text"]', by=By.CSS_SELECTOR).find_element(
                by=By.TAG_NAME, value="a").text
            open_hours = item.find_elements(by=By.TAG_NAME, value='li')[4].find_element(
                value='div[class="info-text"]', by=By.CSS_SELECTOR).text
            link = item.find_element(by=By.CSS_SELECTOR, value='a[class="btn btn-website"]').get_attribute('href')
            #  append all what we got
            self.petrol_pumps.append(
                {
                    "name": name,
                    "address": address,
                    "phone": phone,
                    "open_hours": open_hours,
                    "link": link,
                })
        with open("./petrol_pumps.json", "w+") as f:
            #  dump all the file
            f.write(json.dumps(self.petrol_pumps))
        print("Moving to the next page")
        if self.get_next_page():
            #  recall this function to loop again
            self.get_petrol_pumps()
        return True

    def get_petrol_pump_descriptions(self):
        with open("./petrol_pumps.json", "r+") as f:
            #  update the petrol pump once this function is called to
            #  use the one in the files which has been set from scraping
            self.petrol_pumps = json.load(f)
            count = 0
            for item in self.petrol_pumps:
                #  get the link from what we web scraped
                link = item.get("link")
                #  open the link to the description
                self.driver.get(link)
                description = self.driver.find_element(
                    by=By.CSS_SELECTOR,
                    value='div[class="about-text widthoutoffers"]').text
                #  update the description in the petrol pump
                self.petrol_pumps[count]["description"] = description
                # clear the existing file
                with open("./petrol_pumps.json", "w+") as f:
                    #  update it in the json file and use te update one
                    f.write(json.dumps(self.petrol_pumps))
                # update the count which enabling updating the description
                count += 1
        return True

    def get_next_page(self):
        try:
            self.driver.find_element(by=By.CSS_SELECTOR, value='li[class="next"]').find_element(by=By.TAG_NAME,
                                                                                                value="a").click()
            #   get the products in the next pages
            return True
        except:
            #  if error means no next page
            return False
