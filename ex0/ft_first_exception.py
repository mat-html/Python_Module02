def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    input_list = ["25", "abc"]
    for input in input_list:
        try:
            print(f"Input data is '{input}'")
            input_temperature(input)
            print(f"Temperature is now {input}°C")
            print()
        except ValueError as err:
            print(f"Caught input_temperature error: {err}")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    print()
    test_temperature()
    print()
    print("All tests completed - program didn't crash!")
