from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def scrape_terumo():
    # use incognito mode
    options = webdriver.ChromeOptions()
    options.add_argument(' -- incognito')

    browser = webdriver.Chrome(chrome_options=options)

    url = 'https://www.terumo.co.jp/medical/index.html'

    # open the url
    browser.get(url)

    timeout = 10

    try:
        WebDriverWait(browser, timeout).until(
        EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="nonMemberLoginLink"]')
        )
        )

    except TimeoutException:
        print('Timed Out Waiting for page to load')
        browser.quit()

    # click the yes button
    yes_btn = browser.find_element_by_xpath('//*[@id="nonMemberLoginLink"]')
    yes_btn.click()

    browser.implicitly_wait(3)

    # get top news list
    top_news = browser.find_element_by_class_name('topNewsList')
    link_elems = top_news.find_elements_by_css_selector('.topNewsList [href]')
    news_date_and_text_list = top_news.text.split('\n')
    links_list = [elem.get_attribute('href') for elem in link_elems]

    return news_date_and_text_list, links_list
