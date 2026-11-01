def garden_operations(operation_number) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("/non/existent/file", "r")
    elif operation_number == 3:
        "abc" + 42


def test_error_types() -> None:
    for i in [0, 1, 2, 3, 4]:
        try:
            print(f"Testing operation {i}...")
            garden_operations(i)
            print("Operation completed successfully!")
        except ValueError as err:
            print(f"Caught ValueError: {err}")
        except ZeroDivisionError as err:
            print(f"Caught ZeroDivisionError: {err}")
        except FileNotFoundError as err:
            print(f"Caught FileNotFound: {err}")
        except TypeError as err:
            print(f"Caught TypeError: {err}")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print()
    print("All error types tested successfully!")
