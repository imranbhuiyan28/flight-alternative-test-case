from pages.base_page import BasePage


class MainPage(BasePage):



    def open_main(self):
        self.open_url("https://www.target.com/")


    def circle_target_page(self):
        self.open_url("https://www.target.com/circle")


    def target_app_page(self):
        self.open_url("https://www.target.com/c/target-app/-/N-4th2r")