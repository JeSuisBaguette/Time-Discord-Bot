# Imports
import requests
import json


# Returns the time of the timezone specified. Has to be in IANA format to work. 
def get_time(timezone):
    try:
        data = requests.get(
            f"https://timeapi.io/api/Time/current/zone?timeZone={timezone}"
        ).json()
        return f'{data["timeZone"]}\
                \n{data["year"]}-{data["month"]:02}-{data["day"]:02}\
                \n{data["hour"]:02}:{data["minute"]:02}:{data["seconds"]}'
    except AttributeError:
        return "Invalid Time zone. Only IANA time zone names are accepted."


# Returns the time zone of the "to_zone" incremented by the specified amount from the "from_zone".
def convert_time(from_zone, to_zone, increment="00:00:00:00"):
    try:
        # Gets the time zone of the "from_zone" with incremented modifier.
        initial = requests.post(
            "https://timeapi.io/api/Calculation/current/increment",
            json={"timeZone": from_zone, "timeSpan": increment},
        ).json()
        dateTime = initial["calculationResult"]["dateTime"]
        date, time_stuff = dateTime.split("T")
        time, _ = time_stuff.split(".")
        # Runs conversion to "to_zone" time. 
        data = requests.post(
            "https://timeapi.io/api/Conversion/ConvertTimeZone",
            json={
                "fromTimeZone": from_zone,
                "dateTime": f"{date} {time}",
                "toTimeZone": f"{to_zone}",
                "dstAmbiguity": "",
            },
        ).json()
        return f'{data["toTimeZone"]}\
                \n{data["conversionResult"]["year"]}-{data["conversionResult"]["month"]:02}-{data["conversionResult"]["day"]:02}\
                \n{data["conversionResult"]["hour"]:02}:{data["conversionResult"]["minute"]:02}:{data["conversionResult"]["seconds"]:02}'
    except (TypeError, AttributeError):
        return "Invalid increment range/time zone. Make sure to add leading zeros if applicable/only enter time zones in IANA format."
