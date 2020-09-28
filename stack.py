class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Accept item as a param and appends at the end of the list.
        Return nothing

        The runtime of the method is O(1) or constant time because appending in
        end of a list happen in constant time
        """
        self.items.append(item)

    def pop(self):
        """Removes and returns the last item of the list

        The runtime of the method is O(1) or constant, because all it does is 
        index to the last item of the list.
        """
        if self.items:
            return self.items.pop()

        return None

    def peek(self):
        """Returns the last(Top) item of the list

        The runtime of the method is O(1) or constant, because indexing into a
        list is do in constant time
        """
        if self.items:
            return self.items[-1]

        return None

    def size(self):
        """Return length of the list representing the stack

        The runtime of the method is O(1) or constant, because finding the 
        length of a list happen in a constant time
        """
        return len(self.items)

    def is_empty(self):
        """Return a boolean value describing whether or not the stack is empty

        The runtime of the method is O(1) or constant, testing for equality
        happen in constant time
        """
        return self.items == []


# Real World Examples


def match_symbols(symbol_str):

    symbol_pairs = {"(": ")", "[": "]", "{": "}"}

    openers = symbol_pairs.keys()
    symbol_stack = Stack()

    index = 0
    while index < len(symbol_str):
        symbol = symbol_str[index]

        if symbol in openers:
            symbol_stack.push(symbol)
        else:  # Symbol is a closer

            # if stack is already empty the symbols are not balanced
            if symbol_stack.is_empty():
                return False

            # If there are items in the stack check for a mismatch
            else:
                top_item = symbol_stack.pop()
                if symbol != symbol_pairs[top_item]:
                    return False

        index += 1

    if symbol_stack.is_empty():
        return True


print(match_symbols("[{[(())]}]"))
print(match_symbols("[]][{[](())[]}"))
