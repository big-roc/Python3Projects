# coding:utf8
from leetcode.data_structure.linked_list import Node, LinkedList


def insert_to_front_test():
    linked_list = LinkedList(None)
    linked_list.insert_to_front(10)
    print(linked_list.get_all_data())

    linked_list.insert_to_front(None)
    print(linked_list.get_all_data())

    linked_list.insert_to_front('a')
    linked_list.insert_to_front('bc')
    print(linked_list.get_all_data())


def append_test():
    linked_list = LinkedList(None)
    linked_list.append(10)
    print(linked_list.get_all_data())

    linked_list.append(None)
    print(linked_list.get_all_data())

    linked_list.append('a')
    linked_list.append('bc')
    print(linked_list.get_all_data())


def find_test():
    linked_list = LinkedList(None)
    node = linked_list.find('a')
    print(node)

    head = Node(10)
    linked_list = LinkedList(head)
    node = linked_list.find(None)
    print(node)

    head = Node(10)
    linked_list = LinkedList(head)
    linked_list.insert_to_front('a')
    linked_list.insert_to_front('bc')
    node = linked_list.find('a')
    print(node)

    node = linked_list.find('aaa')
    print(node)


def delete_test():
    linked_list = LinkedList(None)
    linked_list.delete('a')
    print(linked_list.get_all_data())

    head = Node(10)
    linked_list = LinkedList(head)
    linked_list.delete(None)
    print(linked_list.get_all_data())

    head = Node(10)
    linked_list = LinkedList(head)
    linked_list.insert_to_front('a')
    linked_list.insert_to_front('bc')
    linked_list.delete('a')
    print(linked_list.get_all_data())

    linked_list.delete('aa')
    print(linked_list.get_all_data())


def len_test():
    linked_list = LinkedList(None)
    print(len(linked_list))

    head = Node(10)
    linked_list = LinkedList(head)
    linked_list.insert_to_front('a')
    linked_list.insert_to_front('bc')
    print(len(linked_list))


def main():
    # insert_to_front_test()
    # append_test()
    # find_test()
    # delete_test()
    len_test()


if __name__ == '__main__':
    main()
