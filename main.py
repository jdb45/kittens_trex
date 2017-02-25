from config import huey
from tasks import tweet_gif


def main():
    while True:
        print('1. Tweet kitten\n2. Tweet T-Rex\n3. Quit')
        choice = input('Enter choice')
        if choice == '1':
            tweet_gif('kitten')
            print('Kitten gif tweet queued')
        elif choice == '2':
            tweet_gif('trex')
            print('Trex gif queued')
        elif choice == '3':
            break
        else:
            print('Not a choice. Try again?')


if __name__ == '__main__':
    main()
