from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
from selenium.webdriver.common.action_chains import ActionChains
import os
import time
import datetime

#TODO : handle logging
#TODO : remove elements which are ordered from file
#TODO : add quantities of items to buy

def login(browser):
	username = browser.find_element_by_name('username')
	password = browser.find_element_by_name('password')
	username.send_keys('kumariankita002@gmail.com')
	password.send_keys('ankita002')
	browser.find_element_by_name('Submit').click()
	print str(datetime.datetime.now()), ' : Logged in'
	return

def search(browser, keyword):
	print str(datetime.datetime.now()), ' : Searching for ', keyword
	search_box = browser.find_element_by_name('q')
	print str(datetime.datetime.now()), ' : Got search box'
	search_box.clear()
	print str(datetime.datetime.now()), ' : Search box cleared'
	search_box.send_keys(keyword)
	print str(datetime.datetime.now()), ': Sent keys'
	search_box.submit()
	print str(datetime.datetime.now()), ' : Search form submitted'
	return

def add_item(browser):
	print str(datetime.datetime.now()), ' : Adding item to cart'
	html_list = browser.find_element_by_class_name('uiv2-our-recommendations-list-box')
	items = html_list.find_elements_by_tag_name("li")
	for item in items:
		print item.text
	item = items[0]
	print 'TO BUY : ', item.text
	if len(item.find_elements_by_class_name('uiv2-add-button')) != 0:
		button = item.find_element_by_class_name('uiv2-add-button')
	else:
		return
	button.click()
	return

def get_min_total(browser):
	print str(datetime.datetime.now()), ' : Getting minimum amount required'
	basket_container = browser.find_element_by_class_name('uiv2-your-basket')
	container = browser.find_element_by_class_name('uiv2-total-cost-wrap')
	hover = ActionChains(browser).move_to_element(basket_container)
	hover.perform()
	time.sleep(5)
	free_delivery = basket_container.find_element_by_class_name('uiv2-get-free-delivery')
	time.sleep(3)
	f =free_delivery
	text = f.get_attribute('textContent')
	min_total = re.findall(r'\d+',text)
	min_total = float(min_total[0])
	return min_total

def get_my_total(browser):
	print str(datetime.datetime.now()), ' : Getting total amount'
	my_total = browser.find_element_by_class_name('uiv2-items-total-cost')
	#my_total = my_total[0]
	my_total = my_total.get_attribute('textContent')
	my_total = re.findall(r'\d+', my_total)
	my_total = float(my_total[0])
	return my_total

def go_to_checkout(browser):
	print str(datetime.datetime.now()), ' : Going to the checkout page'
	basket_container = browser.find_element_by_class_name('uiv2-your-basket')
	checkout_button = browser.find_elements_by_class_name('view_basket_checkout')
	button = checkout_button[1]
	#button.click()
	hover = ActionChains(browser).move_to_element(basket_container)
	hover.perform()
	button.click()
	return

def checkout(browser):
	print str(datetime.datetime.now()), ' : Checking out'
	checkout_button = browser.find_element_by_id('checkout')
	checkout_button.click()
	return

def notify(title, subtitle, message):
	print str(datetime.datetime.now()), ' : Notifying'
	t = '-title {!r}'.format(title)
	s = '-subtitle {!r}'.format(subtitle)
	m = '-message {!r}'.format(message)
	so = '-sound {!r}'.format('default')
	a = '-activate {!r}'.format('org.mozilla.firefox')
	os.system('terminal-notifier {}'.format(' '.join([m, t, s, so, a])))

def get_shopping_list():
	print str(datetime.datetime.now()), ': Getting shopping list'
	f = open('shopping_list', 'r')
	shopping_list = []
	for line in f:
		shopping_list.append(line)
	f.close()
	return shopping_list

def add(item):
	print str(datetime.datetime.now()), ' : Adding item to shopping list'
	f = open('shopping_list', 'a')
	item = item + '\n'
	f.write(item)
	f.close()
	return

if __name__ == '__main__':
	browser = webdriver.Firefox()
	browser.get('http://www.bigbasket.com/auth/login/')
	login(browser)
	shopping_list = get_shopping_list()
	shopping_list = [s.rstrip() for s in shopping_list]
	for item in shopping_list:
		time.sleep(10)
		search(browser, item)
		add_item(browser)
		time.sleep(10)
		browser.get('http://www.bigbasket.com/')
		time.sleep(5)
	time.sleep(5)
	my_min = get_min_total(browser)
	time.sleep(7)
	my_total = get_my_total(browser)
	if my_min <= my_total:
		go_to_checkout(browser)
		checkout(browser)
		notify('Confirmation', 'Order from BigBasket', 'Please confirm your order from browser')
		print 'DONE'
	else:
		notify('Order limit not reached yet', 'Add more items', 'The minimum amount required for free delivery is more than your total')


