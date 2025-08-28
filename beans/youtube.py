import uiautomator2 as u2
import time
from utils.process import ProcessApp
import random
from utils.random_string import generate_random_string

class Youtube:
    def __init__(self, app) -> None:
        self.processApp = ProcessApp()
        self.process(app)
  
    def process(self, app):
        # for i in range(500):
        #     self.processApp.process_all(self, "open", app, i)

        for i in range(21):
            self.processApp.process_all(self, "search", app, i)
        
        
    def search(self):
        # for i in range(20):
        d = u2.connect()
        d(text="YouTube").click()
        time.sleep(20)
        if d(resourceId="com.google.android.youtube:id/menu_item_1").exists:
            d(resourceId="com.google.android.youtube:id/menu_item_1").click()
            input_field = d(resourceId='com.google.android.youtube:id/search_edit_text')
            if input_field.exists:
            # 清空输入框（如果需要）
                input_field.clear_text()
            # 输入文本
            
                random_string = generate_random_string(6)
                # print(random_string)
                input_field.set_text(random_string)
                # print('Text input completed.')
                # Click the search button
                d.press("enter")
            else:
                # print('Input field not found.')
                pass
            time.sleep(10)
            d(description="转到上一层级").click()
            time.sleep(2)
            d.app_stop('com.google.android.youtube')
            time.sleep(1)
        else: 
            d.app_stop('com.google.android.youtube')
            time.sleep(1)



        
