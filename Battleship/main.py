import sys
from src.game import Game

if __name__ == '__main__':
    config_file_path = sys.argv[1]
    with open(config_file_path) as cfg:
        ship_args = dict()
        for line_num, line in enumerate(cfg):
            split_line = line.split()
            if line_num == 0:
                num_rows, num_cols = (int(x.strip()) for x in split_line)
            else:
                ship_args[split_line[0]] = int(split_line[1])
    print(f'num_rows = {num_rows}, num_cols = {num_cols}')
    print(f'ships = {ship_args}')
    game = Game(ship_args, num_rows, num_cols)
