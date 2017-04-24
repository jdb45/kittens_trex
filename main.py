from config import huey
from tasks import tweet_gif


def main():
    global res
    holding_list = []
    while True:
        print('1. Tweet kitten gif\n2. Tweet T-Rex gif\n3. Quit')
        choice = input('Enter choice: ')
        if choice == '1':
            res = tweet_gif('kitten')
            print('Kitten gif tweet queued')
        elif choice == '2':
            res = tweet_gif('trex')
            print('Trex gif queued')
        elif choice == '3':
            break
        else:
            print('Not a choice. Try again? ')
            #adding each file path to the list and making sure there is data to add
        holding_list.append(res(blocking=True))
    print(holding_list)

if __name__ == '__main__':
    main()
