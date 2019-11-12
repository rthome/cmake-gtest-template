import os
import sys
import argparse

# Constants
WALK_ROOT = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), "template")
TEMPLATE_NAME = "foobar"

# Set up command line interface
parser = argparse.ArgumentParser("CMake-GTest-Generator")
parser.add_argument("projectname", help="name to substitute for 'foobar' in generated build")
parser.add_argument("-t", "--target", default=os.getcwd(), help="path to the generated build")

# Parse arguments
parsed_args = parser.parse_args()
projectname = parsed_args.projectname
targetpath = os.path.realpath(parsed_args.target)

# Walk template build, copy & replace
target_root_path = os.path.join(targetpath, projectname)
for root, dirs, files in os.walk(WALK_ROOT):
    fixed_relpath = os.path.relpath(root, WALK_ROOT).replace(TEMPLATE_NAME, projectname)
    current_target_dir = os.path.normpath(os.path.join(target_root_path, fixed_relpath))
    os.makedirs(current_target_dir, exist_ok=False)

    for file in files:
        template_file_path = os.path.join(root, file)
        target_file_path = os.path.join(current_target_dir, file)
        with open(template_file_path, "rb") as template_file, open(target_file_path, "wb") as target_file:
            template_content = template_file.read()
            target_content = template_content.replace(bytes(TEMPLATE_NAME, "utf-8"), bytes(projectname, "utf-8"))
            target_file.write(target_content)
