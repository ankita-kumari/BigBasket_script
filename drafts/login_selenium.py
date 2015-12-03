from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
from selenium.webdriver.common.action_chains import ActionChains
import os

def place_order():
	browser = webdriver.Firefox()
	browser.get('http://www.bigbasket.com/auth/login/')
	username = browser.find_element_by_name('username')
	password = browser.find_element_by_name('password')
	username.send_keys('kumariankita002@gmail.com')
	password.send_keys('ankita002')
	browser.find_element_by_name('Submit').click()
	search_box = browser.find_element_by_name('q')
	search_box.clear()
	search_box.send_keys('apples')
	search_box.submit()
	html_list = browser.find_element_by_class_name('uiv2-our-recommendations-list-box')
	items = html_list.find_elements_by_tag_name("li")
	item = items[0]
	b = item.find_element_by_class_name('uiv2-add-button')
	b.click()
	basket_container = browser.find_element_by_class_name('uiv2-your-basket')
	free_delivery = basket_container.find_element_by_class_name('uiv2-get-free-delivery')
	free_delivery = basket_container.find_elements_by_class_name('uiv2-get-free-delivery')
	total = browser.find_elements_by_id('sub_total')
	f =free_delivery[0]
	text = f.get_attribute('textContent')
	min_total = re.findall(r'\d+',text)
	min_total = float(min_total[0])
	my_total = browser.find_elements_by_class_name('uiv2-items-total-cost')
	my_total = my_total[0]
	my_total = my_total.get_attribute('textContent')
	my_total = re.findall(r'\d+', my_total)
	my_total = my_total[0]
	my_total = float(my_total)
	checkout_button = browser.find_elements_by_class_name('view_basket_checkout')
	button = checkout_button[1]
	#button.click()
	hover = ActionChains(browser).move_to_element(basket_container)
	hover.perform()
	button.click()
	checkout_button = browser.find_element_by_id('checkout')
	checkout_button.click()

def notify(title, subtitle, message):
	t = '-title {!r}'.format(title)
	s = '-subtitle {!r}'.format(subtitle)
	m = '-message {!r}'.format(message)
	os.system('terminal-notifier {}'.format(' '.join([m, t, s])))
