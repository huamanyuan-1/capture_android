import uiautomator2 as u2
import time
from utils.process import ProcessApp
from utils.random_string import generate_random_string

        

        
class Reddit:
    def __init__(self, app) -> None:
        self.processApp = ProcessApp()
        self.process(app)
  
    def process(self, app):
        # count = int(count)
        # for i in range(500):
            # self.processApp.process_all(self, "open", app, i)

        for i in range(21):
            self.processApp.process_all(self, "search", app, i)

        
    def search(self):
        d = u2.connect()
        d(text="Reddit").click()
        time.sleep(15)

        # d(description="Search").click()
        d.click(795, 78)
        time.sleep(1)
        random_string = generate_random_string(6)
        d.send_keys(random_string, clear=True)
        # d.press("enter")
        time.sleep(2)
        # d.press("search")
        d.click(555, 1572)
        # d(resourceId="query_prompt_item").click()
        time.sleep(5)
        d.click(53, 87)
        # d(description="Back").click()
        time.sleep(1)
        
        d.app_stop('com.reddit.frontpage')
        time.sleep(1)