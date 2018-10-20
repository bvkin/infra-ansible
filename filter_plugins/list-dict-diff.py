def get_remaining_items(list_a, list_b, key_a, key_b):
    for b in list_b:
        if len(list_a) == 0:
            break
        for a in list_a[:]:
            if a[key_a] == b[key_b]:
                list_a.remove(a)

    return list_a

# For manage-workflow-templates role
# Takes a workflow defined in a dictionary and processes it into a list
def flatten_workflow_nodes(workflows):
    flattened_workflow, flattened_start_tree = [], []
    current_node_index = 1

    # Processes each node beginning at start and all their success/failure branches
    for workflow in workflows:
        flattened_start_tree = gen_flattened_list(workflow, current_node_index, 0, 'start', [])
        current_node_index += len(flattened_start_tree)
        flattened_workflow = flattened_workflow + flattened_start_tree

    return flattened_workflow

# Helper function for flatten_workflow_nodes
# Recursively flattens a workflow dictionary with one node at start
def gen_flattened_list(workflow, node_index, parent_index, node_type, flattened_nodes):
    current_node = [{
     'job_name': workflow['unified_job_template']['name'],
     'type': node_type,
     'index': node_index,
     'parent_index': parent_index
   }]

   # Return node it has no children
    if('success_nodes' not in workflow and 'failure_nodes' not in workflow or
        (not workflow['success_nodes'] and not workflow['failure_nodes'])):
            return current_node

    # Add current node to the list of processed nodes
    flattened_nodes = flattened_nodes + current_node
    child_index = node_index + 1

    # Recursively process all of the current nodes success children
    if ('success_nodes' in workflow and len(workflow['success_nodes']) > 0):
        new_nodes = []
        for node in workflow['success_nodes']:
            new_nodes = gen_flattened_list(node, child_index, node_index, 'success', [])
            child_index += len(new_nodes)
            flattened_nodes = flattened_nodes + new_nodes

    # Recursively process all of the current nodes failure children
    if ('failure_nodes' in workflow and len(workflow['failure_nodes']) > 0):
        new_nodes = []
        for node in workflow['failure_nodes']:
            new_nodes = gen_flattened_list(node, child_index, node_index, 'failure', [])
            child_index += len(new_nodes)
            flattened_nodes = flattened_nodes + new_nodes

    return flattened_nodes


class FilterModule(object):
    ''' A set of filters to support diff'ing lists of dicts'''
    def filters(self):
        return {
            'get_remaining_items': get_remaining_items,
            'flatten_workflow_nodes': flatten_workflow_nodes
        }
