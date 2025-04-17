from pages.base_page import BasePage


class MainPage(BasePage):



    def open_main(self):
        self.open_url("https://www.target.com/")


    def circle_target_page(self):
        self.open_url("https://www.target.com/circle")


    def target_app_page(self):
        self.open_url("https://www.target.com/c/target-app/-/N-4th2r")

    def open_sace_demo(self):
        self.open_url('https://www.saucedemo.com/v1/')

    def open_automation_website(self):
        self.open_url("https://automationexercise.com/")