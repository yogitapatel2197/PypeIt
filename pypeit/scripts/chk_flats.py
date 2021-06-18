"""
This script displays the flat images in an RC Ginga window.

.. include common links, assuming primary doc root is up one directory
.. include:: ../include/links.rst
"""

from pypeit.scripts import scriptbase


class ChkFlats(scriptbase.ScriptBase):

    @classmethod
    def get_parser(cls, width=None):
        parser = super().get_parser(description='Display MasterFlat images in Ginga viewer',
                                    width=width)
        parser.add_argument("--type", type=str, default='all',
                            help="Which flats to display. Must be one of: pixel, illum, all")
        parser.add_argument('master_file', type=str,
                            help='PypeIt MasterFlat file [e.g. MasterFlat_A_1_01.fits]')
        parser.add_argument('--try_old', default=False, action='store_true',
                            help='Attempt to load old datamodel versions.  A crash may ensue..')
        return parser

    @staticmethod
    def main(args):

        from pypeit import flatfield

        # Load
        flatImages = flatfield.FlatImages.from_file(args.master_file,
                                                    chk_version=(not args.try_old))
        # Show
        flatImages.show(args.type)


