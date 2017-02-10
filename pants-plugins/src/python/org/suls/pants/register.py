from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)
import os
from pants.goal.task_registrar import TaskRegistrar as task
from pants.task.task import Task
from pants.backend.jvm.tasks.resources_task import ResourcesTask
from pants.backend.jvm.targets.jvm_app import JvmApp
from pants.util.dirutil import safe_open

def register_goals():
    class BuildProperties(ResourcesTask):    
        def find_all_relevant_resources_targets(self):
            def is_jvm_app(target):
                return isinstance(target, JvmApp)
            return self.context.targets(predicate=is_jvm_app)

        def prepare_resources(self, target, chroot):
            path = os.path.join(chroot, 'generated.properties')

            with safe_open(path, 'w') as out:
                out.writelines(
                    ['who={}\n'.format(self.context.scm.commit_id)])


    task(name='build-properties', action=BuildProperties).install('resources')
