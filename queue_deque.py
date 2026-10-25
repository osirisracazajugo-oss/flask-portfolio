from collections import deque


class Queue:

    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0

    def to_list(self):
        return list(self._items)

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return f"Queue({list(self._items)})"


class Deque:

    def __init__(self):
        self._items = deque()

    def add_front(self, item):
        self._items.appendleft(item)

    def add_rear(self, item):
        self._items.append(item)

    def remove_front(self):
        if self.is_empty():
            raise IndexError("remove from empty deque")
        return self._items.popleft()

    def remove_rear(self):
        if self.is_empty():
            raise IndexError("remove from empty deque")
        return self._items.pop()

    def peek_front(self):
        if self.is_empty():
            raise IndexError("peek from empty deque")
        return self._items[0]

    def peek_rear(self):
        if self.is_empty():
            raise IndexError("peek from empty deque")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def to_list(self):
        return list(self._items)

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return f"Deque({list(self._items)})"


def queue_menu():
    q = Queue()

    while True:
        print("\n--- QUEUE MENU ---")
        print("1. Enqueue (Add item)")
        print("2. Dequeue (Remove first item)")
        print("3. Peek (View first item)")
        print("4. Display queue")
        print("5. Check size")
        print("6. Back")

        choice = input("Choose an option: ")

        if choice == "1":
            item = input("Enter item: ")
            q.enqueue(item)
            print("Item added.")

        elif choice == "2":
            try:
                print("Removed:", q.dequeue())
            except IndexError:
                print("The queue is empty.")

        elif choice == "3":
            try:
                print("First item:", q.peek())
            except IndexError:
                print("The queue is empty.")

        elif choice == "4":
            print(q)

        elif choice == "5":
            print("Queue size:", len(q))

        elif choice == "6":
            break

        else:
            print("Invalid choice.")


def deque_menu():
    d = Deque()

    while True:
        print("\n--- DEQUE MENU ---")
        print("1. Add to front")
        print("2. Add to rear")
        print("3. Remove from front")
        print("4. Remove from rear")
        print("5. Peek at front")
        print("6. Peek at rear")
        print("7. Display deque")
        print("8. Check size")
        print("9. Back")

        choice = input("Choose an option: ")

        if choice == "1":
            d.add_front(input("Enter item: "))
        elif choice == "2":
            d.add_rear(input("Enter item: "))
        elif choice == "3":
            try:
                print("Removed:", d.remove_front())
            except IndexError:
                print("The deque is empty.")
        elif choice == "4":
            try:
                print("Removed:", d.remove_rear())
            except IndexError:
                print("The deque is empty.")
        elif choice == "5":
            try:
                print("Front:", d.peek_front())
            except IndexError:
                print("The deque is empty.")
        elif choice == "6":
            try:
                print("Rear:", d.peek_rear())
            except IndexError:
                print("The deque is empty.")
        elif choice == "7":
            print(d)
        elif choice == "8":
            print("Deque size:", len(d))
        elif choice == "9":
            break
        else:
            print("Invalid choice.")


def main():
    while True:
        print("\n=== QUEUE AND DEQUE SYSTEM ===")
        print("1. Queue")
        print("2. Deque")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            queue_menu()
        elif choice == "2":
            deque_menu()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()