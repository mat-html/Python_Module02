class GardenError(Exception):
    def __init__ (self, 
                  message:str = "Unknown plant error"
                  ) -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__ (self,
                  message:str = "Unknown plant error"
                 ) -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__ (self,
                  message:str = "Unkonwn plant error"
                 ) -> None:
        super().__init__(message)


def test_plant_error():
    raise PlantError("The Tomato plant is wilting!")


def test_water_error() -> None:
    raise WaterError("Not enought water in the tank!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===", end="\n\n")
    print("Testing PlantError...")
    try:
        test_plant_error()
    except PlantError as err:
        print(f"Caught PlantError: {err}")
    print()
    print("Testing WaterError...")
    try:
        test_water_error()
    except WaterError as err:
        print(f"Caught WaterError: {err}")
    print()
    print("Testing GardenError...")
    try:
        test_plant_error()
    except GardenError as err:
        print(f"Caught GardenError: {err}")
    try:
        test_water_error()
    except GardenError as err:
        print(f"Caught GardenError: {err}")
    print()
    print("All custom error types work correctlly!")