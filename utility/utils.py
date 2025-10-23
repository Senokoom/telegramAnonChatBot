from geopy.geocoders import Nominatim


def get_location(location_inp: str | tuple[float, float]) -> dict | None:
    """
    Проверяет существование города и возвращает *Dict(существует)* или *None* . Поддерживает русские и английские названия.
    Так же может выдать локацию, если есть такое кафе, ресторан и т.п.
    :param location_inp: str Название города на русском или англиском. tuple(float,float) координаты.
    """
    geolocator = Nominatim(user_agent="AnonChatTgBot UnivercityProject (leva.kochin@gmail.com)")
    if isinstance(location_inp, tuple):
        lat, lon = location_inp
        location = geolocator.reverse((lat, lon), exactly_one=True)
        if location and "adress" in location.raw:
            address = location.raw["address"]
            city = address.get("city") or address.get("town") or address.get("village")
            return {"city": city,
                    "lat": lat,
                    "lon": lon}
    elif isinstance(location_inp, str):
        location = geolocator.geocode(location_inp)
        if location:
            return {"city": location_inp,
                    "lat": location.latitude,
                    "lon": location.longitude}
    return None



