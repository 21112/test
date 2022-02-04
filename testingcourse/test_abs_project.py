import unittest
import pytest
import time
from selenium import webdriver
path = "E:\projects\mensamax\webdriver\chromedriver.exe"
browser = webdriver.Chrome(path)
# class TestAbs(pytest.TestCase):

def test_abs1():
    link = "http://suninjuly.github.io/registration1.html"
    browser.get(link)
    check1 = browser.find_element_by_css_selector("div.first_block > div.form-group.first_class > input")
    check1.send_keys("vgfdg")
    check2 = browser.find_element_by_css_selector("div.first_block > div.form-group.second_class > input")
    check2.send_keys("vgfdg")
    em = browser.find_element_by_css_selector("div.first_block > div.form-group.third_class > input")
    em.send_keys("gfdrs")
    p = browser.find_element_by_css_selector("div.second_block > div.form-group.first_class > input")
    p.send_keys("gfdrs")
    a = browser.find_element_by_css_selector("div.second_block > div.form-group.second_class > input")
    a.send_keys("gfdrs")
    btn = browser.find_element_by_class_name("btn-default")
    btn.click()
    time.sleep(2)
    cont = browser.find_element_by_tag_name("h1")
    # print(cont.text)
    assert cont.text == "Congratulations! You have successfully registered!"," No correkt"
    # self.assertEqual(abs(-42) , 42, "Should be absolute value of a number")
    # time.sleep(3)
    # browser.quit()

def test_abs2():
    link = "http://suninjuly.github.io/registration2.html"
    browser.get(link)
    check1 = browser.find_element_by_css_selector("div.first_block > div.form-group.first_class > input")
    check1.send_keys("vgfdg")
    check2 = browser.find_element_by_css_selector("div.first_block > div.form-group.second_class > input")
    check2.send_keys("vgfdg")
    em = browser.find_element_by_css_selector("div.first_block > div.form-group.third_class > input")
    em.send_keys("gfdrs")
    p = browser.find_element_by_css_selector("div.second_block > div.form-group.first_class > input")
    p.send_keys("gfdrs")
    a = browser.find_element_by_css_selector("div.second_block > div.form-group.second_class > input")
    a.send_keys("gfdrs")
    btn = browser.find_element_by_class_name("btn-default")
    btn.click()
    time.sleep(2)
    cont = browser.find_element_by_tag_name("h1")
    # print(cont.text)
    assert cont.text == "Congratulations! You have successfully registered!"," No correkt"
#     self.assertEqual(abs(-42) , -42, "Should be absolute value of a number")

if __name__ == "__main__":
    pytest.main()




