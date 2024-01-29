class ActionsInterface:
    def resend_sms_confirmation_code(self):
        pass

    def click_where_to_banner(self):
        pass

    def click_top_route(self):
        pass

    def send_top_route(self, adress):
        pass

    def clear_route(self):
        pass

    def click_bottom_route(self):
        pass

    def send_bottom_route(self, adress):
        pass

    def click_to_payment_method(self):
        pass

    def click_entrance_top_route(self):
        pass

    def click_entrance_bottom_route(self):
        pass

    def click_gps_location_circle(self):
        pass

    def click_settings_menu(self):
        pass

    def click_to_suggested_dest(self, is_bottom=None):
        pass

    # def choose_payment_method(self): # TODO
    #     pass

    # def choose_eco_cat(self): # TODO
    #     pass

    def confirm_ride(self):
        pass

    def click_to_settings_profile(self):
        pass

    def click_to_logout(self):
        pass

    def click_enter_phone_number(self):
        pass

    #
    # def enter_phone_number(self):
    #     pass

    def delete_phone_number(self):
        pass

    def add_phone_number(self):
        pass

    def clear_phone_number(self):
        pass

    def send_phone_number(self, phone_number):
        pass

    def click_to_send_confirmation_code(self):
        pass

    def send_confirmation_code(self, confirmation_code):
        pass

    def set_user_name(self, names_tuple):
        pass

    def click_cash(self):
        pass

    def click_back_from_paymet_method_view(self):
        pass

    def check_if_no_cars_have_found(self):
        pass

    def shrink_active_order_view(self):
        pass

    def click_to_details_in_active_order(self):
        pass

    def get_all_driver_data(self):
        pass

    def take_screenshot(self):
        pass

    def is_any_active_order(self):
        pass

    def shrink_active_search_order(self):
        pass

    def cancel_active_search_ride(self):
        pass

    def click_ok_at_cancelled_ride(self):
        pass

    def cancel_ride(self):
        pass

    # //android.widget.Button[@content-desc="Cancel ride"]/android.widget.FrameLayout/android.widget.ImageView

    def hanlde_are_you_sure_to_cancel(self):
        pass

    # /hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[6]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]

    def select_reason(self):
        pass

    # //android.widget.CheckBox[@content-desc="Driver asked me to cancel the ride"]

    def complete_reason_click_done(self):
        pass

    # com.mlubv.uber.az:id/done

    def check_for_device_block(self):
        pass

    def check_for_number_block(self):
        pass

    def your_ride_will_be_cheaper_message_handler(self):
        pass

    def is_new_state_adress(self):
        pass

    def click_to_use_another_number(self):
        pass

    def click_to_ok_in_number_block(self):
        pass

    def check_if_user(self):  # FIXME
        pass

    def add_account(self):
        pass
