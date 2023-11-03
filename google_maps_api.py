from https_methods import HttpMethods

"""Create, change, get & delete location"""

BASE_URL = 'https://rahulshettyacademy.com'
key = '?key=qaclick123'


class GoogleMapsApi:

    """Post"""
    @staticmethod
    def create_new_location():
        post_resource = '/maps/api/place/add/json'
        body = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"

        }
        post_url = BASE_URL + post_resource + key
        post_results = HttpMethods.post_method(post_url, body)
        return post_results


        """Get"""
    @staticmethod
    def get_location(place_id):
        get_resource = '/maps/api/place/get/json'
        place_id = place_id
        get_url = BASE_URL + get_resource + key + '&place_id=' + place_id
        get_results = HttpMethods.get_method(get_url)
        return get_results

    """Put"""
    @staticmethod
    def put_location(place_id):
        put_resource = '/maps/api/place/update/json'
        put_body = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"

        }
        put_url = BASE_URL + put_resource + key
        put_result = HttpMethods.put_method(put_url, put_body)
        return put_result

    """Delete"""
    @staticmethod
    def delete_location(place_id):
        delete_resource = '/maps/api/place/delete/json'
        delete_body = {
            "place_id": place_id
        }

        delete_url = BASE_URL + delete_resource + key
        delete_result = HttpMethods.delete_method(delete_url, delete_body)
        return delete_result













