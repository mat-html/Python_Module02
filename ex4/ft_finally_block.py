class GardenError(Exception):
    def __init__(self,
                 message: str = "Unknown plant error"
                 ) -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self,
                 message: str = "Unknown plant error"
                 ) -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self,
                 message: str = "Unkonwn plant error"
                 ) -> None:
        super().__init__(message)


def test_plant_error():
    raise PlantError("The Tomato plant is wilting!")


def test_water_error() -> None:
    raise WaterError("Not enought water in the tank!")


def water_plant(plant_name) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:
    plant_name = ["Tomato", "Lettuce", "Carrots"]
    print("Opening watering system")
    try:
        for plant in plant_name:
            water_plant(plant)
    except PlantError as err:
        print(f"Caught PlantError: {err}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


def test_invalid_watering_system() -> None:
    plant_name = ["Tomato", "lettuce", "Carrots"]
    print("Opening watering system")
    try:
        for plant in plant_name:
            water_plant(plant)
    except PlantError as err:
        print(f"Caught PlantError: {err}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print()
    print("Testing valid plants...")
    test_watering_system()
    print()
    print("Testing invalid plants...")
    test_invalid_watering_system()
    print()
    print("Cleanup always happens, even with errors!")
