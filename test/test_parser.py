from pytest import (
    fixture,
    mark,
)

from i3ark.parser import *


@fixture
def vsplit_parser():
    parser = YamlParser("test/test_cases/valid/vsplit_container.yml")
    parser.parse()
    return parser


@fixture
def term():
    return "i3-sensible-terminal -e \"i3-sensible-terminal\" &"


class TestParsing():
    @fixture
    def vsplit(self):
        return "i3-msg split v"

    @fixture
    def hsplit(self):
        return "i3-msg split h"

    @fixture
    def stack(self):
        return "i3-msg layout stacking"

    @fixture
    def tab(self):
        return "i3-msg layout tabbed"

    @fixture
    def parent(self):
        return "i3-msg focus parent"

    def test_vsplit_parsed_correctly(self, vsplit, hsplit, parent, stack,
                                     tab, vsplit_parser, term):
        assert vsplit_parser.instructions == [
            vsplit, term, parent, term, parent, hsplit, term, parent, term,
            parent, stack, term, parent, term, parent, tab, term, parent, term,
            parent]
