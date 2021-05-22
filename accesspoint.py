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

from tbselenium.utils import start_xvfb, stop_xvfb
from tbselenium.tbdriver import TorBrowserDriver
from os.path import join, dirname, realpath


"""
out_img = join(dirname(realpath(__file__)), "headless_screenshot.png")
xvfb_display = start_xvfb()
with TorBrowserDriver('/home/manivannan/pythonexamle/selenium_example/tor-browser_en-US') as driver:
    driver.load_url("https://check.torproject.org")
    driver.get_screenshot_as_file(out_img)
    print("Screenshot is saved as %s" % out_img)

stop_xvfb(xvfb_display)
"""

with TorBrowserDriver('/etc/tor') as driver:
    driver.load_url("https://check.torproject.org")
    driver.get_screenshot_as_file(out_img)
    print("Screenshot is saved as %s" % out_img)

