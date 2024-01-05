.. readme-include-start
Diablo 2 Loot Filter Generator (d2lfg)
======================================

Diablo 2 Loot Filter Generator (d2lfg) is a small Python library
to aid in maintenance of Diablo 2 loot filter configurations.

d2lfg was built targeting `Project Diablo 2`_ and `BH`_ loot filter
configurations. Other mods using BH will probably work out of the
box. Support for other loot filters, like `D2Stats`_, should be
relatively easy to implement.

d2lfg provides access to game data, allowing for things like
iterating over all of a class's skills or discovering all items
with four or more max sockets. Game data is pulled from
`Diablo 2 txt files`_ so if you want to use this data, you'll
need to have these txt files extracted somewhere.

Requirements
------------

d2lfg requires `Python`_ 3.8 or later to run. It does not
have any runtime dependencies.

.. _Project Diablo 2: https://projectdiablo2.com/
.. _BH: https://github.com/planqi/slashdiablo-maphack
.. _D2Stats: https://github.com/planqi/slashdiablo-maphack
.. _Diablo 2 txt files: http://d2mods.info/forum/viewtopic.php?p=248164#248164
.. _Python: https://www.python.org/

.. readme-include-end
