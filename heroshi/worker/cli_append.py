from optparse import OptionParser

import heroshi
from heroshi import api


def parse_params():
    usage_info = "Usage: %prog [OPTION...] ITEM-URL..."
    version_info = "Heroshi/%s" % heroshi.__version__
    opt_parser = OptionParser(usage_info, version=version_info)
    opt_parser.set_defaults(verbose=False, quiet=False)
    opt_parser.add_option('-q', '--quiet', action="store_true", help="Be quiet, don't generate any output")
    opt_parser.add_option('-v', '--verbose', action="store_true", help="Be verbose, print detailed information")
    (options, args) = opt_parser.parse_args()
    return options, args

def main():
    _options, args = parse_params()

    item = {'url': None, 'links': args}
    api.report_result(item)


if __name__ == '__main__':
    main()
