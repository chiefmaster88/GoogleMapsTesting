import pytest

from google_maps_api import GoogleMapsApi
from cheks import Check


@pytest.mark.api
def test_create_location():
    print('\nMethod Post')
    post_result = GoogleMapsApi.create_new_location()
    print(post_result.status_code, post_result.text)
    json_data = post_result.json()
    place_id = json_data.get('place_id')
    Check.assert_status_code(post_result.status_code, 200)
    Check.check_required_fields(list(post_result.json()), ['status', 'place_id', 'scope', 'reference', 'id'])


    print('Method Get')
    get_result = GoogleMapsApi.get_location(place_id)
    print(get_result.status_code, get_result.text)
    Check.assert_status_code(get_result.status_code, 200)
    data_json = get_result.json()
    Check.check_required_fields(list(data_json), ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])


    print('Method Put')
    put_result = GoogleMapsApi.put_location(place_id)
    print(put_result.status_code, put_result.text)
    Check.assert_status_code(put_result.status_code, 200)
    json_value = put_result.json()
    field_value = json_value['msg']
    Check.check_fields_value(field_value, 'Address successfully updated')



    print('Delete Method')
    delete_result = GoogleMapsApi.delete_location(place_id)
    print(delete_result.status_code, delete_result.text)
    Check.assert_status_code(delete_result.status_code, 200)
    json_delete_fields = delete_result.json()
    Check.check_required_fields(list(json_delete_fields), ['status'])
    value_delete_fields = json_delete_fields['status']
    Check.check_fields_value(value_delete_fields, 'OK')













