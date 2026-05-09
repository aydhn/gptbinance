from datetime import datetime, timezone, timedelta
from app.workflow_plane.registry import registry
from app.workflow_plane.runs import RunManager
from app.workflow_plane.reruns import RerunManager
from app.workflow_plane.reporting import WorkflowReporter
from app.workflow_plane.models import RunWindow
from app.workflow_plane.enums import TriggerClass, WindowClass
from app.workflow_plane.exceptions import DuplicateRunError

def run_workflow_cli(args):
    run_mgr = RunManager()
    rerun_mgr = RerunManager(run_mgr)
    reporter = WorkflowReporter(run_mgr)

    now = datetime.now(timezone.utc)
    win = RunWindow(window_id="win-1", start_time=now - timedelta(minutes=5), end_time=now, as_of_cut=now, window_class=WindowClass.ROLLING)
    run1 = run_mgr.initiate_run("market_data_refresh_workflow", win, TriggerClass.SCHEDULE)

    try:
        run_mgr.initiate_run("market_data_refresh_workflow", win, TriggerClass.SCHEDULE)
    except DuplicateRunError:
        pass

    rerun_mgr.execute_rerun(run1.run_id, "Data missing, required full fetch", approver="operator-1")

    if getattr(args, "show_workflow_registry", False):
        reporter.print_registry()
    elif getattr(args, "show_workflow_runs", False):
        reporter.print_runs()
    elif getattr(args, "show_run_windows", False):
        print("=== RUN WINDOWS SEMANTICS ===")
        print("- as_of_cut: Logical time of the workflow")
        print("- available_data_cut: Hard cutoff for ingesting new data")
        print("- partial window caveats: Enforced through is_partial flag")
    elif getattr(args, "show_workflow_dependencies", False):
        print("=== DEPENDENCY GRAPH ===")
        print("model_inference -> requires -> feature_refresh")
        print("allocation_cycle -> requires -> model_inference, risk_refresh")
        print("execution_cycle -> requires -> allocation_cycle")
    elif getattr(args, "show_workflow_triggers", False):
        print("=== WORKFLOW TRIGGERS ===")
        print("- MANUAL: Triggered by human operator")
        print("- SCHEDULE: Triggered by temporal boundary")
        print("- DATA_ARRIVAL: Triggered by upstream data presence")
    elif getattr(args, "show_workflow_gates", False):
        print("=== WORKFLOW GATES ===")
        print("- DATA_TRUST: Validates data feed health")
        print("- READINESS: Verifies board approval before critical action")
    else:
        print("Platform Core Workflow Plane initialized. Use --show-* commands to inspect.")
