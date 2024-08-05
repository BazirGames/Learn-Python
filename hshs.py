
class Duration:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __add__(self, other):
        if not isinstance(other, Duration):
            return None
        total_hours = self.hours + other.hours
        total_minutes = self.minutes + other.minutes
        if total_minutes >= 60:
            total_hours += 1
            total_minutes -= 60
        return Duration(total_hours, total_minutes)

    def __int__(self):
        return self.hours * 60 + self.minutes

flight_time = Duration(3, 50)
drive_time = Duration(2, 26)

print(int(flight_time) + int(drive_time))
print(int(flight_time + drive_time))