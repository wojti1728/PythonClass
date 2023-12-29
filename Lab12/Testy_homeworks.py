
def strike(text):
    """ Renders string with strike-through characters through it.

        `strike('hello world')` -> '̶h̶e̶l̶l̶o̶ ̶w̶o̶r̶l̶d'

        Notes
        -----
        \u0336 is a special strike-through unicode character; it
        is not unique to Python."""
    return ''.join('\u0336{}'.format(c) for c in text)

class ShoppingList:
    def __init__(self, items):
        self._needed = set(items)
        self._purchased = set()

    def __repr__(self):
        """ Returns formatted shopping list as a string with
                    purchased items being crossed out.

                    Returns
                    -------
                    str"""
        if self._needed or self._purchased:
            remaining_items = [str(i) for i in self._needed]
            purchased_items = [strike(str(i)) for i in self._purchased]
            return "* " + "\n".join(remaining_items + purchased_items)

    def add_new_items(self, items):
        self._needed.update(items)

    def mark_purchased_items(self, items):
        self._purchased.update(set(items) & self._needed)
        self._needed.difference_update(self._purchased)

l = ShoppingList(["grapes", "beets", "apples", "milk", "melon", "coffee"])
print(l.__repr__())
print(l.mark_purchased_items(["grapes", "beets", "milk"]))
print(l)


