import git
from src import *


repo = git.Repo("C:\\Users\\a0500034\\TI Drive\\TPS22996H\\FT\\eb7384")
mock_repo = git.Repo("C:\\Users\\a0500034\\Notes\\mock_prj1")

importer = Importer([repo], mock_repo)
importer.set_author('e-huuki@seg.ti.com')

importer.import_repository()