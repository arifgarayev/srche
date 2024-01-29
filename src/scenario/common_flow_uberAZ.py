import os
import time

from src.services.uber_az import Uber_az
from src.services.emulator import Emulator
from src.utils.common import Utils
from src.services.sms_activate import SMSActivator
from src.entity.common_queries import Query
from src.common.generator import CommonObjectGenerator


class CommonFlowUberAZ(CommonObjectGenerator):
    # emu = Emulator(Utils.get_json_to_dict(os.path.dirname(os.getcwd()) + '/config/emulator_config.json'))

    #
    # db = Query(Utils.get_json_to_dict(os.path.dirname(os.getcwd()) + '/config/database_config.json')['DB_conn_str'])
    #
    # sms = SMSActivator()

    _issued_number_id = None  # FIXME to None

    _send_new_state_tries = 2

    def __init__(self):
        super().__init__()

        self.uber = Uber_az(self.emu)

    def issue_a_number(self):
        """
        issue a number
        add to db
        :return:
        """

        operator_dict = self.sms.activate_number(is_uber=True)

        try:
            # added to db
            self.db.insert_new_issued_number(
                operator_dict["activation_id"], operator_dict["phone"], is_uber=True
            )

            # set a prop
            self._issued_number_id = operator_dict["activation_id"]

            print("Issued number id prop - ", self._issued_number_id)
            print("Dict ", operator_dict)

            print(operator_dict)

            return operator_dict["activation_id"]
        except Exception:
            return None

    def register_a_user_with_registered_acc(self):
        time.sleep(3.5)

        self.uber.click_settings_menu()

        time.sleep(3.5)

        self.uber.click_to_settings_profile()

        time.sleep(3.5)

        self.uber.click_to_logout()

        time.sleep(3.5)

        self.uber.click_enter_phone_number()

        time.sleep(3.5)

        # self.uber.delete_phone_number()

        self.uber.add_account()

        time.sleep(7)

        # self.uber.add_phone_number()
        #
        # time.sleep(3.5)

        self.uber.clear_phone_number()

        time.sleep(3.5)

        self.issue_a_number()

        time.sleep(5)

        phone_number = self.db.get_mobile_no(self._issued_number_id, is_uber=True)

        self.uber.send_phone_number("+" + str(phone_number[0][0]))

        time.sleep(3.5)

        self.uber.click_to_send_confirmation_code()
        # wait for confirmation code
        time.sleep(3.5)

    def register_a_user_without_registered_acc(self):
        time.sleep(3.5)

        self.uber.click_settings_menu()

        time.sleep(3.5)

        self.uber.click_enter_phone_number()

        time.sleep(10)

        self.uber.clear_phone_number()

        time.sleep(2.5)

        phone_number = self.db.get_mobile_no(self._issued_number_id, is_uber=True)

        self.uber.send_phone_number("+" + str(phone_number[0][0]))

        time.sleep(3.5)

        self.uber.click_to_send_confirmation_code()

        # wait for confirmation code

        time.sleep(3.5)

    def register_a_user_with_device_blocked_user_in(self):
        # self.uber.delete_phone_number()

        # self.uber.add_account()
        #
        # time.sleep(7)

        self.uber.clear_phone_number()

        time.sleep(3.5)

        self.issue_a_number()

        time.sleep(5)

        phone_number = self.db.get_mobile_no(self._issued_number_id, is_uber=True)

        self.uber.send_phone_number("+" + str(phone_number[0][0]))

        time.sleep(3.5)

        self.uber.click_to_send_confirmation_code()
        # wait for confirmation code
        time.sleep(15)

    def check_and_set_confirmation_code(self):
        time.sleep(10)

        confirmation_code = self.sms.get_number_status_by_id(self._issued_number_id)

        # time.sleep(15)
        print("Uber AZ confirmation code: ", confirmation_code)

        counter = 0
        while not confirmation_code and counter < 2:
            self.uber.resend_sms_confirmation_code()
            time.sleep(35)
            confirmation_code = self.sms.get_number_status_by_id(self._issued_number_id)
            print("Uber AZ confirmation code: ", confirmation_code)
            counter += 1

        # self.db.insert_confirmation_code()
        if not confirmation_code:
            self.sms.sa.setStatus(id=self._issued_number_id, status=8)

            self.uber.driver.back()

            self.register_a_user_with_device_blocked_user_in()

            time.sleep(10)

            confirmation_code = self.sms.get_number_status_by_id(self._issued_number_id)

            # time.sleep(15)
            print("Uber AZ confirmation code: ", confirmation_code)

            counter = 0
            while not confirmation_code and counter < 2:
                self.uber.resend_sms_confirmation_code()
                time.sleep(35)
                confirmation_code = self.sms.get_number_status_by_id(
                    self._issued_number_id
                )
                print("Uber AZ confirmation code: ", confirmation_code)
                counter += 1

        self.uber.send_confirmation_code(confirmation_code)

        self.db.insert_confirmation_code(
            self._issued_number_id, confirmation_code, is_uber=True
        )

        self.uber.click_to_payment_method()

        time.sleep(3)

        self.uber.click_cash()

        time.sleep(3)

        self.uber.click_back_from_paymet_method_view()

        time.sleep(3)

    def send_new_state_route(self, origin, destination):
        # if
        try:
            self.uber.click_where_to_banner(self._send_new_state_tries)

        except (self.uber.NoSuchElementException, self.uber.TimeoutException):
            self._send_new_state_tries = 0

            self.uber.kill_uber_app()

            time.sleep(10)

            self.uber.start_uber_app()

            time.sleep(10)

            self.uber.click_gps_location_circle()

            time.sleep(5)

            self.uber.click_where_to_banner(self._send_new_state_tries)

        self._send_new_state_tries += 1

        time.sleep(3)

        self.uber.click_top_route()

        time.sleep(3)

        self.uber.clear_route()
        time.sleep(2)

        self.uber.send_top_route(origin)

        time.sleep(3)

        self.uber.click_to_suggested_dest()

        time.sleep(5)

        self.uber.send_bottom_route(destination)

        time.sleep(3)

        if self.uber.click_to_suggested_dest(is_bottom=True) == False:
            time.sleep(3)
            self.register_a_user_with_device_blocked_user_in()

            time.sleep(3)

            self.check_and_set_confirmation_code()
            time.sleep(3)

            # reg ended

            self.uber.click_where_to_banner()

            time.sleep(2)

            self.uber.click_top_route()

            time.sleep(3)

            self.uber.clear_route()
            time.sleep(2)

            self.uber.send_top_route(origin)

            time.sleep(3)

            self.uber.click_to_suggested_dest()

            time.sleep(5)

            self.uber.send_bottom_route(destination)

            time.sleep(3)

            self.uber.click_to_suggested_dest(is_bottom=True)

        time.sleep(10)

    def confirm_ride(self):
        time.sleep(5)

        self.uber.confirm_ride()

        time.sleep(13)

        if self.uber.check_for_device_block():
            # self.uber.click_to_use_another_number()
            # time.sleep(10)
            # self.register_a_user_with_device_blocked_user_in() # FIXME
            # time.sleep(3)
            #
            # self.check_and_set_confirmation_code()
            # time.sleep(3)

            return False

        elif self.uber.check_for_number_block():
            # self.register_a_user_with_number_blocked_user_in()  # FIXME
            # time.sleep(3)
            #
            # self.check_and_set_confirmation_code()
            # time.sleep(3)

            return False

        return True

        # time.sleep(7)
        #
        # self.uber.shrink_active_search_order()

    def register_a_user_with_number_blocked_user_in(self):
        self.uber.click_to_ok_in_number_block()

        time.sleep(3.5)

        self.register_a_user_with_registered_acc()

        time.sleep(3)

        # self.uber.delete_phone_number()
        #
        # time.sleep(7)
        #
        # self.uber.clear_phone_number()
        #
        # time.sleep(3.5)
        #
        # phone_number = self.db.get_mobile_no(self._issued_number_id)
        #
        # self.uber.send_phone_number("+" + str(phone_number[0][0]))
        #
        # time.sleep(3.5)
        #
        # self.uber.click_to_send_confirmation_code()
        # # wait for confirmation code
        # time.sleep(3.5)

    def handle_active_order(self):
        def activity_checker():
            is_active_order = self.uber.is_any_active_order()
            limit = 10

            while not is_active_order:
                time.sleep(10)
                if limit < 180:
                    is_active_order = self.uber.is_any_active_order()
                    limit += 10

                else:
                    return False

            return True

        if activity_checker():
            if self._issued_number_id:
                self.db.update_trip_info(self._issued_number_id, is_uber=True)

            time.sleep(5)

            # your ride will be cheaper message handler
            try:
                self.uber.shrink_active_order_view()
            except:
                self.uber.your_ride_will_be_cheaper_message_handler()

                time.sleep(2)

                self.uber.shrink_active_order_view()

            time.sleep(3)

            self.uber.click_to_details_in_active_order()

            time.sleep(5)

            driver_name, car_description, phone_number = self.uber.get_all_driver_data()

            driver_name = driver_name
            car_description = car_description.replace("\u200a", " ")
            phone_number = (
                phone_number.replace("+", "")
                .replace("(", "")
                .replace(")", "")
                .replace("-", "")
                .replace("\xa0", "")
            )
            # insert scraped data to db
            self.db.insert_driver_data(
                driver_name, phone_number, car_description, is_uber=True
            )

            return driver_name, car_description, phone_number

        else:
            return None

    def cancel_active_order(self):
        self.uber.cancel_ride()

        time.sleep(3)

        try:
            self.uber.hanlde_are_you_sure_to_cancel()

            time.sleep(5)

            self.uber.click_ok_at_cancelled_ride()

        except self.uber.NoSuchElementException:
            time.sleep(3)
            self.uber.click_ok_at_cancelled_ride()

        self.uber.select_reason()

        time.sleep(2)

        self.uber.complete_reason_click_done()

        time.sleep(5)

    def reinstall_with_new_id(self):
        self.uber.kill_uber_app()
        time.sleep(2)
        self.uber.kill_clone_app()

        time.sleep(2)

        if self.uber.package_name:
            self.uber.uninstall_app(self.uber.package_name)

        time.sleep(3)

        self.uber.start_clone_app()

        time.sleep(7)

        self.uber.click_clone_button()

        time.sleep(5)

        try:
            self.uber.click_uber_app()

        except:
            self.uber.scroll_down_page()
            time.sleep(3)
            self.uber.click_uber_app()

        time.sleep(2)

        self.uber.click_to_choose_os()

        time.sleep(3)

        self.uber.click_device_privacy()

        time.sleep(2)

        self.uber.enable_one_click()

        time.sleep(2)

        self.uber.edit_custom_android_id()

        time.sleep(2)

        self.uber.send_custom_anroid_id()

        time.sleep(2)

        self.uber.edit_custom_imei()

        time.sleep(2)

        self.uber.send_custom_imei()

        time.sleep(2)

        self.uber.driver.back()

        time.sleep(2)

        self.uber.submit_clone()

        time.sleep(2)

        self.uber.submit_install()

        time.sleep(2)

        self.uber.kill_clone_app()

        self.uber.package_name_setter()

        time.sleep(2)

        self.uber.grant_permissions()

        time.sleep(2)


