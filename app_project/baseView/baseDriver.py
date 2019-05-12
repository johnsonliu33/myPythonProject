class BaseDriver(object):
    def __init__(self, driver):
        self.driver = driver

    def base_find_element(self, *args):
        return self.driver.find_element(*args)

    def base_find_elements(self, *args):
        return self.driver.find_elements(*args)

    def base_get_win_size(self):
        return self.driver.get_window_size()

    def base_swipes(self, start_x1, start_y1, end_x2, end_y2, duration):
        return self.driver.swipe(start_x1, start_y1, end_x2, end_y2, duration)
