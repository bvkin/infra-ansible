def get_remaining_items(list_a, list_b, key_a, key_b):
    for b in list_b:
        if len(list_a) == 0:
            break
        for a in list_a[:]:
            if a[key_a] == b[key_b]:
                list_a.remove(a)

    return list_a

def flatten_workflow_nodes(workflows):
    flattened_workflow, flattened_node_tree = [], []
    node_index = 1

    for workflow in workflows:
        flattened_node_tree = gen_flattened_list(workflow, node_index, 0, 'start', [])
        node_index += len(flattened_node_tree)
        flattened_workflow = flattened_workflow + flattened_node_tree

    return flattened_workflow


def gen_flattened_list(workflow, node_index, parent_index, node_type, flattened_nodes):
    child_nodes = []
    child_index = node_index + 1
    current_node = [{
     'job_name': workflow['unified_job_template']['name'],
     'type': node_type,
     'index': node_index,
     'parnet_index': parent_index
   }]


    if('success_nodes' not in workflow and 'failure_nodes' not in workflow or
        (not workflow['success_nodes'] and not workflow['failure_nodes'])):
            return current_node

    flattened_nodes = flattened_nodes + current_node

    if ('success_nodes' in workflow and len(workflow['success_nodes']) > 0):
        new_nodes = []
        for node in workflow['success_nodes']:
            new_nodes = gen_flattened_list(node, child_index, node_index, 'success', [])
            child_index += len(new_nodes)
            flattened_nodes = flattened_nodes + new_nodes

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
