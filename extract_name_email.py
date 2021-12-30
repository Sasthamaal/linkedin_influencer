from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(chrome_options=options)

url_2="https://www.linkedin.com/login"
driver.get(url_2)
time.sleep(1)
try:
    sign_in=driver.find_element('//button[@data-tracking-control-name="auth_wall_desktop_company-login-toggle"]')
    sign_in.click()
except:
    t1=1
try:
    username=driver.find_element_by_class_name('login-email')
except:
    username=driver.find_element_by_id('username')
username.send_keys('rajasekhar.itla@gmail.com')
# username.send_keys('hrishi.moglix@gmail.com')

try:
    password=driver.find_element_by_class_name('login-password')
except:
    password=driver.find_element_by_id('password')
password.send_keys('rajasekhar1992')
# password.send_keys('testaccount1')
login= driver.find_element_by_xpath('//button[@type="submit"]')
login.click()


with open('profile_urls.txt', 'r') as fopen:
    for line in fopen:
        stripped_line = line.strip()
        profile_url = stripped_line
        # num_followers = 0
        # if ',' in stripped_line:
        #     profile_url = stripped_line.split(',')[0]
        #     num_followers = stripped_line.split(',')[1]
        driver.get(profile_url)

        content = driver.page_source
        soup = BeautifulSoup(content)
        time.sleep(3)
    # name = soup.findAll('div', attrs={'class':'text-heading-xlarge inline t-24 v-align-middle break-words'})
    # print(name[0].text)
        names = soup.find_all(attrs={"class" : "text-heading-xlarge inline t-24 v-align-middle break-words"})

        # print("name: ", names[0].text)
        # print("url: ", profile_url)

        taglines = soup.find_all(attrs={"class":"text-body-medium break-words"})
        # print("Bio: ", taglines[0].text.strip())

        # talksabout = soup.find_all(attrs={"class":"text-body-small t-black--light break-words pt1"})
        # print("talks about: ", talksabout[0].text.strip())
        # print(names[0].text,'\t',profile_url,'\t',taglines[0].text.strip(),'\t',num_followers)
        print(names[0].text,'\t',profile_url,'\t',taglines[0].text.strip())

