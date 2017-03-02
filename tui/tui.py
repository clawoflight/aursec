#!/usr/bin/python
from datetime import datetime
from threading import Thread
import blocks
import urwid


class OuterContainer:
    palette = [
        ('body', 'black', 'light gray'),
        ('focus', 'light gray', 'dark blue', 'standout'),
        ('head', 'yellow', 'black', 'standout'),
        ('foot', 'light gray', 'black'),
        ('key', 'light cyan', 'black', 'underline'),
        ('title', 'white', 'black', 'bold'),
        ('flag', 'dark gray', 'light gray'),
        ('error', 'dark red', 'light gray'),
        ('bold', 'default,bold', 'black')
    ]

    footer_text = [
        ('title', "Keys: "),
        ('key', "Q"), "uit ", ('key', "R"), "efresh ",
    ]

    def __init__(self):
        self.screen = urwid.raw_display.Screen()
        self.footer = urwid.AttrWrap(urwid.Text(self.footer_text), 'foot')
        self.header = urwid.Text("Aursec - TUI")
        self.settings = Settings(self)
        self.col_desc = urwid.AttrWrap(
            urwid.Columns([
                ('fixed', 10, urwid.Text("Nr")),
                ('fixed', 10, urwid.Text("Hash")),
                ('fixed', 46, urwid.Text("Miner")),
                ('fixed', 25, urwid.Text("Time")),
                urwid.Text("Transactions")
            ]),
            'bold')
        self.list = items()
        self.body = urwid.BoxAdapter(urwid.ListBox(self.list), height=self.screen.get_cols_rows()[True] - 4)
        self.layout = urwid.Pile([
            self.settings,
            self.col_desc,
            self.body
        ])
        self.old_show_all = self.settings.show_all.state
        self.old_transactions = self.settings.transactions.state

        self.view = urwid.Frame(urwid.AttrWrap(urwid.Filler(self.layout, valign='top'), 'body'),
                                header=urwid.AttrWrap(self.header, 'head'),
                                footer=self.footer)
        self.blocks = blocks.Blocks()
        self.curr_block = self.blocks.get_curr_block()
        self.refresh()
        thread = Thread(target=self.blocks.run, args=(self.curr_block,))
        thread.start()

    def main(self):
        """Run the program."""

        self.loop = urwid.MainLoop(self.view, self.palette, unhandled_input=self.unhandled_input)
        self.loop.run()

    def unhandled_input(self, k):
        if k in ('q', 'Q'):
            raise urwid.ExitMainLoop()
        if k in ('r', 'R'):
            self.refresh()
        if k is 'j':
            self.body.keypress((0,), 'down')
        if k is 'k':
            self.body.keypress((0,), 'up')

    def refresh(self):
        show_all = self.settings.show_all.state
        transactions = self.settings.transactions.state
        if self.old_show_all != show_all or self.old_transactions != transactions:
            self.curr_block = self.blocks.get_curr_block()
            self.old_transactions = transactions
            self.old_show_all = show_all
            self.list.contents.clear()
        for x in self.blocks.get_older_blocks(self.curr_block, show_all, transactions):
            self.list.add(x.nr, x.hash, x.miner, x.time, x.transactions)
            self.curr_block = x.nr


class Settings(urwid.Columns):
    def __init__(self, container):
        pick = []
        self.container = container
        self.transactions = urwid.CheckBox("just transactions")
        self.show_all = urwid.CheckBox("just mine:")
        self.refresh_b = urwid.Button("refresh", on_press=self.refresh)
        string = "Settings :"
        self.text = urwid.Text(string)
        self.body = [
            self.text, self.transactions, self.show_all, self.refresh_b
        ]
        super().__init__(self.body)

    def refresh(self, button):
        self.container.refresh()


class items(urwid.SimpleListWalker):
    """docstring for item"""

    def __init__(self):
        super().__init__([])

    def add(self, nr, block_hash, miner, time, transactions):
        self.contents.append(urwid.Columns([
            ('fixed', 10, urwid.Text(str(nr))),
            ('fixed', 10, urwid.Text(str(block_hash[2:10]))),
            ('fixed', 46, urwid.Text(str(miner))),
            ('fixed', 25, urwid.Text(str(time))),
            urwid.Text(str(transactions))
        ]))


def main():
    OuterContainer().main()


if __name__ == "__main__":
    main()
