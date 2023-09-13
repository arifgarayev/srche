import subprocess
import time
import os
import random


from src.services.emulator import Emulator
from src.utils.common import Utils
from src.services.interface.actions_interface import ActionsInterface

from selenium.webdriver.common.keys import Keys


#   Appium -> Selenium -> ABC
#        |
#       \/
# Emulator -> AVD
#        |
#       \/
# Inversion of control
# Uber_az -> applicaton


# Utils.get_json_to_dict(os.path.dirname(os.getcwd()) + '/config/emulator_config.json')

# emulator must be independently injected into objects
class Uber_az(ActionsInterface):



    def __init__(self, emulator_instance: Emulator):

        self.emu = emulator_instance

        self.driver = emulator_instance.get_emulator_driver()
        self.wait = emulator_instance.get_emulator_wait()
        self.action_chains = emulator_instance.get_action_chains()
        self.By = emulator_instance.get_By()
        self.EC = emulator_instance.get_Ec()

        self.NoSuchElementException, self.TimeoutException,\
            self.StaleElementReferenceException= emulator_instance.get_Exceptions()
        try:
            self.package_name = subprocess.check_output(f'adb -s {self.emu.device_name} shell pm list packages | grep dkapp', shell=True).decode().split(':')[-1].strip()
        except:
            self.package_name = None

    def start_uber_app(self):
        time.sleep(3)
        #os.system("adb shell monkey -p com.mlubv.uber.az -c android.intent.category.LAUNCHER 1")
        os.system(f"adb -s {self.emu.device_name} shell monkey -p {self.package_name} -c android.intent.category.LAUNCHER 1")

        # time.sleep(3)
        #package_name = os.system('adb shell pm list packages | grep dkapp')
        # package_name = subprocess.check_output("adb shell pm list packages | grep dkapp", shell=True)
        # print(package_name.decode(), type(package_name.decode()))

        time.sleep(10)

        try:
            self.driver.find_element_by_xpath("//android.widget.Button[@text = 'Continue']").click()
            time.sleep(5)
        except:
            pass

    def package_name_setter(self):
        self.package_name = subprocess.check_output(f'adb -s {self.emu.device_name} shell pm list packages | grep dkapp', shell=True).decode().split(':')[-1].strip()

    def kill_uber_app(self):
        time.sleep(2)
        #os.system("adb shell am force-stop com.mlubv.uber.az")
        os.system(f"adb -s {self.emu.device_name} shell am force-stop {self.package_name}")
        time.sleep(15)

    def uninstall_app(self, package_name):
        os.system(f"adb -s {self.emu.device_name} uninstall {package_name}")


    def grant_permissions(self):

        os.system(f"adb -s {self.emu.device_name} shell pm grant {self.package_name} android.permission.CALL_PHONE")

        time.sleep(2)

        os.system(f"adb -s {self.emu.device_name} shell pm grant {self.package_name} android.permission.POST_NOTIFICATIONS")

        time.sleep(2)

        os.system(f"adb -s {self.emu.device_name} shell pm grant {self.package_name} android.permission.WRITE_EXTERNAL_STORAGE")

        time.sleep(2)

        os.system(f"adb -s {self.emu.device_name} shell pm grant {self.package_name} android.permission.ACCESS_FINE_LOCATION")

        time.sleep(2)


    def start_clone_app(self):
        # com.py.cloneapp.huawei

        time.sleep(2)

        os.system(f"adb -s {self.emu.device_name} shell monkey -p com.py.cloneapp.huawei -c android.intent.category.LAUNCHER 1")

        time.sleep(10)

    def kill_clone_app(self):

        time.sleep(2)
        # os.system("adb shell am force-stop com.mlubv.uber.az")
        os.system(f"adb -s {self.emu.device_name} shell am force-stop com.py.cloneapp.huawei")
        time.sleep(10)

    def click_gps_location_circle(self):
        # self.driver.back()
        try:
            self.driver.find_element_by_id('com.mlubv.uber.az:id/icon_circle_button_image').click()
            self.wait(self.EC.presence_of_element_located((self.By.ID, 'com.mlubv.uber.az:id/center')))
        except (self.NoSuchElementException, self.TimeoutException):
            time.sleep(20)
        time.sleep(5)

    def submit_clone(self):

        self.driver.find_element_by_xpath('//android.widget.TextView[@text = "Clone"]').click()

        time.sleep(15)


    def submit_install(self):

        self.driver.find_element_by_xpath('//android.widget.Button[@text="Install"]').click()

        time.sleep(15)

        self.driver.find_element_by_xpath('//android.widget.Button[@text="Done"]').click()

        time.sleep(5)
    def click_clone_button(self):
        self.driver.back()
        time.sleep(8)
        self.driver.find_element_by_xpath('//android.widget.ImageView[@resource-id="com.py.cloneapp.huawei:id/iv_btn_create"]').click()
        time.sleep(5)


    def scroll_down_page(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text = 'ALL']").click()
        time.sleep(2)
        for _ in range(47):
            self.action_chains.send_keys(Keys.ARROW_DOWN).perform()
            time.sleep(0.2)

        time.sleep(5)

    def click_uber_app(self):
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="Uber AZ"]').click()

        time.sleep(5)


    def click_to_choose_os(self):

        self.driver.find_element_by_id('com.py.cloneapp.huawei:id/tv_os_cur').click()

        time.sleep(5)

        self.driver.find_element_by_xpath("//android.widget.Button[@text = 'Confirm']").click()

        time.sleep(3)

    def click_device_privacy(self):

        self.driver.find_element_by_xpath('//android.widget.TextView[@text="Device privacy"]').click()

        time.sleep(5)

    def enable_one_click(self):

        self.driver.find_element_by_id('com.py.cloneapp.huawei:id/switch_all').click()

        time.sleep(4)


    def edit_custom_android_id(self):

        self.driver.find_element_by_id('com.py.cloneapp.huawei:id/iv_custom_androidid').click()

        time.sleep(3)

    def send_custom_anroid_id(self):

        self.driver.find_element_by_id('com.py.cloneapp.huawei:id/et').click()

        time.sleep(3)

        self.driver.find_element_by_id('com.py.cloneapp.huawei:id/et').send_keys('%016x' % random.randrange(16**16))

        time.sleep(3)

        self.driver.find_element_by_id('com.py.cloneapp.huawei:id/tv_btn_ok').click()

        time.sleep(5)


    def edit_custom_imei(self):

        self.driver.find_element_by_id('com.py.cloneapp.huawei:id/iv_custom_imei_imsi').click()

        time.sleep(3)

    def send_custom_imei(self):

        self.driver.find_element_by_id('com.py.cloneapp.huawei:id/et_imei').click()
        time.sleep(3)
        self.driver.find_element_by_id('com.py.cloneapp.huawei:id/et_imei').send_keys(''.join(random.choice('0123456789') for n in range(15)))
        time.sleep(3)

        self.driver.find_element_by_id('com.py.cloneapp.huawei:id/et_imsi').click()
        time.sleep(3)
        self.driver.find_element_by_id('com.py.cloneapp.huawei:id/et_imsi').send_keys(
            ''.join(random.choice('0123456789') for n in range(15)))
        time.sleep(3)

        self.driver.find_element_by_id('com.py.cloneapp.huawei:id/tv_btn_ok').click()

        time.sleep(5)

    def click_where_to_banner(self, tries=0):
        time.sleep(5)
        # if tries != 0:
        #     self.driver.find_element_by_xpath("//android.widget.TextView[@text='Where to?']").click()
        #
        #     time.sleep(2.2)
        #
        #     self.driver.find_element_by_xpath("//android.widget.TextView[@text='Where to?']").click()
        #
        # else:
        #     self.driver.find_element_by_xpath("//android.widget.TextView[@text='Where to?']").click()
        #
        #     time.sleep(2.2)

        try:
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='Where to?']").click()

            self.driver.find_element_by_id('com.mlubv.uber.az:id/component_input_center')

        except self.NoSuchElementException:

            self.driver.find_element_by_xpath("//android.widget.TextView[@text='Where to?']").click()

        self.wait(self.EC.presence_of_element_located((self.By.ID, 'com.mlubv.uber.az:id/component_input_center')))







    # routes

    def click_top_route(self):
        self.driver.find_element_by_xpath(
            "(//*[@resource-id = 'com.mlubv.uber.az:id/component_input_center'])[1]").click()


    def send_top_route(self, adress):

        self.driver.find_element_by_xpath \
            ("(//android.widget.EditText[@resource-id = 'com.mlubv.uber.az:id/component_list_item_input'])[1]"). \
            send_keys(adress)

        self.wait(self.EC.presence_of_element_located((self.By.XPATH, "//android.widget.LinearLayout[@resource-id = 'com.mlubv.uber.az:id/center']")))

        # wait - //android.widget.LinearLayout[@resource-id = 'com.mlubv.uber.az:id/center']

    # end routes




    def clear_route(self):
        self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="Clear text box"]').click()

    def click_bottom_route(self):
        self.driver.find_element_by_xpath(
            "(//android.widget.EditText[@resource-id = 'com.mlubv.uber.az:id/component_list_item_input'])[2]").click()


    def send_bottom_route(self, adress):

        self.driver.find_element_by_xpath("(//android.widget.EditText[@resource-id = 'com.mlubv.uber.az:id/component_list_item_input'])[2]").send_keys(adress)

        self.wait(self.EC.presence_of_element_located(
            (self.By.XPATH, "//android.widget.LinearLayout[@resource-id = 'com.mlubv.uber.az:id/center']")))


    def confirm_ride(self):


        #//android.widget.Button[@resource-id='com.mlubv.uber.az:id/order_taxi']//android.widget.LinearLayout[@resource-id="com.mlubv.uber.az:id/center"]//android.widget.TextView[@resource-id="com.mlubv.uber.az:id/top"]

        self.driver.find_element_by_xpath('//android.widget.TextView[@text="Confirm Uber"]').click()






    def click_entrance_top_route(self):
        self.driver.find_element_by_xpath \
            ("(//android.widget.EditText[@resource-id = 'com.mlubv.uber.az:id/component_list_item_input'])[1]").click()

        self.wait(self.EC.presence_of_element_located(
            (self.By.XPATH, "//android.widget.LinearLayout[@resource-id = 'com.mlubv.uber.az:id/center']")))


    def click_entrance_bottom_route(self):
        self.driver.find_element_by_xpath \
            ("(//android.widget.EditText[@resource-id = 'com.mlubv.uber.az:id/component_list_item_input'])[2]").click()
        self.wait(self.EC.presence_of_element_located(
            (self.By.XPATH, "//android.widget.LinearLayout[@resource-id = 'com.mlubv.uber.az:id/center']")))




    def click_to_suggested_dest(self, is_bottom=None):
        self.driver.find_element_by_xpath(
            "//android.widget.LinearLayout[@resource-id = 'com.mlubv.uber.az:id/center']").click()

        if is_bottom:
            try:
                time.sleep(10)
                self.driver.find_element_by_xpath("//android.widget.TextView[@text='Enter phone number']")
                return False
            except self.NoSuchElementException:

                try:
                    self.driver.find_element_by_xpath("//android.widget.TextView[@text = 'Cash']").click()

                    time.sleep(4)

                    self.driver.find_element_by_xpath("//android.widget.Button[@text='Done']").click()

                    time.sleep(5)
                except self.NoSuchElementException:
                    pass
                # self.driver.start_client()
                # try if cash is not enabled #FIXME if cash is not enabled

            self.wait(self.EC.presence_of_element_located(
                (self.By.XPATH, "//android.widget.TextView[@resource-id = 'com.mlubv.uber.az:id/wide_tariff_cost']")))

        else:
            self.wait(self.EC.presence_of_element_located((self.By.ID, 'com.mlubv.uber.az:id/component_input_center')))



    def click_settings_menu(self):

        self.driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="Menu"]').click()

        time.sleep(3.5)
        # self.wait(self.EC.presence_of_element_located(
        #     (self.By.XPATH, '//android.widget.Button[@content-desc="Become a driver"]/android.widget.LinearLayout')))



    def click_to_settings_profile(self):

        self.driver.find_element_by_id('com.mlubv.uber.az:id/auth').click()

        self.wait(self.EC.presence_of_element_located(
            (self.By.XPATH, '//android.widget.Button[@content-desc="Log out"]')))

        # //android.widget.Button[@content-desc="Log out"]


    def click_to_logout(self):

        self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="Log out"]').click()

        self.wait(self.EC.presence_of_element_located(
            (self.By.XPATH, '(//android.widget.LinearLayout[@resource-id="com.mlubv.uber.az:id/buttons"]//android.widget.Button)[2]')))

        # Warning message
        self.driver.find_element_by_xpath('(//android.widget.LinearLayout[@resource-id="com.mlubv.uber.az:id/buttons"]//android.widget.Button)[2]').click()

        time.sleep(5)

    def click_enter_phone_number(self):

        self.driver.find_element_by_xpath('//android.widget.LinearLayout[@resource-id="com.mlubv.uber.az:id/menu_personal_section"]//android.widget.Button[@resource-id="com.mlubv.uber.az:id/enter_phone"]').click()

        time.sleep(5)

        # self.wait(self.EC.presence_of_element_located(
        #     (self.By.ID,
        #      'com.mlubv.uber.az:id/text_add_account')))


    def delete_phone_number(self): #FIXME
        self.action_chains.click_and_hold(self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '+')]")).perform()

        self.wait(self.EC.presence_of_element_located(
            (self.By.ID,
             'android:id/button1')))

        self.driver.find_element_by_id('android:id/button1').click()

        self.wait(self.EC.presence_of_element_located(
            (self.By.ID,
             'com.mlubv.uber.az:id/button_next')))

        time.sleep(5)


    def add_account(self):

        time.sleep(3)
        self.driver.find_element_by_xpath("//android.widget.TextView[@class = 'android.widget.TextView'][@text = 'Add account']").click()

        time.sleep(5)


    def is_registered_account(self):

        try:
            self.driver.find_element_by_id('com.mlubv.uber.az:id/auth')
            return True
        except self.NoSuchElementException:
            return False




    def clear_phone_number(self):
        time.sleep(5)
        try:
            self.driver.find_element_by_id('com.mlubv.uber.az:id/edit_phone_number').clear()

        except self.NoSuchElementException:
            self.driver.back()

            time.sleep(2)

            self.driver.find_element_by_id('com.mlubv.uber.az:id/edit_phone_number').clear()


    def send_phone_number(self, phone_number):

        self.driver.find_element_by_id('com.mlubv.uber.az:id/edit_phone_number').send_keys(phone_number)

        time.sleep(2)

    def click_to_send_confirmation_code(self):

        self.driver.find_element_by_id('com.mlubv.uber.az:id/button_next').click()

        # self.wait(self.EC.presence_of_element_located(
        #     (self.By.ID,
        #      'android:id/button1')))

        self.wait(self.EC.presence_of_element_located(
            (self.By.ID,
             'com.mlubv.uber.az:id/button_next')))


    def send_confirmation_code(self, confirmation_code):
        self.driver.find_element_by_id('com.mlubv.uber.az:id/input_phone_code').send_keys(confirmation_code)

        time.sleep(10)


        # self.driver.find_element_by_id('com.mlubv.uber.az:id/button_next').click()


    def add_new_number(self):

        self.driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="Navigate up"]').click()

        time.sleep(5)





    def set_user_name(self, names_tuple):

        user_name = random.choice(names_tuple)

        # FIXME


    def click_to_payment_method(self):

        time.sleep(2)
        self.driver.find_element_by_id('com.mlubv.uber.az:id/hamburger').click()

        time.sleep(4)

        self.driver.find_element_by_id('com.mlubv.uber.az:id/payment_method').click()

        self.wait(self.EC.presence_of_element_located(
            (self.By.XPATH,
             "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.mlubv.uber.az:id/payment_method_list']//android.widget.CheckBox//android.widget.LinearLayout[@resource-id='com.mlubv.uber.az:id/center']")))


    def click_cash(self):

        self.driver.find_element_by_xpath("//androidx.recyclerview.widget.RecyclerView[@resource-id='com.mlubv.uber.az:id/payment_method_list']//android.widget.CheckBox//android.widget.LinearLayout[@resource-id='com.mlubv.uber.az:id/center']").click()

        time.sleep(6)

    def click_back_from_paymet_method_view(self):

        self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="Back"]').click()

        time.sleep(6)

        # close settings menu

        self.driver.back()



    def check_if_no_cars_have_found(self):
        try:
            self.driver.find_element_by_id('com.mlubv.uber.az:id/content_container')

            self.driver.find_element_by_id('com.mlubv.uber.az:id/buttons').click()
            return True
        except self.NoSuchElementException:
            return False


    def resend_sms_confirmation_code(self):

        self.driver.find_element_by_id('com.mlubv.uber.az:id/button_resend_sms').click()

        time.sleep(10)

    def shrink_active_order_view(self):

        self.driver.find_element_by_id('com.mlubv.uber.az:id/arrows_view').click()

        self.wait(self.EC.presence_of_element_located(
            (self.By.XPATH,
             "//android.widget.Button[@resource-id='com.mlubv.uber.az:id/details']//android.widget.Button[@resource-id='com.mlubv.uber.az:id/lead_frame']")))


    def click_to_details_in_active_order(self):
        try:
            self.driver.find_element_by_xpath('//android.widget.Button[@resource-id="com.mlubv.uber.az:id/details"]//android.widget.Button[@resource-id="com.mlubv.uber.az:id/lead_frame"]').click()

        except (self.NoSuchElementException, self.StaleElementReferenceException):
            time.sleep(5)
            self.shrink_active_order_view()

            time.sleep(3)

            self.driver.find_element_by_xpath(
                '//android.widget.Button[@resource-id="com.mlubv.uber.az:id/details"]//android.widget.Button[@resource-id="com.mlubv.uber.az:id/lead_frame"]').click()

        self.wait(self.EC.presence_of_element_located(
            (self.By.XPATH,
             '//android.widget.FrameLayout[@resource-id="com.mlubv.uber.az:id/order_info_phone"]//android.widget.LinearLayout[@resource-id="com.mlubv.uber.az:id/center"]//android.widget.TextView[@resource-id="com.mlubv.uber.az:id/top"]')))


    def is_any_active_order(self):
        try:
            self.driver.find_element_by_xpath('//android.widget.TextView[@text="Contact driver"]')
            return True
        except self.NoSuchElementException:
            try:
                self.driver.find_element_by_xpath('//android.widget.TextView[@text="Call"]')
                return True
            except self.NoSuchElementException:
                return False




    def get_all_driver_data(self):

        time.sleep(3)
        driver_name = self.driver.find_element_by_xpath('//android.widget.FrameLayout[@resource-id="com.mlubv.uber.az:id/order_info_driver"]//android.widget.LinearLayout[@resource-id="com.mlubv.uber.az:id/center"]//android.widget.TextView[@resource-id="com.mlubv.uber.az:id/top"]').text
        time.sleep(3)
        car_description = self.driver.find_element_by_xpath('//android.widget.TextView[@resource-id="com.mlubv.uber.az:id/car_description"]').text
        time.sleep(3)
        phone_number = self.driver.find_element_by_xpath('//android.widget.FrameLayout[@resource-id="com.mlubv.uber.az:id/order_info_phone"]//android.widget.LinearLayout[@resource-id="com.mlubv.uber.az:id/center"]//android.widget.TextView[@resource-id="com.mlubv.uber.az:id/top"]').text

        print("Driver Name: ", driver_name)
        print("Car Description: ", car_description)
        print("Phone Number: ", phone_number)

        self.driver.back()

        try:
            self.driver.find_element_by_xpath(
                '//android.widget.Button[@content-desc="Cancel ride"]/android.widget.FrameLayout/android.widget.ImageView')

        except (self.NoSuchElementException, self.StaleElementReferenceException):
            #open uber app assuming driver has arrived and driver.back() is throw you out app
            self.start_uber_app()
            try:
                self.shrink_active_order_view()
            except (self.NoSuchElementException, self.StaleElementReferenceException, self.TimeoutException):
                self.shrink_active_order_view()

            # self.driver.back()

        time.sleep(2)

        return driver_name, car_description, phone_number


    def take_screenshot(self):
        ...

    def shrink_active_search_order(self):
        self.driver.find_element_by_id('com.mlubv.uber.az:id/arrows_view').click()

        time.sleep(2)
        # FIXME add wait until

    def click_ok_at_cancelled_ride(self):

        time.sleep(4)

        self.driver.find_element_by_xpath('//android.widget.LinearLayout[@resource-id="com.mlubv.uber.az:id/buttons"]//android.widget.Button').click()

        time.sleep(5)

    def cancel_active_search_ride(self):
        self.driver.find_element_by_xpath('//android.widget.ImageView[@resource-id="com.mlubv.uber.az:id/icon_circle_button_image"]').click()

        self.wait(self.EC.presence_of_element_located(
            (self.By.XPATH,
             '//android.widget.LinearLayout[@resource-id="com.mlubv.uber.az:id/buttons"]//android.widget.Button')))

        self.click_ok_at_cancelled_ride()

    def cancel_ride(self):
        try:
            self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="Cancel ride"]/android.widget.FrameLayout/android.widget.ImageView').click()

        except self.NoSuchElementException:

            self.shrink_active_order_view()
            time.sleep(2)

            self.driver.find_element_by_xpath(
                '//android.widget.Button[@content-desc="Cancel ride"]/android.widget.FrameLayout/android.widget.ImageView').click()


    def hanlde_are_you_sure_to_cancel(self):

        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[6]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]').click()

    def select_reason(self):

        self.driver.find_element_by_xpath('//android.widget.CheckBox[@content-desc="Driver asked me to cancel the ride"]').click()

    def complete_reason_click_done(self):

        self.driver.find_element_by_id('com.mlubv.uber.az:id/done').click()

    def your_ride_will_be_cheaper_message_handler(self):

        self.driver.find_element_by_xpath('//android.widget.LinearLayout[@resource-id="com.mlubv.uber.az:id/buttons"]//android.widget.Button[@text="Great"]').click()


    def check_for_device_block(self):
        try:
            self.driver.find_element_by_xpath("//android.widget.Button[@text='Use another number']")

            return True

        except self.NoSuchElementException:


            return False

    def check_for_number_block(self):

        try:
            self.driver.find_element_by_xpath('//android.widget.Button[@text = "OK"]')

            return True

        except self.NoSuchElementException:

            return False

    def click_to_ok_in_number_block(self):
        self.driver.find_element_by_xpath('//android.widget.Button[@text = "OK"]').click()

        time.sleep(7)

    def click_to_use_another_number(self):
        self.driver.find_element_by_xpath("//android.widget.Button[@text='Use another number']").click()



if __name__ == "__main__":
    print(os.getcwd())

    emu = Emulator(Utils.get_json_to_dict(os.path.dirname(os.getcwd()) + '/src/config/emulator_config.json'))

    uber = Uber_az(emu)

    uber.start_uber_app()
