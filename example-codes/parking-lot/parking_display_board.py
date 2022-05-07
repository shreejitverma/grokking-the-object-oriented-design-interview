class ParkingDisplayBoard:
    def __init__(self, id):
        self.__id = id
        self.__handicapped_free_spot = None
        self.__compact_free_spot = None
        self.__large_free_spot = None
        self.__motorbike_free_spot = None
        self.__electric_free_spot = None

    def show_empty_spot_number(self):
        message = ""
        if self.__handicapped_free_spot.is_free():
            message += f"Free Handicapped: {self.__handicapped_free_spot.get_number()}"
        else:
            message += "Handicapped is full"
        message += "\n"

        if self.__compact_free_spot.is_free():
            message += f"Free Compact: {self.__compact_free_spot.get_number()}"
        else:
            message += "Compact is full"
        message += "\n"

        if self.__large_free_spot.is_free():
            message += f"Free Large: {self.__large_free_spot.get_number()}"
        else:
            message += "Large is full"
        message += "\n"

        if self.__motorbike_free_spot.is_free():
            message += f"Free Motorbike: {self.__motorbike_free_spot.get_number()}"
        else:
            message += "Motorbike is full"
        message += "\n"

        if self.__electric_free_spot.is_free():
            message += f"Free Electric: {self.__electric_free_spot.get_number()}"
        else:
            message += "Electric is full"

        print(message)

