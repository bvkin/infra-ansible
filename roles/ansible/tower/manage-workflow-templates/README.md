manage-workflow-templates
====================

This role manages Workflow Templates for Ansible Tower, to be used with Ansible Tower runs.

## Requirements

A running Ansible Tower with admin permission level access.


## Role Variables

The variables used must be defined in the Ansible Inventory using the `ansible_tower.workflow_templates` list as explained below.

| Variable | Description | Required | Defaults |
|:---------|:------------|:---------|:---------|
|ansible_tower.admin_password|Admin password for the Ansible Tower install|yes||
|ansible_tower.workflow_templates.name|Name of the Job Template|yes||
|ansible_tower.workflow_templates.description|Description of the Workflow Template	|no||
|ansible_tower.workflow_templates.permissions|Permissions to run the workflow (see below)	|no||
|ansible_tower.workflow_templates.nodes|A list of job nodes to be added to a workflow (see below)	|no||
|ansible_tower.workflow_templates.extra_vars|Extra Variables to be passed at runtime|no|nothing('')|
|ansible_tower.workflow_templates.allow_simultaneous|Allows multiple instances of the workflow to run in parallel|no|true|


**_Note:_** Workflow Template configuration will **only** happen if the `ansible_tower.workflow_templates` portion of the dictionary is defined. Likewise, the installation expects this section to be "complete" if specified as it otherwise may error out.

### Permissions

The Workflow Template can be configured with a set of permissions to control who can launch the template. This includes setting either a list of users or list of teams with the proper role assignment. **Warning** It is possible to give a user access to job_templates that he/she wouldn't normally have if it is used in a workflow_template that the user has permissions for. An example of such an inventory is shown below:

```yaml
ansible_tower:
  workflow_templates:
  - name: My Workflow Template
    permissions:
      teams:
      - name: "My Team"
        role: Execute
      users:
      - name: "bob"
        role: Execute
      - name: "judy"
        role: Execute
```

## Example Inventory

```yaml
---

ansible_tower:
  admin_password: 'admin'
  workflow_templates:
  - name: "Role Workflow"
    description: "My workflow 1"
    nodes:
    - name: "Hello World"
    - name: "Foo"
    - name: "Bar"
    permissions:
      teams:
      - name: team1
        role: Execute
      users:
      - name: user1
        role: Execute

```

## Example Playbook

```yaml
---

- hosts: tower
  roles:
  - role: manage-workflow-templates
```


License
-------

Apache License 2.0


Author Information
------------------

Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
