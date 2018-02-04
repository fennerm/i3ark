from pytest import fixture

from i3ark.parser import *


@fixture
def vsplit_parser():
    parser = YamlParser("test/test_cases/valid/vsplit_container.yml")
    parser.parse()
    return parser


@fixture
def hsplit_parser():
    parser = YamlParser("test/test_cases/valid/hsplit_container.yml")
    parser.parse()
    return parser


@fixture
def tabbed_parser():
    parser = YamlParser("test/test_cases/valid/tabbed_container.yml")
    parser.parse()
    return parser


@fixture
def stacked_parser():
    parser = YamlParser("test/test_cases/valid/stacked_container.yml")
    parser.parse()
    return parser


@fixture
def term():
    return "i3-sensible-terminal -e \"i3-sensible-terminal\" &"


@fixture
def parent():
    return "i3-msg focus parent"


@fixture
def subterms(term, parent):
    return [term, parent, term, parent]


@fixture
def vsplit(subterms):
    return ["i3-msg split v"] + subterms


@fixture
def hsplit(subterms):
    return ["i3-msg split h"] + subterms


@fixture
def stack(subterms):
    return ["i3-msg layout stacking"] + subterms


@fixture
def tab(subterms):
    return ["i3-msg layout tabbed"] + subterms


@fixture
def shared_instructions(vsplit, stack, tab, hsplit):
    return vsplit + hsplit + stack + tab


def test_vsplit_parsed_correctly(vsplit, shared_instructions, vsplit_parser):
    assert vsplit_parser.instructions == vsplit + shared_instructions


def test_hsplit_parsed_correctly(hsplit, shared_instructions, hsplit_parser):
    assert hsplit_parser.instructions == hsplit + shared_instructions


def test_tabbed_parsed_correctly(tab, shared_instructions, tabbed_parser):
    assert tabbed_parser.instructions == tab + shared_instructions


def test_stacked_parsed_correctly(stack, shared_instructions, stacked_parser):
    assert stacked_parser.instructions == stack + shared_instructions
