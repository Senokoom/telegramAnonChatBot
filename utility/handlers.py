from geopy.geocoders import Nominatim

def city_isreal(location_inp) -> dict | None:
    """
    Проверяет существование города и возвращает *Dict(существует)* или *None* . Поддерживает русские и английские названия.
    Так же может выдать локацию, если есть такое кафе, ресторан и т.п.
    """
    geolocator = Nominatim(user_agent="AnonChatTgBot UnivercityProject (leva.kochin@gmail.com)")
    location = geolocator.geocode(location_inp)
    if location:
        return {"city": location_inp,
                "lat": location.latitude,
                "lon": location.longitude}
    else:
        return None