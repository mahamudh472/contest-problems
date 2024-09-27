class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.bookings:
            # Check if there is an overlap
            if not (end <= s or start >= e):
                return False
        # If no overlap, add the new booking
        self.bookings.append((start, end))
        return True



# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
param_1 = obj.book(47,50)
param_1 = obj.book(33,41)
param_1 = obj.book(39,45)
param_1 = obj.book(33,42)
param_1 = obj.book(25,32)