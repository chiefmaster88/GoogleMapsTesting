import pytest
from ui_google_maps_start_page import StartPage


@pytest.mark.ui
def test_check_find_location():
    google_maps_location = StartPage()
    google_maps_location.open_start_page()
    google_maps_location.search_place('Miami')
    google_maps_location.check_title('Майами – Google Карты')
    google_maps_location.close_browser()
