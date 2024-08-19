from time import sleep
from BackendWorker.game import Game


def main() -> None:
    game = Game()
    del game


if __name__ == "__main__":
    sleep(5)  # Simulating starting... (for actions)
    main()
