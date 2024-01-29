from src.utils.common import Utils
from smsactivate.api import SMSActivateAPI
import pprint


class SMSActivator:
    def __init__(self):
        self.API_KEY = ""
        self.COUNTRY_CODE = 0

        # initializing smsactivate api
        self.sa = SMSActivateAPI(self.API_KEY)
        self.sa.debug_mode = True

    def buy_number(self):
        """

        :return: dict of endDate, id, number
        """

        # number id 7730279

        operators = self.sa.getRentNumber(
            time=4, country=self.COUNTRY_CODE, service="full"
        )

        print(operators)
        # self.operators = self.sa.getRentStatus(self.sa.getRentList()['values']['0']['id']) # check all incoming messages

        # returned sample json
        """
        dict = {'endDate': '2022-12-01 15:37:34',
        "id': 7730279,
        ' number':'79289766823°}
        """

        return operators["phone"]

    def get_confirmation_code(self, id_of_number, is_uber=None, is_yango=None):
        """
        :param id_of_number: required to pass number id to verify incoming message
        :param is_uber: default None - parses message for Uber
        :param is_yango: default None - parses message for Yango
        :return: int confirmation code only in str or None if message is not ready yet
        """

        returned_value = self.sa.getRentStatus(id_of_number)

        def iter(key):
            if returned_value["status"] != "error":
                for i in returned_value["values"]:
                    if key in returned_value["values"][i]["phoneFrom"]:
                        confirmation_code = (
                            returned_value["values"][i]["text"]
                            .replace(".", " ")
                            .replace("\n", " ")
                            .split()
                        )

                        for code in confirmation_code:
                            if code.isdigit():
                                return code
            else:
                return None

        if is_uber:
            return iter("Uber")

        if is_yango:
            return iter("Yandex")

    def activate_number(self, is_uber=None, is_yango=None):
        """


        :param is_uber:
        :param is_yango:
        :return:
        """
        if is_uber:
            return self.sa.getNumber(
                service="ub", operator="any", country=self.COUNTRY_CODE
            )

        if is_yango:
            return self.sa.getNumber(
                service="ya", operator="any", country=self.COUNTRY_CODE
            )

        """
        {'activation_id': 1192283283, 'phone': 79260403285}
        """

    def get_all_number_statuses(self):
        return self.sa.getActiveActivations()

    """
    {'status': 'success', 'activeActivations': [{'activationId': '1192280921', 'serviceCode': 'ub', 'phoneNumber': '79639235075', 'activationCost': '10.00', 'activationStatus': '4', 'smsCode': None, 'smsText': None, 'activationTime': '2022-12-21 14:07:46', 'discount': '0', 'repeated': '0', 'countryCode': '0', 'countryName': 'Russia', 'canGetAnotherSms': '1'}, {'activationId': '1192283283', 'serviceCode': 'ub', 'phoneNumber': '79260403285', 'activationCost': '10.00', 'activationStatus': '4', 'smsCode': None, 'smsText': None, 'activationTime': '2022-12-21 14:09:30', 'discount': '0', 'repeated': '0', 'countryCode': '0', 'countryName': 'Russia', 'canGetAnotherSms': '1'}]}

    or 
    
    {'status': 'success', 'activeActivations': [{'activationId': '1192283283', 'serviceCode': 'ub', 'phoneNumber': '79260403285', 'activationCost': '10.00', 'activationStatus': '2', 'smsCode': ['529503'], 'smsText': ['529503'], 'activationTime': '2022-12-21 14:09:30', 'discount': '0', 'repeated': '0', 'countryCode': '0', 'countryName': 'Russia', 'canGetAnotherSms': '1'}]}
    """

    def get_number_status_by_id(self, portal_id):
        """

        :param portal_id:
        :return:
        """

        """
        STATUS_WAIT_CODE
        """
        """
        STATUS_OK:791423
        """

        response = self.sa.getStatus(portal_id)

        if "STATUS_OK" in response:
            return response.split(":")[-1]

        else:
            return None


if __name__ == "__main__":
    x = SMSActivator()

    # x.request_activations()

    # print(x.activate_number(is_yango=True))

    print(x.get_number_status_by_id(1192290788))

    # print(x.get_all_number_statuses())
