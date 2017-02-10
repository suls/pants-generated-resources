from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)

from pants.goal.task_registrar import TaskRegistrar as task
from pants.task.task import Task


def register_goals():
    class BuildProperties(Task):
        def execute(self):
            pass

    task(name='build-properties', action=BuildProperties).install('resources')
