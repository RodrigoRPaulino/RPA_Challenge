from app.dispatcher.dispatcher import Dispatcher


def main():
    dispatcher = Dispatcher()

    items = dispatcher.run(
        r"C:\Users\rodri\Downloads\challenge.xlsx"
    )

    print(items[0])


if __name__ == "__main__":
    main()