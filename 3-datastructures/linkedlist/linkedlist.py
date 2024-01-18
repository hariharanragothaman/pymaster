"""
Fundamental Template for LinkedList
"""
# General Definition of a node


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        return

    def push_elements(self, item):
        """
        :param item: Push elements into a SLL
        :return:
        """
        if not isinstance(item, ListNode):
            item = ListNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
        return

    def print_list(self):
        current = self.head
        while current:
            print(current.val, end=" ")
            current = current.next
        return

    def reverse_list(self):
        prev = None
        current = self.head
        while current is not None:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

    def has_cycle(self):
        fast = self.head
        slow = self.head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

    def delete_element_given_value(self, data):
        current = self.head
        while current:
            if current.next.val == data:
                current.next = current.next.next
                break
        return

    def delete_node_given_only_node(self, node):
        while node.next:
            node.val = node.next.val
            if node.next.next is None:
                node.next = None
                break
            else:
                node = node.next

    def get_middle_node(self):
        slow = self.heaf
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        return slow

    def delete_duplicates(self):
        # Assume I/P list is sorted
        current = self.head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return self.head


if __name__ == "__main__":
    s1 = ListNode(5)
    s2 = ListNode(6)
    s3 = ListNode(7)
    s4 = ListNode(8)

    t1 = LinkedList()

    t1.push_elements(s1)
    t1.push_elements(s2)
    t1.push_elements(s3)
    t1.push_elements(s4)

    print("Intial LinkedList")
    t1.print_list()

    print("\n")
    print("Reversing the List")
    t1.reverse_list()
    t1.print_list()
