#!/usr/bin/env python3

import argparse
import os
import json
import sys
import yaml
from jinja2 import Environment, FileSystemLoader

def open_yaml(yaml_file):
    with open(yaml_file, 'r') as file:
        try:
            yaml_dict = yaml.safe_load(file)
            return yaml_dict
        except yaml.YAMLError as e:
            print(e)


def render_html(yaml_dict, input_jinja, output_path):
    # TODO: Remove this temporary code
    root = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(root, 'templates')
    env = Environment( loader = FileSystemLoader(templates_dir) )
    template = env.get_template('basic.html')


    if not os.path.exists(output_path):
        os.makedirs(output_path)

    with open(output_path, 'w+') as output_file:
        output_file.write(template.render(
            title = yaml_dict['info']['title'],
            paths = yaml_dict['paths']
        ))


def main():
    parser = argparse.ArgumentParser()
    # Required
    parser.add_argument('spec', help = 'Input OpenAPI specification file in either yaml or json')
    parser.add_argument('template', help = 'Input Jinja2 template path')
    # Optional
    parser.add_argument('-o', '--output', help = 'Output path to store generated files')
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    # Parse Args
    input_spec = args.spec
    input_template = args.template

    output_path = 'output/index.html'
    if args.output:
        output_path = args.output


    if input_spec[-4:] == 'yaml' or input_spec[-3:] == 'yml':
        yaml_dict = open_yaml(input_spec)
    elif input_spec[-4:] == 'json':
        yaml_dict = open_json(input_spec)

    # Render and Output to file
    render_html(yaml_dict, input_template, output_path)


if __name__ == '__main__':
    main()