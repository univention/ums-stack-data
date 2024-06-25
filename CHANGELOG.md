# Changelog

## [0.51.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.50.0...v0.51.0) (2024-06-25)


### Features

* add support for ldapSystemUsers, to allow customer defined ldapSearchUsers that do not override default users created by the nubus umbrella ([8ee7c4e](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/8ee7c4eb991aa725b3c6597c7dbb3a4bd8b607b8))

## [0.50.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.49.2...v0.50.0) (2024-06-25)


### Features

* remove complexity check for user creation ([372919a](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/372919aa1679ee8ba1821a547ce09ead893df511))

## [0.49.2](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.49.1...v0.49.2) (2024-05-24)


### Bug Fixes

* **ci:** use fixed common-ci/helm package to not update dependency waiter tags ([152af55](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/152af55d2e7b7e8f3abf260c430cab4acaea25e4))

## [0.49.1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.49.0...v0.49.1) (2024-05-24)


### Bug Fixes

* remove SKIP_UPDATE_HELM_VALUES ([5e5c4d4](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/5e5c4d4853b4c57ba767eadb4226e721fd0dfe64))

## [0.49.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.48.0...v0.49.0) (2024-05-23)


### Features

* push to harbor ([2a64a75](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/2a64a75e18c8c1b690f53ac08d69d00b14376edb))

## [0.48.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.47.0...v0.48.0) (2024-05-20)


### Features

* further changes to support the refactored umbrella values in a nubus deployment ([626e1f8](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/626e1f82a7178300e57332e36b117626b651b100))

## [0.47.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.46.0...v0.47.0) (2024-04-25)


### Features

* changes to support separation of primary and secondary ldap configuration ([c7a94f8](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/c7a94f8a1f09852d851902d0631049d4b6400386))
* changes to support the refactored umbrella values in a nubus deployment ([c5eeb0f](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/c5eeb0fd46632c0f0f14b14577093c6f64d319f1))
* changes to support the refactored umbrella values in a nubus deployment (stack-data-swp) ([b229e65](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/b229e650e6cf3922c143786c557af63160792cca))


### Bug Fixes

* compatibility fixes, cleanup ([9ff38a3](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/9ff38a3a036d1182cbee7b04850efe56fc7790f4))
* drop default value for memcache username (required for opendesk) ([a91b061](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/a91b061eebbfedb29588cb5cdf9f1ef208c808a8))
* set umcSamlSchemes default to https ([b31e6bc](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/b31e6bcb04619c6fbfdcf257d22efe48b927e60c))

## [0.46.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.45.2...v0.46.0) (2024-04-24)


### Features

* Avoid calls to "apt-get update" to use packages from the base image ([98a8433](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/98a84333984e2b7455821e60eb26afd506490084))
* Pin version of base image to "0.10.0" ([abdf650](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/abdf650be84f24b3ef7bd5846ec000f59a09cf3b))

## [0.45.2](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.45.1...v0.45.2) (2024-03-25)


### Bug Fixes

* **ci:** update common-ci from v1.16.2 to v1.24.5 ([3318eca](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/3318eca2e55cd2fd45114713bb53a5d747354f6e))

## [0.45.1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.45.0...v0.45.1) (2024-03-20)


### Bug Fixes

* add missing configuration options for umc/self-service ([5ced5e3](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/5ced5e3ccb0a6220b9eafd7f694e05a1a6d7cb9f))

## [0.45.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.44.2...v0.45.0) (2024-03-14)


### Features

* Add "directory/manager/starttls" into stack-data-swp ([fbb2347](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/fbb2347e82fb76602e1ee314288d58b7dcb5cd8f))
* Add UCR based configuration for UMC Self-Service ([2b5e203](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/2b5e203219e3d478e4957a6519695af1061d1362))

## [0.44.2](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.44.1...v0.44.2) (2024-03-12)


### Bug Fixes

