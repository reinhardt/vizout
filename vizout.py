import os
from ConfigParser import SafeConfigParser
from sys import argv
from sys import stderr


def extract_extends(filename, parentnode=None):
    nodename = filename.replace('.', '_').replace('/', '_').replace('-', '_')
    directory = os.path.dirname(filename)
    graph = ''
    graph += ' ' * 4
    graph += nodename + ' [label="' + filename + '"];\n'
    if parentnode:
        graph += ' ' * 4
        graph += parentnode + ' -> ' + nodename + ';\n'

    if not os.path.exists(filename):
        stderr.write(filename + ' not found\n')
    else:
        cfg = SafeConfigParser()
        cfg.read(filename)
        if not cfg.has_section('buildout'):
            stderr.write('Section [buildout] not found in ' + filename + '\n')
        else:
            if cfg.has_option('buildout', 'extends'):
                extends = cfg.get('buildout', 'extends')
                if not isinstance(extends, list):
                    if ' ' in extends:
                        extends = extends.split(' ')
                    elif '\n' in extends:
                        extends = extends.split('\n')
                    else:
                        extends = [extends]
                import ipdb; ipdb.set_trace()
                for extends_file in extends:
                    if extends_file:
                        graph += extract_extends(
                            os.path.join(directory, extends_file),
                            parentnode=nodename)
    return graph


if __name__ == '__main__':
    filename = 'buildout.cfg'
    if len(argv) > 1:
        filename = argv[1]
    graph = "digraph extends {\n"

    graph += extract_extends(filename)

    graph += '}\n'
    print(graph)
