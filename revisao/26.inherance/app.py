class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print('Disconnected')



class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def is_print(self, pages):
        if not self.connected:
            print('Your print is not connected')
            return

        print(f"Printing {pages} pages")
        self.remaining_pages -= pages


printer = Printer('HP', 'USB', 200)
printer.is_print(5)
print(printer)
printer.disconnect()
printer.is_print(45)