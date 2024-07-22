class ReservationError(Exception):
    pass

class NoSeatsError(ReservationError):
    def __init__(self):
        super().__init__("Brak dostepnych miejsc.")

class SeatReservedError(ReservationError):
    def __init__(self, seat):
        super().__init__(f"Miejsce {seat} jest juz zarezerwowane.")

class UserReservedError(ReservationError):
    def __init__(self, user, seat):
        super().__init__(f"Miejsce {seat} jest juz zarezerwowane przez urzytkownika {user}.")

class CancellationError(ReservationError):
    def __init__(self):
        super().__init__("Brak uprawnien do usuniecia tej rezerwacji")

class NotFoundError(ReservationError):
    def __init__(self, seat):
        super().__init__(f"Nie znaleziono rezerwacji miejsca {seat}.")


class Cinema:
    def __init__(self, rows, cols):
        self.seats = [['' for _ in range(cols)] for _ in range(rows)]
        self.user_reservations = {}

    def reserve_seat(self, user, seat):
        row, col = self._parse_seat(seat)
        if all(all(seat != '' for seat in row) for row in self.seats):
            raise NoSeatsError()
        if self.seats[row][col] != '':
            raise SeatReservedError(seat)
        if user in self.user_reservations:
            raise UserReservedError(user, seat)

        self.seats[row][col] = user
        self.user_reservations[user] = seat
        print(f"Uzytkownik {user} zarezerwował miejsce {seat}.")

    def cancellation(self, user, seat):
        row, col = self._parse_seat(seat)
        if self.seats[row][col] != user:
            raise CancellationError()
        self.seats[row][col] = ''
        del self.user_reservations[user]
        print(f"Udane usuniecie rezerwacji miejsca {seat}.")


    def _parse_seat(self, seat):
        row = ord(seat[0].upper()) - 65
        col = int(seat[1:]) - 1

        if row < 0 or row >= len(self.seats) or col < 0 or col >= len(self.seats[0]):
            raise NotFoundError(seat)
        return row, col
    

####################
kino = Cinema(5, 5)  # Creates a 5x5 seating arrangement

try:
    kino.reserve_seat("Marta Niemiec", "A2")
    kino.reserve_seat("Barbara Cisza", "A2")
except ReservationError as e:
    print(e)

try:
    kino.cancellation("Barbara Cisza", "A2")
except ReservationError as e:
    print(e)

