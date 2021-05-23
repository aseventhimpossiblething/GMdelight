#https://pypi.org/project/tbselenium/
#"/path/to/TorBrowserBundle/"
#apt install tor
#sudo apt install torbrowser-launcher
#sudo apt remove torbrowser-launcher
#https://tor.stackexchange.com/questions/17308/how-to-install-tor-browser-through-command-line

"""
from argparse import ArgumentParser
from tbselenium.tbdriver import TorBrowserDriver 
from tbselenium.utils import start_xvfb, stop_xvfb
from os.path import join, dirname, realpath
"""
from argparse import ArgumentParser
from tbselenium.utils import start_xvfb, stop_xvfb
from tbselenium.tbdriver import TorBrowserDriver
from os.path import join, dirname, realpath

from selenium import webdriver
import geckodriver_autoinstaller


geckodriver_autoinstaller.install()  # Check if the current version of geckodriver exists
                                     # and if it doesn't exist, download it automatically,
                                     # then add geckodriver to path

xvfb_display = start_xvfb()
driver = webdriver.Firefox()
driver.implicitly_wait(10)
#driver.get("http://www.python.org")
bh="https://www.bulq.com/lots/search/?last_activated_at=2021-05-22T23:40:37.275Z&page=1"
driver.get(bh)
print("page_source")
print(driver.page_source)
#assert "Python" in driver.title
stop_xvfb(xvfb_display)

"""
out_img = join(dirname(realpath(__file__)), "headless_screenshot.png")
xvfb_display = start_xvfb()
with TorBrowserDriver('/home/manivannan/pythonexamle/selenium_example/tor-browser_en-US') as driver:
    driver.load_url("https://check.torproject.org")
    driver.get_screenshot_as_file(out_img)
    print("Screenshot is saved as %s" % out_img)

stop_xvfb(xvfb_display)
"""
"""
with TorBrowserDriver('/etc/tor') as driver:
    driver.load_url("https://check.torproject.org")
    driver.get_screenshot_as_file(out_img)
    print("Screenshot is saved as %s" % out_img)
"""
"""
xvfb_display = start_xvfb()
print("after with xfvb display command")
with TorBrowserDriver('/GMDelight/dependancies/akt/tor-browser_en-US') as driver:
    print("after with Tor Command command")
    #driver.load_url("https://check.torproject.org")
    #driver.load_url("https://ww.google.com")
    print(driver.get("https://ww.google.com").page_source)
    print("after driver load command")
    
stop_xvfb(xvfb_display)    
"""

"""
xvfb_display = start_xvfb()
#driver = webdriver.Firefox()
#driver=TorBrowserDriver('/GMDelight/dependancies/akt/tor-browser_en-US')
driver=TorBrowserDriver('/GMDelight/GMDelight/webtools/tor-browser_en-US')
driver.get("http://www.python.org")
print("page_source")
#print(driver.page_source)
assert "Python" in driver.title
stop_xvfb(xvfb_display)


xvfb_display = start_xvfb()
news="https://www.bulq.com/lots/search/?last_activated_at=2021-05-22T23:40:37.275Z&page=1"
print("page_source")
driver.get(news).implicit_wait(15);
#stop_xvfb(xvfb_display)

"""



