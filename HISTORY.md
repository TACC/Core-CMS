# Codebase History

## 2020.02.03

### Added

- CSS processing (minimal)
- NPM `package.json` file

### Changed

- Move location of source CSS files.


## 2020.01.16

### Background

The initial cms-template01-setup codebase was intended to be a stopgap solution for sites that required only static content rather than a complete portal infrastructure. However, due to the timetables for transitioning the full portals into a parallel architecture (for the CMS portions) several sites have been deployed using this stop gap codebase.

After some discussion between developers, it was decided that the best approach is to create unique forks of the cms-template01-setup codebase for each stand alone site that is deployed. This will make maintenance far easier as well as allow more diversity between the final implementation of each site. 

The following forks will be created from the root codebase for each site deployed:

- Upstream Master Codebase: cms-template01-setup 
    - https://gitlab.tacc.utexas.edu/jgentle/cms-template01-setup
- Fork: lccf-tacc 
    - pending)
- Fork: texascale-org 
    - pending
- Fork: tapis-project-org
    - pending
- FORK: fronterra-tacc
    - pending
    - This is a special case where this version of the CMS will be the one leveraged by the CEP v2 Portals (the new React based Fronterra portal is PoC) going forward.

### Caveats

After forking the root codebase, we will need to update each fork's secret settings, settings and template files. Most of this should be purging the content from the other sites that are no longer relevant to the fork.

Once each fork has been cleaned up and tested for valid content retention, the site should be redeployed on the VM using the correct repo. It is possible that some of the conf files may need to be tweaked, but the configs are identical generally speaking (certs aside).

Workflows for CMS Stand Alone Sites need to be updated to reflect the new approach. 
- This might require coordinating with Colin to change the base image snapshot that is being used...
- Or just clear documentation on how to update the repo on the VM and pull the new fork.

