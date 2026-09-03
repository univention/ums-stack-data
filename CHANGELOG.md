# Changelog

## [0.107.3](https://git.knut.univention.de/univention/dev/nubus-for-k8s/stack-data/compare/v0.107.2...v0.107.3) (2026-09-03)


### Bug Fixes

* **deps:** Update gitregistry.knut.univention.de/univention/dev/projects/ucs-base-image/ucs-base-python Docker tag to v5.3.0-build.20260903 ([4ab7adf](https://git.knut.univention.de/univention/dev/nubus-for-k8s/stack-data/commit/4ab7adf69866d68b7fb1649a2281d4e0ffedaa93)), closes [#0](https://git.knut.univention.de/univention/dev/nubus-for-k8s/stack-data/issues/0)

## [0.107.2](https://git.knut.univention.de/univention/dev/nubus-for-k8s/stack-data/compare/v0.107.1...v0.107.2) (2026-08-26)


### Bug Fixes

* **stack-data-ums:** set directory/manager/rest/server/port ([a3f6a02](https://git.knut.univention.de/univention/dev/nubus-for-k8s/stack-data/commit/a3f6a02110e2f5b2d7b8609bf0fca0ba5bd0e177)), closes [#0](https://git.knut.univention.de/univention/dev/nubus-for-k8s/stack-data/issues/0)

## [0.107.1](https://git.knut.univention.de/univention/dev/nubus-for-k8s/stack-data/compare/v0.107.0...v0.107.1) (2026-08-25)


### Bug Fixes

* **deps:** Update gitregistry.knut.univention.de/univention/dev/projects/ucs-base-image/ucs-base-python Docker tag to v5.3.0-build.20260824 ([c6de48c](https://git.knut.univention.de/univention/dev/nubus-for-k8s/stack-data/commit/c6de48c9d487ceb3a2d47d65a37eed798e9d9a95)), closes [#0](https://git.knut.univention.de/univention/dev/nubus-for-k8s/stack-data/issues/0)

## [0.107.0](https://git.knut.univention.de/univention/dev/nubus-for-k8s/stack-data/compare/v0.106.0...v0.107.0) (2026-08-19)


### Features

* add secure defaults for UCR variable kerberos/defaults/enctypes/permitted ([4d37ba9](https://git.knut.univention.de/univention/dev/nubus-for-k8s/stack-data/commit/4d37ba965b32ca86093ca8cb033d9d1303a900a9)), closes [univention/dev/nubus-for-k8s/umc#14](https://git.knut.univention.de/univention/dev/nubus-for-k8s/umc/issues/14)

## [0.106.0](https://git.knut.univention.de/univention/dev/nubus-for-k8s/stack-data/compare/v0.105.0...v0.106.0) (2026-08-12)


### Features

* **helm:** Enable structured logging by default ([fe3ac3a](https://git.knut.univention.de/univention/dev/nubus-for-k8s/stack-data/commit/fe3ac3a3d9799b744cb5fc66024681d545482562)), closes [univention/dev/internal/team-nubus#1671](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/1671)


### Bug Fixes

* **helm:** Remove memberOf from default LDAP eq index ([2ade0df](https://git.knut.univention.de/univention/dev/nubus-for-k8s/stack-data/commit/2ade0df80efdca2c5bd55c4b5e53292e2e593d91)), closes [univention/dev/internal/team-nubus#1671](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/1671)

## [0.105.0](https://git.knut.univention.de/univention/dev/nubus-for-k8s/stack-data/compare/v0.104.0...v0.105.0) (2026-07-21)


### Features

* disable NT hash generation ([738818b](https://git.knut.univention.de/univention/dev/nubus-for-k8s/stack-data/commit/738818bd62c858ec0f97c15899a78105a9e59783)), closes [univention/dev/ucs#3637](https://git.knut.univention.de/univention/dev/ucs/issues/3637)

## [0.104.0](https://git.knut.univention.de/univention/dev/nubus-for-k8s/stack-data/compare/v0.103.3...v0.104.0) (2026-07-16)


### Features

* create index for memberOf LDAP attribute by default ([0e8ec84](https://git.knut.univention.de/univention/dev/nubus-for-k8s/stack-data/commit/0e8ec84e81ee69e93de6c0c38e39b387877c4c28)), closes [univention/dev/ucs#1297](https://git.knut.univention.de/univention/dev/ucs/issues/1297)

## [0.103.3](https://git.knut.univention.de/univention/dev/nubus-for-k8s/stack-data/compare/v0.103.2...v0.103.3) (2026-07-02)


### Bug Fixes

* **deps:** Update base image ([ddae420](https://git.knut.univention.de/univention/dev/nubus-for-k8s/stack-data/commit/ddae420704c91065b3913a1608d60790fa837591)), closes [univention/dev/internal/team-nubus#1663](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/1663)

## [0.103.2](https://git.knut.univention.de/univention/dev/nubus-for-k8s/stack-data/compare/v0.103.1...v0.103.2) (2026-06-03)


### Bug Fixes

* **deps:** Pin urllib3 >=2.7.0 to address urllib3 CVEs ([56cd5da](https://git.knut.univention.de/univention/dev/nubus-for-k8s/stack-data/commit/56cd5da35f1fb3d2037f51e987f772383158b90a)), closes [univention/dev/internal/team-nubus#1649](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/1649)

## [0.103.1](https://git.knut.univention.de/univention/dev/nubus-for-k8s/stack-data/compare/v0.103.0...v0.103.1) (2026-05-18)


### Bug Fixes

* **deps:** Update gitregistry.knut.univention.de/univention/dev/projects/ucs-base-image/ucs-base-python Docker tag to v5.2.5-build.20260514 ([9792113](https://git.knut.univention.de/univention/dev/nubus-for-k8s/stack-data/commit/97921136daf93bde2b01e5afb03033fd31723bb6)), closes [#0](https://git.knut.univention.de/univention/dev/nubus-for-k8s/stack-data/issues/0)
