from random import randint


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Accept an item and inserts that item into the 0th index of the list
        that represent the queue.

        Runtime is O(n), or linear time because inserting into the 0th index of
        the list forces all other items to move one index to the right
        """
        self.items.insert(0, item)

    def dequeue(self):
        """Removes and returns the front-most item of the Queue which is
        represented by last item of the list.

        The runtime of the method is O(1) or constant, because all it does is 
        index to the last item of the list.
        """
        if self.items:
            return self.items.pop()

        return None

    def peek(self):
        """Returns the last(Top) item in the list which represent front-most
        item of the Queue.

        The runtime of the method is O(1) or constant, because indexing into a
        list is do in constant time
        """
        if self.items:
            return self.items[-1]

        return None

    def size(self):
        """Return length of the list representing the Queue

        The runtime of the method is O(1) or constant, because finding the 
        length of a list happen in a constant time
        """
        return len(self.items)

    def is_empty(self):
        """Return a boolean value describing whether or not the Queue is empty

        The runtime of the method is O(1) or constant, testing for equality
        happen in constant time
        """
        return self.items == []


# Real World Example :- print queue challengs


class PrintQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.items:
            return self.items.pop()

        return None

    def is_empty(self):
        return self.items == []


class Job:
    def __init__(self):
        self.pages = randint(1, 11)

    def print_page(self):
        """Decrement pages
        """
        if self.pages > 0:
            self.pages -= 1

    def check_complete(self):
        """Check if job has been completed
        """
        return self.pages == 0

    def __str__(self):
        return self.pages

    def __repr__(self):
        return f"Pages: {self.pages}"


class Printer:
    def __init__(self):
        self.current_job = None

    def get_job(self, print_queue):
        """
        """
        try:
            self.current_job = print_queue.dequeue()
        except IndexError:
            return "No more jobs to print."

    def print_job(self, job):
        while job.pages > 0:
            job.print_page()

        if job.check_complete():
            return "Printing complete."
        else:
            return "An error occurred."

job1 = Job()
print_q = PrintQueue()
printer = Printer()
print_q.enqueue(job1)
print(print_q.items)
printer.get_job(print_q)
print(print_q.items)

print(printer.print_job(printer.current_job))