* restore upstream ucr compatibility ([9dad395](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/9dad3959d7864c7c6bccb4c9e95264cbcaeca6a6))

## [0.44.1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.44.0...v0.44.1) (2024-03-08)


### Bug Fixes

* ucr variable name for uldap starttls configuration ([ce77164](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/ce77164e9c9a57ac390befe58ef31797c763191f))

## [0.44.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.43.2...v0.44.0) (2024-02-13)


### Features

* **fileshare:** Add admin flag and group ([d28ec64](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/d28ec64862eb9a6821b1698f634030df56f48716))

## [0.43.2](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.43.1...v0.43.2) (2024-01-23)


### Bug Fixes

* **stack-data-ums:** Add "initialPasswordSysIdpUser" as required variable ([07ddfdf](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/07ddfdfa282704835f123f5e691be0c53d8c265a))

## [0.43.1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.43.0...v0.43.1) (2024-01-22)


### Bug Fixes

* Comment out failing operations if "installUmcPolicies" is true ([d17b3a4](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/d17b3a420b9cf3e14530947b00a6cd0a78bcb03c))
* Handling of self-service related policies if "installUmcPolicies" is true ([1f97637](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/1f97637dbcc95a4a83632e1f9e837b5b44120fdc))

## [0.43.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.42.0...v0.43.0) (2024-01-18)


### Features

* **ci:** add debian update check jobs for scheduled pipeline ([84cd0ce](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/84cd0ce1006539099bbee93423701d99c9d0ace7))


### Bug Fixes

* **deps:** add renovate.json ([84e67a2](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/84e67a28b446b31699e46035456737197eddd0e1))

## [0.42.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.41.8...v0.42.0) (2024-01-12)


### Features

* **stack-data-swp:** Configure password policies ([170797a](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/170797abc2b13a526c78867cdf85ea01fd324d79))

## [0.41.8](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.41.7...v0.41.8) (2024-01-10)


### Bug Fixes

* Reenable oxContext in UMC as there is a bug that invisible items cannot be set by a user template ([16e42c5](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/16e42c5dd0b470a6d11e49b0651b20d40f51ba38))

## [0.41.7](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.41.6...v0.41.7) (2024-01-10)


### Bug Fixes

* Add oxContext to user template as it is removed from UI ([08e9594](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/08e959441ee9a607ddf6d596a67effa8a13435a2))

## [0.41.6](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.41.5...v0.41.6) (2024-01-08)


### Bug Fixes

* System info links ([4374166](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/43741664f8fff1ea39ae2986272047026c714789))
* Typos in portal entries ([4ab3c62](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/4ab3c6267578ebf97411bd4240e74c1bede3b21f))

## [0.41.5](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.41.4...v0.41.5) (2024-01-05)


### Bug Fixes

* Configure isOxGroup and oxContext properly ([e73e949](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/e73e949bbcd3487083e1407996e8b0d4ce5f5f2e))

## [0.41.4](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.41.3...v0.41.4) (2024-01-04)


### Bug Fixes

* Update Nextcloud URLs for new container setup ([d1c03d2](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/d1c03d2f4a7f2f1d672498f48b6871ca6034bc24))

## [0.41.3](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.41.2...v0.41.3) (2024-01-04)


### Bug Fixes

* **stack-data-ums:** Correct the checksum annotations in the Job object ([3d8e146](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/3d8e146dd814dd97f2a3746cc5474cb2c63c92b9))

## [0.41.2](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.41.1...v0.41.2) (2023-12-29)


### Bug Fixes

* **stack-data-swp:** Add system info scope ([1872b6b](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/1872b6bab465b6e1387a13154e50c428f3569e74))

## [0.41.1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.41.0...v0.41.1) (2023-12-28)


### Bug Fixes

* **licensing/ci:** add spdx license headers, add license header checking pre-commit ([b7ab26e](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/b7ab26ed5a5987c83ad2f498c57add87e80912e9))

