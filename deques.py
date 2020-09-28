class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        """Accept an item and inserts that item into the 0th index of the list
        that represent the Deque.

        Runtime is O(n), or linear time because inserting into the 0th index of
        the list forces all other items to move one index to the right
        """
        self.items.insert(0, item)

    def add_rear(self, item):
        """Accept an item and appends that item to the end of the list that
        represent the Deque.

        The runtime of the method is O(1) or constant time because appending in
        end of a list happen in constant time
        """
        self.items.append(item)

    def remove_front(self):
        """Removes and returns the item in the 0th index of the list,
        which represents the frontof the Deque.

        Runtime is O(n), or linear time because removing an item from the 0th 
        index of the list all other items have to shift one index to the left.
        """
        if self.items:
            return self.items.pop(0)

        return None

    def remove_rear(self):
        """Removes and returns the last item of the list which represents the 
        rear of the Deque.

        The runtime of the method is O(1) or constant, because all it does is 
        index to the last item of the list.
        """
        if self.items:
            return self.items.pop()

        return None

    def peek_front(self):
        """Returns the item at the 0th index of list which represent front
        item of the Deque.

        The runtime of the method is O(1) or constant, because indexing into a
        list is do in constant time
        """
        if self.items:
            return self.items[0]

        return None

    def peek_rear(self):
        """Returns the item at the -1st index of list which represent last
        item of the Deque.

        The runtime of the method is O(1) or constant, because indexing into a
        list is do in constant time.
        """
        if self.items:
            return self.items[-1]

        return None
    
    def size(self):
        """Return length of the list representing the Deque

        The runtime of the method is O(1) or constant, because finding the 
        length of a list happen in a constant time
        """
        return len(self.items)

    def is_empty(self):
        """Return a boolean value describing whether or not the Deque is empty

        The runtime of the method is O(1) or constant, testing for equality
        happen in constant time
        """
        return self.items == []



# Real Example: Palindrome checker
# A Palindrome is a word that is spelled the same backwards and forwards:

## Inefficient
def palindrome_checker(word):
    f_start = Deque()
    r_start = Deque()
    for char in word:
        f_start.add_front(char)
        r_start.add_rear(char)

        if f_start.peek_front() != r_start.peek_rear():
            return False
        else:
            continue
    return True
            
print(palindrome_checker("mom"))
print(palindrome_checker("oranges"))
print(palindrome_checker("racecar"))

## Efficient
# add to rear is constant

def palindrome_checker(word):
    word_deque = Deque()
    for char in word:
        word_deque.add_rear(char)

    while word_deque.size() >= 2:
        front_char = word_deque.remove_front()
        rear_char = word_deque.remove_rear()

        if front_char != rear_char:
            return False
    return True


print(palindrome_checker("racecar"))
print(palindrome_checker("oranges"))