[comment]: <> (#### CFPB Open Source Project Template Instructions)

[comment]: <> (1. Create a new project.)

[comment]: <> (2. [Copy these files into the new project]&#40;#installation&#41;)

[comment]: <> (3. Update the README, replacing the contents below as prescribed.)

[comment]: <> (4. Add any libraries, assets, or hard dependencies whose source code will be included)

[comment]: <> (   in the project's repository to the _Exceptions_ section in the [TERMS]&#40;TERMS.md&#41;.)

[comment]: <> (  - If no exceptions are needed, remove that section from TERMS.)

[comment]: <> (5. If working with an existing code base, answer the questions on the [open source checklist]&#40;opensource-checklist.md&#41;)

[comment]: <> (6. Delete these instructions and everything up to the _Project Title_ from the README.)

[comment]: <> (7. Write some great software and tell people about it.)

[comment]: <> (> Keep the README fresh! It's the first thing people see and will make the initial impression.)

[comment]: <> (## Installation)

[comment]: <> (To install all of the template files, run the following script from the root of your project's directory:)

[comment]: <> (```)

[comment]: <> (bash -c "$&#40;curl -s https://raw.githubusercontent.com/CFPB/development/master/open-source-template.sh&#41;")

[comment]: <> (```)

----

# Project Title

**Description**:  A webservice to send notification to user on completion/progress of a task
in the service or request received. This would save time for regular checking on the task progress and completion.
   - Solves frequent checking into tasks for progress and completion saving time.
   - Sends notification to user based on task completion with report. 


Other things to include:

  - **Technology stack**: Python3, Django, REST
  - **Status**:  1.0 . This is also a good place to link to the [CHANGELOG](CHANGELOG.md).

  - **Links to production or demo instances**

[comment]: <> (  - Describe what sets this apart from related-projects. Linking to another doc or page is OK if this can't be expressed in a sentence or two.)


[comment]: <> (**Screenshot**: If the software has visual components, place a screenshot after the description; e.g.,)

[comment]: <> (![]&#40;https://raw.githubusercontent.com/cfpb/open-source-project-template/master/screenshot.png&#41;)


## Dependencies

    - Python 3.9
    - Django 3.2.3


## Installation

Detailed instructions on how to install, configure, and get the project running. [INSTALL](INSTALL.md)


## Configuration

[comment]: <> (If the software is configurable, describe it in detail, either here or in other documentation to which you link.)

## Usage

```
    python manage.py runserver --settings=djangoutil.settings.dev
```

## How to test the software

[comment]: <> (If the software includes automated tests, detail how to run those tests.)

## Known issues

[comment]: <> (Document any known significant shortcomings with the software.)

## Getting help

[comment]: <> (Instruct users how to get help with this software; this might include links to an issue tracker, wiki, mailing list, etc.)

[comment]: <> (**Example**)

[comment]: <> (If you have questions, concerns, bug reports, etc, please file an issue in this repository's Issue Tracker.)

## Getting involved

[comment]: <> (This section should detail why people should get involved and describe key areas you are)

[comment]: <> (currently focusing on; e.g., trying to get feedback on features, fixing certain bugs, building)

[comment]: <> (important pieces, etc.)

General instructions on _how_ to contribute should be stated with a link to [CONTRIBUTING](CONTRIBUTING.md).


----

## Open source licensing info
1. [TERMS](TERMS.md)
2. [LICENSE](LICENSE)
3. [CFPB Source Code Policy](https://github.com/cfpb/source-code-policy/)


----

## Credits and references

1. Movies/Series where user gets notification on a device on completion/progress of task with report.

[comment]: <> (2. Related projects)

[comment]: <> (3. Books, papers, talks, or other sources that have meaningful impact or influence on this project)
