class Parking:
    def __init__(self):
        self.levels = {'A': [None] * 20, 'B': [None] * 20}

    def assign_parking_spot(self, vehicle_number):
        for level, spots in self.levels.items():
            for spot, occupied_vehicle in enumerate(spots, start=1):
                if occupied_vehicle is None:
                    if vehicle_number in self.levels[level]:
                        return {"level": level, "spot": "Already occupied vehicle NO."}
                    self.levels[level][spot - 1] = vehicle_number
                    return {"level": level, "spot": spot}
        return None

    def retrieve_parking_spot(self, vehicle_number):
        for level, spots in self.levels.items():
            for spot, occupied_vehicle in enumerate(spots, start=1):
                if occupied_vehicle == vehicle_number:
                    self.levels[level][spot - 1] = None
                    return {"level": level, "spot": spot}
        return None

def main():
    parking_lot = Parking()

    while True:
        print("\nOptions:")
        print("1. Assign a parking spot")
        print("2. Retrieve parking spot number")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            vehicle_number = input("Enter vehicle NO: ")
            result = parking_lot.assign_parking_spot(vehicle_number)
            if result:
                print(f"Parking spot assigned: {result}")
            else:
                print("Sorry, the parking lot is full.")

        elif choice == '2':
            vehicle_number = input("Enter vehicle NO: ")
            result = parking_lot.retrieve_parking_spot(vehicle_number)
            if result:
                print(f"Parking spot for vehicle {vehicle_number}: {result}")
            else:
                print(f"Vehicle {vehicle_number} not found in the parking lot.")

        elif choice == '3':
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
