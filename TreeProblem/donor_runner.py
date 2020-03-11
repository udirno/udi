# Your solution for the donor problem here
import sys
from Trees.src.trees.bst_tree import BST, MissingValueError
from Trees.src.nodes.bst_node import BSTNode
from Trees.src.donor_prog.donor import Donor

if __name__ == '__main__':
    donor_file_path = sys.argv[1]
    command = sys.argv[2]
    donor_tree = BST(None, lambda x: x.amount)

    with open(donor_file_path) as cfg:
        ship_args = dict()
        for line_num, line in enumerate(cfg):
            split_line = line.split(" : ")
            if line_num == 0:
                donor_name, donor_amount = (int(x.strip()) for x in split_line)
                #create donor object and add it to the tree
                donor_info = Donor(donor_name, donor_amount)
                donor_tree.add_value(donor_info)
            else:
                ship_args[split_line[0]] = int(split_line[1])
    random.seed(int(sys.argv[2]))
    #print(f'num_rows = {num_rows}, num_cols = {num_cols}')
    #print(f'ships = {ship_args}')
    game = Game(ship_args, num_rows, num_cols)
    game.play()
