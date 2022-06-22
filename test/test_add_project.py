import random
import time
from model.project import Project


def test_create_project(app, db):
    old_projects = db.get_projects()
    project = Project(name='new  project')
    app.project.create_new_project(project)
    time.sleep(1)
    new_projects = app.soap.get_user_accessible_projects()
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
