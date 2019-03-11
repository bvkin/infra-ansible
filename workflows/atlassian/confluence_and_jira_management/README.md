# Confluence and Jira Management

This workflow can be used to deploy Confluence and Jira projects.

How to run: <br />
`ansible-playbook -i workflows/atlassian/confluence_and_jira_management playbooks/ansible/tower/configure-ansible-tower.yaml`

The workflow will first create a Jira project followed by Confluence. If either fails a notification email will be sent to the specified people. If both succeed, a success notification is sent.

The workflow is intended to gather information from a running instance of the [omp-data-api](https://github.com/rht-labs/omp-data-api).