"""Helper function to load swagger schema to Connexion."""
from collections import defaultdict
from io import StringIO
from os import path, walk
from typing import Dict, List, Optional  # pylint: disable=unused-import

import jinja2
import yaml
from yaml.constructor import ConstructorError
import yaml.resolver


def prepare_schema(specification_dirs):
    # type: (List[str]) -> dict
    """Load schema from filestructure, determined by ``specification_dirs``.

    Navigates through the specification directory and goes through all subdirectories, creating yml attributes
    according to the directory structure. The bottom level files are "headers" and top level features,
    usually all contained in headers.py.

    :param specification_dirs: root directories related to the schema
    :return: swagger schema compatible with Connexion framework
    """
    specification = StringIO()
    schema_dirs = defaultdict(lambda: defaultdict(str))  # type: dict

    for specification_dir in specification_dirs:
        dirs = walk(specification_dir)

        root_dir, _, root_files = next(dirs)
        _load_files(specification, specification_dir, root_files, is_root=True)

        for directory, _, files in dirs:
            schema_dirs[path.basename(directory)][directory] = files

    for directory_name, files_dict in schema_dirs.items():
        specification.write("{}:\n".format(directory_name))

        for directory, files in files_dict.items():
            _load_files(specification, directory, files)

    specification.seek(0)
    contents = specification.read()
    try:
        swagger_template = contents.decode()  # type: ignore
    except UnicodeDecodeError:
        swagger_template = contents.decode("utf-8", "replace")  # type: ignore
    except AttributeError:
        swagger_template = contents  # Python 3

    swagger_string = jinja2.Template(swagger_template).render()
    yaml.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_duplicates_constructor)
    return yaml.safe_load(swagger_string)  # type: ignore


def _load_files(specification, directory, files, is_root=False):
    # type: (StringIO, str, List[str], Optional[bool]) -> None
    """Load files contents to specification stream.

    :param specification: specification string stream
    :param directory: directory path
    :param files: file names
    :param is_root: is root directory flag
    """
    for file in files:
        with open("{}/{}".format(directory, file)) as infile:
            for line in infile:
                specification.write("{}{}".format("" if is_root else "  ", line))


def _no_duplicates_constructor(loader, node, deep=False):
    """Check for duplicate keys."""

    mapping: Dict = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        value = loader.construct_object(value_node, deep=deep)
        if key in mapping:
            raise ConstructorError(
                "while constructing a mapping", node.start_mark, "found duplicate key (%s)" % key, key_node.start_mark
            )
        mapping[key] = value

    return loader.construct_mapping(node, deep)
