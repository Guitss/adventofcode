"""
--- Day 6: Probably a Fire Hazard ---
Because your neighbors keep defeating you in the holiday house decorating contest year
after year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you
instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each
corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn
on, turn off, or toggle various inclusive ranges given as coordinate pairs.
Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate
pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square.
The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing
the instructions Santa sent you in order.

For example:

turn on 0,0 through 999,999 would turn on (or leave on) every light.
toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the
ones that were on, and turning on the ones that were off.
turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.

After following the instructions, how many lights are lit?

--- Part Two ---
You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of those lights by 1.

The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?

For example:

turn on 0,0 through 0,0 would increase the total brightness by 1.
toggle 0,0 through 999,999 would increase the total brightness by 2000000.
"""
from typing import Iterator

from utils import load_input


INPUT = load_input(__file__)


GRID_LINES = 1_000
GRID_COLUMNS = 1_000


class SantaLight:

    def __init__(self):
        self.state: bool = False

    def __repr__(self) -> str:
        return 'O' if self.state else 'X'

    def switch_on(self) -> None:
        self.state = True

    def switch_off(self) -> None:
        self.state = False

    def toggle(self) -> None:
        self.switch_off() if self.state else self.switch_on()


class Grid:
    nb_rows: int = GRID_LINES
    nb_cols: int = GRID_COLUMNS

    def __init__(self):
        self._grid: list[list[SantaLight]] = (
            [
                [SantaLight() for _ in range(Grid.nb_cols)]
                for __ in range(Grid.nb_rows)
            ]
        )

    def __repr__(self) -> str:
        text = []

        sep_every = 5
        lights_spacing = ''
        lights_separator = ' '

        for row_index, lights_row in enumerate(self._grid):

            line = [f"{row_index}  "]

            for colum_index, light in enumerate(lights_row):
                line.append(str(light))

                # Add column separator
                if (colum_index+1) % (2*sep_every) == 0:
                    line[-1] += 2*lights_separator
                elif (colum_index+1) % sep_every == 0:
                    line[-1] += lights_separator
                else:
                    line[-1] += lights_spacing

            # Add row separator
            if row_index and row_index % sep_every == 0:
                text.append('')

            line.append(f" {row_index}")

            # Merge line to text
            text.append(''.join(line))

        return '\n'.join(text)

    @property
    def lights_on_count(self):
        return sum([light.state for line in self._grid for light in line])

    def toggle_lights(self, _from, to):
        for light in self._get_lights_set(_from, to):
            light.toggle()

    def switch_off_lights(self, _from, to):
        for light in self._get_lights_set(_from, to):
            light.switch_off()

    def switch_on_lights(self, _from, to):
        for light in self._get_lights_set(_from, to):
            light.switch_on()

    def _get_lights_set(self, _from, to) -> Iterator[SantaLight]:

        start_x, start_y = (int(v) for v in _from.split(','))
        end_x, end_y = (int(v) for v in to.split(','))

        for line in self._grid[start_y:end_y+1]:
            for light in line[start_x:end_x+1]:
                yield light


class SantaBrightningLight(SantaLight):

    def __init__(self):
        SantaLight.__init__(self)
        self.state: int = 0

    def __repr__(self) -> str:
        return str(self.state)

    def switch_on(self) -> None:
        self.state += 1

    def switch_off(self) -> None:
        self.state = max([self.state-1, 0])

    def toggle(self) -> None:
        self.state += 2


class BrightningGrid(Grid):

    def __init__(self):
        Grid.__init__(self)

        self._grid: list[list[SantaBrightningLight]] = (
            [
                [SantaBrightningLight() for _ in range(BrightningGrid.nb_cols)]
                for __ in range(BrightningGrid.nb_rows)
            ]
        )


def solve(input: str, brightness: bool = False):

    grid = BrightningGrid() if brightness else Grid()

    for order in input.split('\n'):
        if not order:
            continue

        raw_order = order.split(' ')
        start = raw_order[-3]
        end = raw_order[-1]

        if order.startswith('toggle'):
            grid.toggle_lights(_from=start, to=end)
        elif order.startswith('turn on'):
            grid.switch_on_lights(_from=start, to=end)
        elif order.startswith('turn off'):
            grid.switch_off_lights(_from=start, to=end)

    # print(grid)
    return grid.lights_on_count


def solve_part1(input: str):
    return solve(input, brightness=False)


def solve_part2(input: str):
    return solve(input, brightness=True)


if __name__ == "__main__":

    print('part1:', solve_part1(INPUT))
    print('part2:', solve_part2(INPUT))
