Ansible role for faketime
==================================

Installs faketime. For Ubuntu, from apt. For Red Hat from source.

[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-faketime/workflows/Molecule%20Test/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-faketime/actions?query=workflow%3A%22Molecule+Test%22)
[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-faketime/workflows/Release/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-faketime/actions?query=workflow%3A%22Molecule+Test%22)

Requirements
------------

None

Role Variables
--------------

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-------:|:--------:|
| `faketime_repo` | URL of the faketime repo to download from | string | https://github.com/wolfcw/libfaketime.git | no
| `faketime_version` | Version of faketime to download | string | v.0.9.8 | no

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - role: ansible-role-faketime
```

License
-------

[Apache License](LICENSE)
