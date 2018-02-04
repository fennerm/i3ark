"""Parsing the input yaml"""
from ruamel.yaml import YAML


class YamlParser:
    """Class for parsing the input yaml file

    Attributes
    ----------
    contents: Dict
        The contents of the input yaml file
    instructions: List[str]
        List of commands which will produce the layout
    name: str
        The name of the layout

    Parameters
    ----------
    filename: str
        The path to the yaml file

    Raises
    ------
    ParseError
        Thrown when syntax errors are encountered in the input yaml
    """

    def __init__(self, filename):
        yaml = YAML()
        with open(filename, 'r') as f:
            self.contents = yaml.load(f)
        self.instructions = []
        self.name = None

    def parse(self):
        """Parse the yaml file into a list of command line instructions"""
        self._parse_name()
        self._parse_workspace()

    def _parse_instruction(self, key, value):
        """Parse a single entry from the yaml file"""
        if key == "vsplit":
            self.instructions.append("i3-msg split v")
        elif key == "hsplit":
            self.instructions.append("i3-msg split h")
        elif key == "stacked":
            self.instructions.append("i3-msg layout stacking")
        elif key == "tabbed":
            self.instructions.append("i3-msg layout tabbed")
        else:
            # All non-recognized fields are assumed to be terminal nodes
            self._parse_node(value)

        try:
            for k, v in value.items():
                self._parse_instruction(k, v)
        except AttributeError:
            # Thrown if value is a node
            pass

    def _parse_name(self):
        """Parse the name field of the yaml"""
        try:
            self.name = self.contents["name"]
        except KeyError:
            print("Syntax error: Name field is missing")

    def _parse_node(self, commands):
        """Parse a terminal node from the yaml file"""
        command_chain = '; '.join(commands)
        instruction = '"'.join(
            ['i3-sensible-terminal -e ', command_chain, ' &'])
        self.instructions.append(instruction)
        # After a window is created, we need to focus on the parent container,
        # for further commands
        self.instructions.append("i3-msg focus parent")

    def _parse_workspace(self):
        """Parse the workspace entry from the yaml file"""
        try:
            workspace_contents = self.contents["workspace"]
            for k, v in workspace_contents.items():
                self._parse_instruction(k, v)
        except KeyError:
            print("Syntax error: Workspace field is missing")
            raise


class ParseError(SyntaxError):
    """Thrown if a syntax error is encountered in the input yaml"""
    pass