if __name__ == "__main__":
    xyz = CommonFlowUberAZ()

    xyz.uber.kill_uber_app()

    xyz.uber.start_uber_app()

    # time.sleep(5)

    xyz.uber.click_gps_location_circle()

    while True:
        for x, y in Utils.get_json_to_dict(
            os.path.dirname(os.getcwd()) + "/config/top_routes.json"
        ).items():
            xyz.send_new_state_route(x, y)

            if not xyz.confirm_ride():
                # uninstall app
                # clone app with new ID

                time.sleep(3)
                xyz.send_new_state_route(x, y)

            print(xyz.handle_active_order())

            xyz.cancel_active_order()

    # time.sleep(5)
    #
    # xyz.issue_a_number() #
    #
    # time.sleep(5)
    #
    # xyz.register_a_user_without_registered_acc()
    #
    # time.sleep(5)
    #
    # xyz.check_and_set_confirmation_code()


# id=  com.mlubv.uber.az:id/arrows_view
# //android.widget.Button[@content-desc="Call"]

# DETAIL //android.widget.Button[@resource-id="com.mlubv.uber.az:id/details"]//android.widget.Button[@resource-id="com.mlubv.uber.az:id/lead_frame"]

# Ride details locators .text + take screenshot

# driver name => //android.widget.FrameLayout[@resource-id="com.mlubv.uber.az:id/order_info_driver"]//android.widget.LinearLayout[@resource-id="com.mlubv.uber.az:id/center"]//android.widget.TextView[@resource-id="com.mlubv.uber.az:id/top"]

# car desription => //android.widget.TextView[@resource-id="com.mlubv.uber.az:id/car_description"]

#  phone number => //android.widget.FrameLayout[@resource-id="com.mlubv.uber.az:id/order_info_phone"]//android.widget.LinearLayout[@resource-id="com.mlubv.uber.az:id/center"]//android.widget.TextView[@resource-id="com.mlubv.uber.az:id/top"]


# 5 seconds arrovview moves down
