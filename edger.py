from com.dtmilano.android.viewclient import ViewClient
import random
import time
import multiprocessing
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys

rand_num = random.randint(1, 10000000)


def pc(seed):

    driver = webdriver.ChromiumEdge()

    driver.get(f"https://www.bing.com/search?q={seed}, please log in")
    driver.find_element(By.ID, "id_a").click()

    time.sleep(3)
    for i in range(34):
        driver.get(f"https://www.bing.com/search?q={seed} search number {i + 1}")


def phone(seed):

    device, serialno = ViewClient.connectToDeviceOrExit()
    vc = ViewClient(device, serialno)
    device.startActivity(component='com.microsoft.bing/com.microsoft.sapphire.app.main.SapphireMainActivity')
    vc.dump(sleep=1)
    vc.findViewWithText("Search or type URL").touch()
    vc.dump(sleep=1)

    inp = vc.findViewWithText("Search or type URL")
    device.type(f"{seed} search ")
    for i in range(20):
        device.type("I\n")
        time.sleep(2)
        inp.touch()
        time.sleep(1)


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--pc" in args:
        p1 = multiprocessing.Process(target=pc, args=(rand_num,))
        p1.start()
    if "--phone" in args:
        p2 = multiprocessing.Process(target=phone, args=(rand_num, ))
        p2.start()
