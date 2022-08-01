import argparse


def main():
    parser = argparse.ArgumentParser('Enter the name of the file and get the number of words in it')
    parser.add_argument('filename', type=argparse.FileType('r'))
    args = parser.parse_args()
    print(len(args.filename.read().replace('\n', ' ').replace('\t', ' ').split()))


if __name__ == '__main__':
    main()
