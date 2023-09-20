class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    # prints the linked list
    def printList(self):

        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    # delete a key value
    def deletion(self, key):

        temp = self.head

        # for the head node
        while temp:
            if (temp.data == key):
                # sets the head to the next value
                self.head = temp.next
                # clears the value of the current head
                temp = None
                return

        # searches the rest of the linked list
        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # value is not present
        if (temp == None):
            return

        # unlink the node from the linked list
        prev.next = temp.next
        temp = None

    # two pointers solution
    def two_pointers(self):

        temp = self.head
        arr = []

        # instead of having the second ptr here, move it to inside the loop
        # move = self.head.next

        # inner loop
        while temp:
            # Reset move to the node next to temp for each iteration of the outer loop
            move = temp.next
            while move:
                if move.data == temp.data:
                    arr.append(move.data)
                move = move.next
            temp = temp.next
        return arr


linked = LinkedList()
node1 = Node(1)
node2 = Node(1)
node3 = Node(2)
node4 = Node(3)
node5 = Node(3)

linked.head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print(linked.two_pointers())
