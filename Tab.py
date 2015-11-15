class Tab(object):
    def __init__(self, strings="EADGBe"):
        self.strings = [s for s in strings]
        self.blocks = []

    def tab_block(self, *args, **kwargs):
        b = TabBlock(*args, strings=self.strings, **kwargs)
        self.blocks.append(b)
        return b

    def chord_block(self, *args, **kwargs):
        b = ChordBlock(*args, strings=self.strings, **kwargs)
        self.blocks.append(b)
        return b

    def render(self):
        result = ""
        for b in self.blocks:
            result += b._render()
        return result


class Block(object):
    """
    Parent class for individual sections of the tab
    """
    def __init__(self, strings="EADGBe"):
        self.strings = [s for s in strings]

    def __str__(self):
        return self._render()

    def __mul__(self, other):
        return [self for i in range(other)]

    def __rmul__(self, other):
        return self * other

    def _render(self):
        pass


class TabBlock(Block):
    """
    Standard tablature block for more complex sections of the song
    """
    def __init__(self, measures, beats_per_measure=4, notes=[], **kwargs):
        super(TabBlock, self).__init__(**kwargs)
        self.measures = measures
        self.beats_per_measure = beats_per_measure

    def _render(self):
        lines = [s for s in self.strings]
        for line in range(len(lines)):
            for measure in range(self.measures):
                lines[line] += "|"
                for beat in range(self.beats_per_measure):
                    lines[line] += "-"
        return "\n".join(lines)


class ChordBlock(Block):
    """
    Block for simpler sections. Chord progressions intermixed with lyrics.
    """
    pass

t = Tab()
t.tab_block(1, notes=[{
    "E": 0,
    "A": 2,
    "D": 2,
}, {}, {
    "E": 3,
    "A": 2,
    "D": 0,
    "G": 0,
    "B": 0,
    "e": 3,
}, {}])
print t.render()