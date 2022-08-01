import argparse


def main():
    parser = argparse.ArgumentParser('2 numbers and an action \n\t if the action is *, enter "*"')
    parser.add_argument('num_1', type=int, help="number1")
    parser.add_argument('act', type=str, help="action")
    parser.add_argument('num_2', type=int, help="number2")
    args = parser.parse_args()
    res = None
    if args.act == '+':
        res = args.num_1 +args.num_2
    elif args.act == '+':
        res = args.num_1 - args.num_2
    elif args.act == '*':
        res = args.num_1 * args.num_2
    elif args.act == '**':
        res = args.num_1 ** args.num_2
    elif args.act == '/':
        try:
            res = args.num_1 / args.num_2
        except ZeroDivisionError:
            res = f'{args.num_1}/{args.num_2}'
    print(f'{args.num_1} {args.act} {args.num_2} = {res}')


if __name__ == "__main__":
    main()
