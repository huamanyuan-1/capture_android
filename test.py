import uiautomator2 as u2
from uiautomator2 import Direction
import time
from utils.process import ProcessApp
from utils.random_string import generate_random_string
         
def repost():
    # for i in range(20):
    d = u2.connect()
    d.app_start("xyz.blueskyweb.app",stop=True)
    if not d.xpath("(//com.horcrux.svg.GroupView)[9]").exists:
        d.xpath("(//com.horcrux.svg.GroupView)[7]").click()

    d.sleep(10)
    # d.xpath('//*[@resource-id="tv.twitch.android.app:id/bottom_navigation"]/android.widget.LinearLayout[1]/android.widget.FrameLayout[5]/android.widget.ImageView[1]').click()
    flag=True
    while(flag):
        if not d.xpath('//*[@resource-id="repostBtn"]').exists:
            d.swipe_ext(Direction.FORWARD)
            d.sleep(1)
            print("===========swiping==========")
        else:
            d.xpath('//*[@resource-id="repostBtn"]').click()
            print("==========reposting===========")
            flag=False
    d.sleep(1)
    d.xpath('//*[@content-desc="转发"]').click()
    d.sleep(10)
    d.app_stop('xyz.blueskyweb.app')

if __name__=="__main__":
    repost()

        
