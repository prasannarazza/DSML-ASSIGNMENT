class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def display(self):
        return "{:02d}:{:02d}:{:02d}".format(self.hours, self.minutes, self.seconds)

    def add(self, other_time):
        total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds + \
                        other_time.hours * 3600 + other_time.minutes * 60 + other_time.seconds
        hours = total_seconds // 3600
        total_seconds %= 3600
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return Time(hours, minutes, seconds)

# Example usage:
time1 = Time(5, 30, 15)
time2 = Time(2, 45, 50)

print("Time 1:", time1.display())
print("Time 2:", time2.display())

added_time = time1.add(time2)
print("Sum of Time 1 and Time 2:", added_time.display())
