import argparse

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def main():
    parser = argparse.ArgumentParser(description="CLI Unit Converter for Temperature")

    parser.add_argument(
        "-t", "--temp",
        type=float,
        required=True,
        help="Temperature value to convert"
    )

    parser.add_argument(
        "-c2f",
        action="store_true",
        help="Convert Celsius to Fahrenheit"
    )

    parser.add_argument(
        "-f2c",
        action="store_true",
        help="Convert Fahrenheit to Celsius"
    )

    args = parser.parse_args()

    if args.c2f:
        result = celsius_to_fahrenheit(args.temp)
        print(f"{args.temp}°C = {result:.2f}°F")
    elif args.f2c:
        result = fahrenheit_to_celsius(args.temp)
        print(f"{args.temp}°F = {result:.2f}°C")
    else:
        print("Please specify conversion direction: --c2f or --f2c")

if __name__ == "__main__":
    main()

