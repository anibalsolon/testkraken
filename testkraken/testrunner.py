"""Running workflows and regression tests for all projects in chosen dictionary"""

from testkraken.workflowregtest import WorkflowRegtest
import os, pdb


def runner(workflow_dir):
    print("Workflow Name: {}".format(os.path.basename(workflow_dir)))
    wf = WorkflowRegtest(workflow_dir)
    wf.run()
    wf.merge_outputs()
    wf.dashboard_workflow()
