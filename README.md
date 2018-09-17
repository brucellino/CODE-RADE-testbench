# CODE-RADE testbench

[![Build Status](https://travis-ci.org/AAROC/CODE-RADE-testbench.svg?branch=master)](https://travis-ci.org/AAROC/CODE-RADE-testbench) [![Docker Repository on Quay](https://quay.io/repository/aaroc/code-rade-testbench/status "Docker Repository on Quay")](https://quay.io/repository/aaroc/code-rade-testbench) 
<!-- A brief description of the role goes here. -->
This is a container-enabled role to create the testbench image used in running unit tests of CODE-RADE repo code.
This image is used during the first part of the testing pipeline, to run unit and linting tests on the code in the repo under question.
It contains the following runtime environments:

  - python:
    - versions 2.7, 3.6 in virtualenv
    - packages:
      - pytest
      - mock
      - requests
  - ruby: 2.0.0
    - gems:
      - bundler
      - rspec

Also included are the following testing tools:

  - ShellCheck

See [defaults](detaults/main.yml) for more information.

## Requirements

<!--
Any pre-requisites that may not be covered by Ansible itself or the role should be
mentioned here.
For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.
-->
No specific requirements.

## Role Variables

<!--
A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.
-->
Variables are described in `defaults.yml`.
They refer to the packages necessary to be be present on the image.


## Dependencies

None

## Example Playbook

<!--
Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too.
Be sure to write the dependencies explicitly.
-->

```yaml
    - hosts: CI-initial-stage-servers
      roles:
         - { role: AAROC.CODE-RADE-testbench }
```

## License

Apache-2.0

## Author Information

<!--
Add the relevant contributors
-->
See AUTHORS.md