def input_temperature(temp_str: str) -> int:
    if int(temp_str) > 40:
        raise ValueError(f"{temp_str}°C is too hot for plants (max 40°C)")
    elif int(temp_str) < 0:
        raise ValueError(f"{temp_str}°C is too cold for plants (min 0°C)")
    return int(temp_str)


def test_temperature() -> None:
    input_list = ["25", "abc", "100", "-50"]
    for input in input_list:
        try:
            print(f"Input data is '{input}'")
            input_temperature(input)
            print(f"Temperature is now {input}°C", end="\n\n")
        except ValueError as err:
            print(f"Caught input_temperature error: {err}", end="\n\n")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    print()
    test_temperature()
