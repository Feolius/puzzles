from queue import Queue


class QueueWrapper(Queue):
    def __init__(self):
        super().__init__()
        self.low_count: int = 0
        self.high_count: int = 0

    def put(self, item, block = True, timeout = None):
        super().put(item, block, timeout)
        if item.signal:
            self.high_count += 1
        else:
            self.low_count += 1




class Pulse:
    def __init__(self, source: str, dest: str, signal: bool):
        self.source: str = source
        self.dest: str = dest
        self.signal: bool = signal


class Module:
    def __init__(self, name):
        self.name: str = name
        self.outputs: list[str] = []

    def add_output(self, output):
        self.outputs.append(output)

    def _put_output_pulses(self, queue: Queue[Pulse], signal: bool):
        for output in self.outputs:
            queue.put(Pulse(self.name, output, signal))

    def handle(self, pulse: Pulse, queue: Queue[Pulse]):
        pass


class FlipFlop(Module):
    def __init__(self, name: str):
        super().__init__(name)
        self.status = False

    def handle(self, pulse: Pulse, queue: Queue[Pulse]):
        if not pulse.signal:
            self.status = not self.status
            self._put_output_pulses(queue, self.status)


class Conjunction(Module):
    def __init__(self, name: str):
        super().__init__(name)
        self.state: dict[str, bool] = {}

    def add_input(self, name: str):
        self.state[name] = False

    def handle(self, pulse: Pulse, queue: Queue[Pulse]):
        self.state[pulse.source] = pulse.signal
        if all(input for input in self.state.values()):
            self._put_output_pulses(queue, False)
        else:
            self._put_output_pulses(queue, True)


f = open("input.txt")
rows = f.read().splitlines()
modules: dict[str, Module] = {}
broadcaster = []
modules_outputs: dict[str, list[str]] = {}
for row in rows:
    name_part, outputs_part = row.split(" -> ")
    outputs = outputs_part.split(", ")
    if name_part == "broadcaster":
        broadcaster = outputs
        continue
    name = name_part[1:]
    modules_outputs[name] = outputs
    if name_part[0] == "%":
        modules[name] = FlipFlop(name)
    else:
        modules[name] = Conjunction(name)

for name in modules_outputs:
    outputs = modules_outputs[name]
    modules[name].outputs.extend(outputs)
    for output_name in outputs:
        if output_name not in modules:
            modules[output_name] = Module(output_name)
        output_module = modules[output_name]
        if isinstance(output_module, Conjunction):
            output_module.add_input(name)

low_res = 0
high_res = 0
for i in range(1000):
    low_res += 1
    queue = QueueWrapper()
    for init_mod_name in broadcaster:
        queue.put(Pulse("broadcast", init_mod_name, False))
    while not queue.empty():
        pulse = queue.get()
        modules[pulse.dest].handle(pulse, queue)
    low_res += queue.low_count
    high_res += queue.high_count

print(low_res * high_res)




