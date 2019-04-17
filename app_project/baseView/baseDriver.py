class BaseDriver(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *args):
        return self.driver.find_element(*args)

    def find_elements(self, *args):
        return self.driver.find_elements(*args)

    def get_win_size(self):
        return self.driver.get_window_size()

    def swipes(self, start_x1, start_y1, end_x2, end_y2, duration):
        return self.driver.swipe(start_x1, start_y1, end_x2, end_y2, duration)