## [0.41.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.40.1...v0.41.0) (2023-12-27)


### Features

* **data-loader:** Add upsert action ([e18e8cc](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/e18e8cc40014eace160e18e54b4a8a39ce8cd1ed))

## [0.40.1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.40.0...v0.40.1) (2023-12-21)


### Bug Fixes

* **docker:** update ucs-base from 5.0-5 to 5.0-6 ([c958d14](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/c958d14081a47d819e2bf6c8dc32b1f13aa1a6b2))

## [0.40.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.39.6...v0.40.0) (2023-12-20)


### Features

* **ums:** guardian role extended attribute ([f5f77bd](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/f5f77bdc5f7fe9f5517caa452aa8e03105b48fa5)), closes [univention/customers/dataport/team-souvap#342](https://git.knut.univention.de/univention/customers/dataport/team-souvap/issues/342)

## [0.39.6](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.39.5...v0.39.6) (2023-12-20)


### Bug Fixes

* **customcss:** add styles for buttons on password renewal screen ([6a14d11](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/6a14d11a13a9b55454d030faff44e750e5dd271b))

## [0.39.5](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.39.4...v0.39.5) (2023-12-18)


### Bug Fixes

* **ci:** add Helm chart signing and publishing to souvap via OCI, common-ci 1.12.x ([3405d8c](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/3405d8cae013d08653b55712c8074d762f343c0e))

## [0.39.4](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.39.3...v0.39.4) (2023-12-15)


### Bug Fixes

* Correct various opendesk adaptions ([c18213a](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/c18213ac18ed05120514377e20ba8adebb830578))

## [0.39.3](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.39.2...v0.39.3) (2023-12-12)


### Bug Fixes

* Set former First and Lastname for default users ([4f81144](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/4f81144bbffc84689c98d8c88f6b017a51fc2ce9))
* Set proper OX access profile for default user ([fc9fcc3](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/fc9fcc347e62521a9d8c1c51286c34418f589451))

## [0.39.2](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.39.1...v0.39.2) (2023-12-11)


### Bug Fixes

* Configuration finetuning for openDesk ([96d5ba5](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/96d5ba5a3ba885a1ad1258a5d3fc222cb85e44c5))

## [0.39.1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.39.0...v0.39.1) (2023-12-11)


### Bug Fixes

* **ci:** reference common-ci v1.11.x to push sbom and signature to souvap ([6c6d8c2](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/6c6d8c21b14c27d2730ff759c81baf8d193293c4))

## [0.39.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.38.5...v0.39.0) (2023-12-08)


### Features

* **data-loader:** Support object delete ([7fe3e54](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/7fe3e54add85b7ab988844b3bd0c0644beca3f8c))


### Bug Fixes

* **stack-data-swp:** remove selfservice registration template ([f034b27](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/f034b27fbe4e33ce75fe9d103852f2c2fd3ec53f))

## [0.38.5](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.38.4...v0.38.5) (2023-12-08)


### Bug Fixes

* Add oxContext to openDesk user template ([86d24e8](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/86d24e8ba10ffcfa4009ffb8ebdfe48012f818b8))

## [0.38.4](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.38.3...v0.38.4) (2023-12-07)


### Bug Fixes

* Keycloak Login custom.css ([91d41b0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/91d41b090893788486f4972a6cecbeaa1f47b8c2))

## [0.38.3](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.38.2...v0.38.3) (2023-12-06)


### Bug Fixes

* **stack-data-ums:** don't add 'self registered users' to the 'default containers' ([46e4c6b](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/46e4c6be0a8e54369a37c012a6dd33b4c53953a9))
* **stack-data:** resolve circular dependency between ums and swp ([f9ba5d2](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/f9ba5d25c416a2943bf3a537e965168213324827))

## [0.38.2](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.38.1...v0.38.2) (2023-12-06)


### Bug Fixes

* add required openDesk branding details for Univention Keycloak ([a6b41b0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/a6b41b0eaf8073b8b3fb35ebc25fc397f4ac7a07))

## [0.38.1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.38.0...v0.38.1) (2023-12-04)


### Bug Fixes

* trigger re-release ([c43cae4](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/c43cae4bf2e261b6d1e7e137879e858a9e415aa2))

## [0.38.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.37.0...v0.38.0) (2023-11-29)


### Features

* **stack-data-ums:** selfservice portal ([0b39cf6](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/0b39cf6460407709d710d3bae9fedc5d6bb4ab46))

## [0.37.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.36.0...v0.37.0) (2023-11-29)


### Features

* Add additionalAnnotations to helm charts ([e92d5c7](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/e92d5c7088adcb1af92fd1e5574815f0456ac865))

## [0.36.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.35.0...v0.36.0) (2023-11-22)


### Features

* Add ConfigMap to hold the openDesk Announcements customization ([7063dee](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/7063dee5b51875b7390abe3c28d91cf4815d6af4))
* Add UMC policies and operationsets to enable Announcements ([0494b67](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/0494b67413c27cee2fc1c348abd2a0ce8059c25d))

## [0.35.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.34.0...v0.35.0) (2023-11-21)


### Features

* **stack-data-swp:** Integrate A2GM UDM Hook into the containerized stack. ([44518f0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/44518f07cbd33db1eebba012813c34d58f673597))

## [0.34.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.33.0...v0.34.0) (2023-11-21)


### Features

* **stack-data-swp:** allow configuring self-service smtp host ([4b365c4](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/4b365c4fa39aed4021aa12a02791b067bad0a3f0))

## [0.33.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.32.1...v0.33.0) (2023-11-17)


### Features

* **stack-data-swp:** include openDesk customizations for self-service ([40da783](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/40da7833227723f6b2783877e6d0c0988970e57b))

## [0.32.1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.32.0...v0.32.1) (2023-11-17)


### Bug Fixes

* **stack-data:** fix typos in UDM-REST configuration ([730946e](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/730946edde32a997755ff4a081ea9b1ee478fb2b))

## [0.32.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.31.0...v0.32.0) (2023-11-16)


### Features

* **stack-data-swp:** deactivate duplicate password-change entry in portal sidebar ([a37da7c](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/a37da7c44e15feff9fd322c4c36d0e1ecc926788))

## [0.31.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.30.2...v0.31.0) (2023-11-16)


### Features

* Apply umc-server patch to help with setting self-service attributes readonly ([06031a2](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/06031a283f2c4db9f93a3a2dc72fb908302e45ce))

## [0.30.2](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.30.1...v0.30.2) (2023-11-16)


### Bug Fixes

* Document "extraDataFiles" in the values file of stack-data-swp ([c00fe0b](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/c00fe0b8d0f37c4e9e111723d3f75ab04ca368db))

## [0.30.1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.30.0...v0.30.1) (2023-11-16)


### Bug Fixes

* Avoid renaming in a "modify" call of ox-connector ([6cda60e](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/6cda60ea89f7b713c58ec5677e8c432d113003fd))

## [0.30.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.29.2...v0.30.0) (2023-11-16)


### Features

* Configure the available user attributes in self-service ([c69b1fe](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/c69b1feb9007c98c6c0780ae40c57f95cc803660))

## [0.29.2](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.29.1...v0.29.2) (2023-11-16)


### Bug Fixes

* **stack-data-swp:** oxAccess for default user and template ([9f89cf2](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/9f89cf285e193e533ea5cdb75c4e69b4f87e0f88))

## [0.29.1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.29.0...v0.29.1) (2023-11-16)


### Bug Fixes

* **stack-data-swp:** `test.user` is now called `default.user` everywhere ([2cddbe9](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/2cddbe9e8cfdbab31c2bd9f576a4d63bdcc82eed))

## [0.29.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.28.0...v0.29.0) (2023-11-16)


### Features

* **stack-data-swp:** include settings for self-service ([ce2ab90](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/ce2ab90a2dee0895ad3c3fe55882a217df6ae20d))

## [0.28.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.27.1...v0.28.0) (2023-11-16)


### Features

* **stack-data-swp:** create keycloak 2fa group ([6933737](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/6933737f7a0aeaba1fae779b0ae2bcb826cdf2e4))

## [0.27.1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.27.0...v0.27.1) (2023-11-16)


### Bug Fixes

* **stack-data-swp:** default values for extended attributes on user creation ([e5966e5](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/e5966e500e44134653954d7b083963a972bcceb9))

## [0.27.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.26.2...v0.27.0) (2023-11-15)


### Features

* make default user passwords configurable ([c231356](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/c231356f404f3e886eb9029c68f3198e7b09861b))

## [0.26.2](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.26.1...v0.26.2) (2023-11-15)


### Bug Fixes

* **stack-data-swp:** enforce order for udm files ([f44d394](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/f44d3949c4fbf9fe64c4ff2b10efb07c86be9b49))

## [0.26.1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.26.0...v0.26.1) (2023-11-14)


### Bug Fixes

* **stack-data-swp:** ox tab as openDesk tab ([79ab345](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/79ab3456e1fa4e438dbbdd6897732530c793b305))

## [0.26.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.25.2...v0.26.0) (2023-11-14)


### Features

* **stack-data-swp:** default user template ([7e82670](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/7e82670d580be6fcb999497fcc570098230aebad))

## [0.25.2](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.25.1...v0.25.2) (2023-11-14)


### Bug Fixes

* Ensure default for UCR value "ucs/web/theme" ([a4a0f69](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/a4a0f691b12daf1faeea088004f33abd0d8f67e0))

## [0.25.1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.25.0...v0.25.1) (2023-11-11)


### Bug Fixes

* Quote "oxDefaultContext" in "oxContextResource" ([afb9bc5](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/afb9bc5979f3726aa86dddb2af1783ec7a3bcc43))

## [0.25.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.24.1...v0.25.0) (2023-11-10)


### Features

* Add a stub value for "kerberos/realm" ([a41d990](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/a41d9905e1b614f195624ace6948094f723cff9f))
* Add a stub value for "kerberos/realm" ([a219a44](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/a219a44f6023e5fbde09643720964d74d5b22f93))

## [0.24.1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.24.0...v0.24.1) (2023-11-10)


### Bug Fixes

* **swp:** oxContext default should be string ([9b04929](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/9b049295804b1672a6f59246ddbc3572485c296e))

## [0.24.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.23.0...v0.24.0) (2023-11-10)


### Features

* **swp:** create default ox context ([a6128e6](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/a6128e68cbeeb0e0a5f1590f0855ff9c42692f72))


### Bug Fixes

* **swp:** add missing properties to ox extended attributes ([27a4db3](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/27a4db38aa86e4add14c314f84d899123c54f111))

## [0.23.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.22.0...v0.23.0) (2023-11-10)


### Features

* Disable showing tracebacks in umc and udm rest via UCR values ([1194301](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/119430121b0f3749427aa533ace3365cb20d9968))

## [0.22.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.21.1...v0.22.0) (2023-11-09)


### Features

* Configure password hashing to use "bcrypt" ([642e308](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/642e308f5f11dee6ba9a54a904d845166d9ac3ca))

## [0.21.1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.21.0...v0.21.1) (2023-11-09)


### Bug Fixes

* **ucr:** include settings for container-ldap ([02ebd68](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/02ebd68166cc0896ded6c58329f683c63ccbee39))

## [0.21.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.20.0...v0.21.0) (2023-11-09)


### Features

* Disable Piwik tracking ([3eebbd0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/3eebbd0de8bc33ade154aed2f98a2d0f21bdf3d2))

## [0.20.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.19.0...v0.20.0) (2023-11-09)


### Features

* Disable portal and oxcontext in admin interface ([b078aff](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/b078aff12664705b177b4ef8190f16ca0e8fc33c))

## [0.19.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.18.0...v0.19.0) (2023-11-09)


### Features

* Add messages regarding the password complexity rules. ([f66eb9f](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/f66eb9f235c8dfd47b5052569bd6cfaf872c55c8))

## [0.18.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.17.0...v0.18.0) (2023-11-08)


### Features

* Apply hardening configuration regarding UMC cookies ([2ac6680](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/2ac6680d392db38fdb43806b0effd3b210d752c8))

## [0.17.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.16.0...v0.17.0) (2023-11-07)


### Features

* **swp:** Add OX Context tile ([96f268c](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/96f268c2eb6bd817d8566121c4c61052dd50afb9))

## [0.16.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.15.2...v0.16.0) (2023-11-07)


### Features

* make the udm-data configmap extensible via custom values files ([f435fe5](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/f435fe5f68b1047616619a2a84d00a261c282fba))

## [0.15.2](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.15.1...v0.15.2) (2023-11-06)


### Bug Fixes

* **docker:** bump common-ci to build latest image ([6c4effe](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/6c4effe97e351ac5d548694c40d99e27ebd4259e))

## [0.15.1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.15.0...v0.15.1) (2023-11-06)


### Bug Fixes

* Provide stub data to workaround required fields during stack bootstrap ([27dd15d](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/27dd15d5cfe3fdf164ee6c43a28d3143ec1b37a5))

## [0.15.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.14.0...v0.15.0) (2023-11-06)


### Features

* Apply UCR settings regarding the User Creation Wizard ([59696d1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/59696d1e43b3003eb14de76565ea807ccd5e5af6))

## [0.14.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.13.3...v0.14.0) (2023-11-03)


### Features

* **swp:** ox-connector install join ([f149606](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/f14960641032154d7ba1b15a860bc4c114855bdf))

## [0.13.3](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.13.2...v0.13.3) (2023-11-03)


### Bug Fixes

* **stack-data-swp:** Remove invalid property from users/ldap ([37ecf37](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/37ecf37c272977f634fa01904623a147de737d61))

## [0.13.2](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.13.1...v0.13.2) (2023-11-03)


### Bug Fixes

* **versions:** produce version-tagged Docker images ([c4d929d](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/c4d929dcf48ffd45cdc35905c45a35719b54b85b))

## [0.13.1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.13.0...v0.13.1) (2023-11-02)


### Bug Fixes

* **stack-data-swp:** Create LDAP search users as users/ldap, so they are hidden from the Admin UI ([da70394](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/da70394085c1b3f98a17e57f40a9c9c14f40885f))
* **stack-data-swp:** Reorder productivity icons for openDesk ([ffc241c](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/ffc241c5117d708ebb582cd3d138764a46f1f733))

## [0.13.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.12.0...v0.13.0) (2023-11-02)


### Features

* **stack-data-swp:** Add openDesk branding to configmap that can be mouted by the portal-frontend ([c877530](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/c8775301da650f134b23796e51b9ae5c3a120a75))
* **stack-data-swp:** use light theme for UMC ([ee18af1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/ee18af11b647d8ccfcb6bdc116fc938383f49284))


### Bug Fixes

* **stack-data-swp:** Fix sidebar link to imprint ([75d8e28](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/75d8e2895df70994117d36436a47e9bdcd236c56))
* **stack-data-swp:** Remove unwanted entries from sidebar ([bf2b33a](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/bf2b33a4c3a1a38175040fb32f598f6658680029))
* **stack-data-swp:** Remove unwanted title from login page ([f0a4164](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/f0a41643016ca0aeb68445d44d4c77849ab1ef78))
