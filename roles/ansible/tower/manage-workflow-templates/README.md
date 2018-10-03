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


**_Note:_** Job Template configuration will **only** happen if the `ansible_tower.workflow_templates` portion of the dictionary is defined. Likewise, the installation expects this section to be "complete" if specified as it otherwise may error out.

### Permissions


```yaml
ansible_tower:
  workflow_templates:
```

## Example Inventory

```yaml
---

ansible_tower:
  admin_password: 'admin'
  workflow_templates:
  - name: "Role Workflow"
    description: "A workflow created from an ansible role"
    nodes:
    - name: "Hello World!"
    - name: "Foo"
    - name: "Bar"

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
