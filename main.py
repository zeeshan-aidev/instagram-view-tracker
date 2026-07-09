from browser import start_browser
from instagram import *

driver=start_browser()

url="https://www.instagram.com/missyazminxdo/reels/"

open_reels(driver,url)

scroll_to_bottom(driver)

posts=count_reels(driver)

views=get_total_views(driver)

print("="*40)
print("Posts :",posts)
print("Views :",views)
print("="*40)

input("Press ENTER...")

driver.quit()