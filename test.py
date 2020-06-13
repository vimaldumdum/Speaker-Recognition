import argparse

def arguments():
    parser= argparse.ArgumentParser(description='meh')
    parser.add_argument('-t', '--task', type=int, required=True)
    ret=parser.parse_args()

if __name__ == '__main__':
    args=arguments()
    print(args.task)
    # -t 6