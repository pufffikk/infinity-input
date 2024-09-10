def main():
    try:
        while True:
            text = input()
            print(text)
    except KeyboardInterrupt:
        print("Program interrupted by user.")


if __name__ == '__main__':
    main()
