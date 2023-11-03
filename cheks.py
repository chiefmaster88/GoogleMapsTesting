

class Check:

    @staticmethod
    def assert_status_code(response, status_code):
        assert response == status_code

    @staticmethod
    def check_required_fields(response, expected_result):
        assert response == expected_result

    @staticmethod
    def check_fields_value(response, fields_value):
        assert response == fields_value