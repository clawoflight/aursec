#!/usr/bin/python
from datetime import datetime

import urwid


class OuterContainer:
    palette = [
        ('body', 'black', 'light gray'),
        ('focus', 'light gray', 'dark blue', 'standout'),
        ('head', 'yellow', 'black', 'standout'),
        ('foot', 'light gray', 'black'),
        ('key', 'light cyan', 'black','underline'),
        ('title', 'white', 'black', 'bold'),
        ('flag', 'dark gray', 'light gray'),
        ('error', 'dark red', 'light gray'),
        ('bold', 'default,bold', 'black')
        ]
 
    footer_text = [
        ('title', "Keys: "),
         " QUIT ", ('key', "Q"),
        ]



    def __init__(self):
        self.screen = urwid.raw_display.Screen()
        self.footer = urwid.AttrWrap( urwid.Text( self.footer_text), 'foot')
        self.header = urwid.Text("Aursec - TUI")
        self.settings = Settings(self)
        #delete this after body implementation
        self.test = 0
        self.col_desc = urwid.AttrWrap(urwid.Columns([urwid.Text("Nr"),urwid.Text("Miner"),urwid.Text("Sender"),urwid.Text("Transaction")]),'bold')
        # TODO ListBox
        # seperate name from List 
        # create Object which covers all 4 lines
        self.list = items()
        self.body = urwid.BoxAdapter(urwid.ListBox(self.list),height=self.screen.get_cols_rows()[True]-4)
        self.layout = urwid.Pile([
            self.settings,
            self.col_desc,
            self.body
            ])

        self.view = urwid.Frame(urwid.AttrWrap( urwid.Filler(self.layout , valign='top'), 'body'),
                                header=urwid.AttrWrap(self.header, 'head'),
                                footer=self.footer)



    def main(self):
        """Run the program."""

        self.loop = urwid.MainLoop(self.view, self.palette, unhandled_input=self.unhandled_input)
        self.loop.run()

    def unhandled_input(self, k):
        if k in ('q','Q'):
            raise urwid.ExitMainLoop()

    def refresh(self):
        self.test += 1
        self.list.add(self.test,self.test,self.test,self.test)



class Settings(urwid.Columns):
    def __init__(self,container):
        pick = []
        self.container = container
        self.blocks = urwid.RadioButton(pick, "blocks", state="first True",on_state_change=self.refresh)
        self.transactions = urwid.RadioButton(pick, "transactions",on_state_change=self.refresh)
        self.showAll = urwid.CheckBox("show just mine:",on_state_change=self.refresh)
        string = "Settings :"
        self.text = urwid.Text(string)
        self.body = [
            self.text, self.blocks, self.transactions, self.showAll
        ]
        super().__init__(self.body)

    def refresh(self,button,state):
        self.container.refresh()

class items(urwid.SimpleListWalker):
    """docstring for item"""
    def __init__(self):
        super().__init__([])

    def add(self,nr,miner,sender,transaction):
        self.contents.append(urwid.Columns([
            urwid.Text(str(nr)),
            urwid.Text(str(miner)),
            urwid.Text(str(sender)),
            urwid.Text(str(transaction)),
            ]))

        

def main():
    OuterContainer().main()


if __name__=="__main__":
    main()

