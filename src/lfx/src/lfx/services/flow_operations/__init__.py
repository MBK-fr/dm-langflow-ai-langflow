"""Flow operation vocabulary and pure apply engine.

Operations describe granular edits to ``flow.data``: nodes and edges added,
updated field by field, or deleted, and top-level metadata changes. The engine
has no transport or database dependencies, so the same rules apply wherever an
operation comes from.
"""

from lfx.services.flow_operations.apply import (
    FlowOperationsApplyResult,
    GraphState,
    apply_flow_operations,
    build_graph_state,
    finalize_graph,
)
from lfx.services.flow_operations.canonical import (
    canonical_graph,
    canonical_graph_json,
    canonical_json,
    graph_hash,
    graphs_equal,
    json_type,
)
from lfx.services.flow_operations.diff import DerivedFlowOperations, derive_flow_operations, diff_flow_data
from lfx.services.flow_operations.exceptions import (
    FlowDataValidationError,
    FlowOperationError,
    FlowOperationReplayError,
    FlowOperationValidationError,
)
from lfx.services.flow_operations.ops import (
    AddEdgesOp,
    AddNodesOp,
    DeleteEdgesOp,
    DeleteNodeFieldUpdate,
    DeleteNodesOp,
    FlowOperation,
    NodeFieldPath,
    NodeFieldPathSegment,
    SetNodeFieldUpdate,
    UpdateMetadataOp,
    UpdateNodeEntry,
    UpdateNodesOp,
    deduplicate_delete_ids,
    dump_flow_operation,
    normalize_requested_ops,
    parse_flow_operation,
    parse_flow_operations,
)
from lfx.services.flow_operations.python import PythonFlowOperationService
from lfx.services.flow_operations.repair import REPAIRS, GraphFix, RepairResult, repair_flow_data
from lfx.services.flow_operations.service import BaseFlowOperationService
from lfx.services.flow_operations.validation import (
    GraphViolation,
    GraphViolationCode,
    find_graph_violations,
    validate_flow_data,
)

__all__ = [
    "REPAIRS",
    "AddEdgesOp",
    "AddNodesOp",
    "BaseFlowOperationService",
    "DeleteEdgesOp",
    "DeleteNodeFieldUpdate",
    "DeleteNodesOp",
    "DerivedFlowOperations",
    "FlowDataValidationError",
    "FlowOperation",
    "FlowOperationError",
    "FlowOperationReplayError",
    "FlowOperationValidationError",
    "FlowOperationsApplyResult",
    "GraphFix",
    "GraphState",
    "GraphViolation",
    "GraphViolationCode",
    "NodeFieldPath",
    "NodeFieldPathSegment",
    "PythonFlowOperationService",
    "RepairResult",
    "SetNodeFieldUpdate",
    "UpdateMetadataOp",
    "UpdateNodeEntry",
    "UpdateNodesOp",
    "apply_flow_operations",
    "build_graph_state",
    "canonical_graph",
    "canonical_graph_json",
    "canonical_json",
    "deduplicate_delete_ids",
    "derive_flow_operations",
    "diff_flow_data",
    "dump_flow_operation",
    "finalize_graph",
    "find_graph_violations",
    "graph_hash",
    "graphs_equal",
    "json_type",
    "normalize_requested_ops",
    "parse_flow_operation",
    "parse_flow_operations",
    "repair_flow_data",
    "validate_flow_data",
]
