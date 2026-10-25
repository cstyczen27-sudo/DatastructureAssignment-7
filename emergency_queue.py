class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency



class MinHeap:
    def __init__(self):
        self.data = []

    def heapify_up(self, urgency):
        while urgency > 0:
            parent_index = (urgency - 1) // 2
            current_task = self.data[urgency]
            parent_task = self.data[parent_index]
            if current_task.urgency < parent_task.urgency:
                temp = self.data[urgency]
                self.data[urgency] = self.data[parent_index]
                self.data[parent_index] = temp

                urgency = parent_index
            else:
                break

    def heapify_down(self, urgency):
        left = 2 * urgency + 1
        right = 2 * urgency + 2
        smallest = urgency

        if left < len(self.data) and self.data[left].urgency < self.data[smallest].urgency:
            smallest = left

        if right < len(self.data) and self.data[right].urgency < self.data[smallest].urgency:
            smallest = right

        if smallest != urgency:
            temp = self.data[urgency]
            self.data[urgency] = self.data[smallest]
            self.data[smallest] = temp

            self.heapify_down(smallest)

    def insert(self, name):
        self.data.append(name)
        self.heapify_up(len(self.data) - 1)

    def remove_min(self):
        if not self.data:
            return None

        if len(self.data) == 1:
            return self.data.pop()

        min_value = self.data[0]
        self.data[0] = self.data.pop()
        self.heapify_down(0)
        return min_value

    def peek(self):
        most_urgent = self.data[0]
        print(most_urgent)

    def print_heap(self):
        print('\n List of Patients')
        for Patient in self.data:
            print(f'Name:{Patient.name} Urgency {Patient.urgency}')
# Test your MinHeap class here including edge cases
