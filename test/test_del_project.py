import random
import time
from model.project import Project


def test_delete_project(app, db):
    old_projects = db.get_projects()
    project = random.choice(old_projects)
    app.project.delete_project(project)
    new_projects = app.soap.get_user_accessible_projects()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)