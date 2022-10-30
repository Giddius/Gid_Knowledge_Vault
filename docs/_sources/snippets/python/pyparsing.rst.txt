PyParsing
============



Parse Python-like function signature
---------------------------------------


.. admonition:: required packages

   * `PyParsing <https://pypi.org/project/pyparsing/>`_



.. code:: python

   import pyparsing as ppa
   from pyparsing import common as ppc

   parenthesis_open = ppa.Literal("(").suppress()
   parenthesis_close = ppa.Literal(")").suppress()

   equal_sign = ppa.Literal("=").suppress()
   comma = ppa.Literal(",").suppress()

   pos_argument = ppc.number | ppa.Word(ppa.alphanums + "_")

   kw_argument = ppa.Group(ppc.identifier + equal_sign + pos_argument.copy())

   arguments = (ppa.ZeroOrMore(pos_argument + ppa.Opt(comma), stop_on=kw_argument)("pos_arguments")
                 + ppa.Dict(ppa.ZeroOrMore(kw_argument + ppa.Opt(comma)), asdict=True).set_parse_action(lambda x: x[0])("kw_arguments"))

   name = ppa.Word(ppa.alphas + "_", ppa.alphanums + '_')

   sub_arguments = parenthesis_open + arguments + parenthesis_close

   grammar = name("name") + ppa.Opt(sub_arguments)