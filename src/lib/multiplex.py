import selectors


class Multiplexer():
    """ Copies data from a list of inputs to a list of output.
        Inputs and outputs must be file objects.
    """

    def __init__(self, inputs, outputs):
        self.inputs = inputs
        self.outputs = outputs
        self.sel = selectors.DefaultSelector()

    def run(self):
        """ blocks until all input streams are closed """

        for f in self.inputs:
            self.sel.register(f, selectors.EVENT_READ, self._write)

        while True:
            # epoll breaks if we call select() after everything is unregistered.
            # so stop early if there is nothing left to select on.
            if len(self.sel._fd_to_key) == 0:
                break

            events = self.sel.select()

            if len(events) == 0:
                break

            for key, mask in events:
                callback = key.data
                callback(key.fileobj)

        self.sel.close()

    def _write(self, stream):
        data = stream.read()
        if data:
            for f in list(self.outputs):
                if f.closed:
                    self.outputs.remove(f)

                if type(data) == str:
                    f.write(data)
                else:
                    f.write(data.decode('utf-8'))
                f.flush()
        else:
            self.sel.unregister(stream)

    def write(self, string):
        for f in self.outputs:
            if not f.closed:
                f.write(string)
                f.flush()
