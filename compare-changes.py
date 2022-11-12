import csv
import sys
import os
import pprint


def size_dictionary(sizes):
    size_map = {}
    for row in sizes:
        directory_or_file = row[1]
        size = int(row[0])
        size_map[directory_or_file] = size
    return size_map


def print_results(old_sizes, new_sizes):
    directories = set(old_sizes.keys()).union(new_sizes.keys())
    size_change_map = {}
    for directory in directories:
        if directory in old_sizes and directory in new_sizes:
            # size has changed
            size_change = new_sizes[directory] - old_sizes[directory]
            if size_change != 0:
                size_change_map[directory] = size_change
        elif directory in old_sizes and (not (directory in new_sizes)):
            # deleted
            size_change_map[directory] = -old_sizes[directory]
        elif (not (directory in old_sizes)) and directory in new_sizes:
            # introduced
            size_change_map[directory] = new_sizes[directory]
        else:
            raise AssertionError("unreachable")
    pp = pprint.PrettyPrinter(indent=2)
    # pp.pprint(size_change_map)

    sorted_map = {
        k: v
        for k, v in sorted(
            size_change_map.items(), key=lambda item: item[1], reverse=True
        )
    }
    # pp.pprint(sorted_map)

    for (directory, size) in sorted_map.items():
        if size >= 0:
            size_string = f"+{size}"
        else:
            size_string = f"{size}"
        print(f"{size_string} {directory}")

    root_size_change = size_change_map["."]
    if root_size_change != 0:
        print("\n\n-----------------------------")
        print(f"Total size change: {root_size_change} MB")
        print("-----------------------------")


def run(argv):
    file_list = []
    for file in os.listdir(os.getcwd()):
        if file.endswith(".tsv"):
            file_list.append(file)

    file_list.sort()
    old_size_file = file_list[len(file_list) - 2]
    new_size_file = file_list[len(file_list) - 1]
    print(f"Read old sizes from {old_size_file}")
    print(f"Read new sizes from {new_size_file}")
    tsvin1 = csv.reader(open(old_size_file, "rt"), delimiter="\t")  # old
    tsvin2 = csv.reader(open(new_size_file, "rt"), delimiter="\t")  # new

    old_sizes = size_dictionary(tsvin1)
    new_sizes = size_dictionary(tsvin2)
    print_results(old_sizes=old_sizes, new_sizes=new_sizes)


if __name__ == "__main__":
    run(sys.argv[1:])
