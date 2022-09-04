import json
import os

# Flake8 makes big strings so hard sometimes...
README_TEMPLATE = (
    "# {addon_string} Mirror\n\n"
    "This is a mirror of {author}'s {addon_string}\n\n"
    "- [Curseforge URL](https://www.curseforge.com/wow/addons/{addon_url})\n\n"
    "----\n\n"
    "To open a ticket related to this repository, please do so on "
    "[this repository](https://github.com/curseforge-mirror/.github)"
)


def load_setup():
    with open("setup.json", "r") as file:
        return json.loads(file.read())


<<<<<<< HEAD
def rewrite_main_workflow(addon_url_name, addon_id_name):
    with open("./.github/workflows/main.yml", "r") as file:
        filedata = file.read()
        filedata = (
            filedata.replace("# ", "")
            .replace("ADDON_NAME_HERE", addon_url_name)
            .replace("ADDON_ID_HERE", addon_id_name)
        )
=======
def rewrite_main_workflow(addon_url_name):
    with open("./.github/workflows/main.yml", "r") as file:
        filedata = file.read()
        filedata = filedata.replace("# ", "").replace("ADDON_NAME_HERE", addon_url_name)
>>>>>>> 978cb49711ba3029ff17f83423d65ed10a02a0f3

    with open("./.github/workflows/main.yml", "w") as file:
        file.write(filedata)


def rewrite_readme(addon_author, addon_url_name, addon_plain_name):
    with open("README.md", "w") as file:
        file.write(
            README_TEMPLATE.format(addon_string=addon_plain_name, author=addon_author, addon_url=addon_url_name)
        )


def export_variables_to_github_env(addon_author, addon_url_name, addon_plain_name):
<<<<<<< HEAD
    env_file = os.getenv("GITHUB_ENV")
=======
    env_file = os.getenv('GITHUB_ENV')
>>>>>>> 978cb49711ba3029ff17f83423d65ed10a02a0f3

    with open(env_file, "a") as myfile:
        myfile.write(f"ADDON_AUTHOR={addon_author}\nADDON_NAME={addon_plain_name}")


if __name__ == "__main__":
    setup_data = load_setup()

    addon_author = setup_data["addon_author"]
<<<<<<< HEAD
    addon_id = setup_data["curseforge_addon_id"]
    addon_url_name = setup_data["curseforge_addon_url_name"]
    addon_plain_name = setup_data["addon_name"]

    rewrite_main_workflow(addon_url_name, addon_id)
=======
    addon_url_name = setup_data["curseforge_addon_url_name"]
    addon_plain_name = setup_data["addon_name"]

    rewrite_main_workflow(addon_url_name)
>>>>>>> 978cb49711ba3029ff17f83423d65ed10a02a0f3
    rewrite_readme(addon_author, addon_url_name, addon_plain_name)
    export_variables_to_github_env(addon_author, addon_url_name, addon_plain_name)
