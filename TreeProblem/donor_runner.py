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
        for line_num, line in enumerate(cfg):
            split_line = line.split(" : ")
            donor_name, donor_amount = split_line[0].strip(), int(split_line[1].strip())
            #create donor object and add it to the tree
            donor_info = Donor(donor_name, donor_amount)
            donor_tree.add_value(donor_info)
    donor_node = None
    if command == 'all':
        donor_node = donor_tree.get_min_node()
        while donor_node is not None:
            print(str(donor_node.value))
            donor_node = donor_tree.successor(donor_node)
    elif command == 'cheap':
        donor_node = donor_tree.get_min_node()
    elif command == 'rich':
        donor_node = donor_tree.get_max_node()
    elif command == 'who':
        amount_arg = sys.argv[3]
        if amount_arg[0] == '+':
            # who +amount: Prints the first donor that donated at least amount if any
            amount = int(amount_arg[1:])
            donor_node = donor_tree.upper_bound(amount)
            
        elif amount_arg[0] == '-':
            # who -amount: Prints the first donor that donated no more than amount if any
            amount = int(amount_arg[1:])
            donor_node = donor_tree.lower_bound(amount)
        else:
            # who amount: Prints the first donor that who donated amount if any
            amount = int(amount_arg)
            try:
                donor_node = donor_tree.get_node(amount)
            except MissingValueError:
                print('No Match')
    if donor_node is not None:
        print(str(donor_node.value))
