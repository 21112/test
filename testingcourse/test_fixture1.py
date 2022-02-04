from selenium import webdriver
path = "E:\projects\mensamax\webdriver\chromedriver.exe"
import time
link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1():

    
    def setup_class(self):
        print("\nstart browser for test 11111111suite..")
        self.browser = webdriver.Chrome(path)

    
    def teardown_class(self):
        print("quit browser for test 1111111111suite..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        print("YYYYYYYYYYYYYYYYYYYY")
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")


class TestMainPage2():
    
    
    def setup_method(self):
        print("start browser for 222222222test..")
        self.browser = webdriver.Chrome(path)
    
    def teardown_method(self):
        print("quit browser for 2222222222test..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")