from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options();
options.add_argument("--headless");

driver = webdriver.Firefox(firefox_options=options);

driver.get("http://www.google.com/");
driver.quit();