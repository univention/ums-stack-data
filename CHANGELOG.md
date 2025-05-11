# Changelog

## [0.91.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.90.1...v0.91.0) (2025-05-11)


### Features

* move and upgrade ucs-base-image to 0.17.3-build-2025-05-11 ([b70e57a](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/b70e57a5e25145ceec9ce6972e5fcf91cd0da7dc))

## [0.90.1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.90.0...v0.90.1) (2025-05-10)


### Bug Fixes

* move addlicense pre-commit hook ([19b2c74](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/19b2c748a723be394cc9bffc889b80de654d2f48))
* update common-ci to main ([b0fd095](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/b0fd095a13d3ea715d2e630cac7808648b664308))

## [0.90.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.89.4...v0.90.0) (2025-04-29)


### Features

* Bump ucs-base-image version ([e38abf7](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/e38abf7518307c24f40c836b68f86569ac69aaff)), closes [univention/dev/internal/team-nubus#1155](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/1155)

## [0.89.4](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.89.3...v0.89.4) (2025-04-28)


### Bug Fixes

* Added index for univetionObjectIdentifier ([09545bc](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/09545bc66cc84561999ad4fbfb8edf9ea6d60cf1)), closes [univention/dev/internal/team-nubus#1019](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/1019)
* **docker:** Bump ucs-base-image ([d56abcd](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/d56abcdd34ac810542240e1baa7db15f2d95d3a3)), closes [univention/dev/internal/team-nubus#1019](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/1019)

## [0.89.3](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.89.2...v0.89.3) (2025-04-22)


### Bug Fixes

* **self-service:** add "c" to allowed list of LDAP attributes to be changed in default profile view ([569b797](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/569b7973acd6c9155e45e7b9b96b519ae1c685c1)), closes [#57397](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/issues/57397)

## [0.89.2](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.89.1...v0.89.2) (2025-04-10)


### Bug Fixes

* make copy calls in container init more robust ([0da5b87](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/0da5b8707b3eb55ec0f240bfecfe78a8b87d911e)), closes [univention/dev/internal/team-nubus#1079](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/1079)

## [0.89.1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.89.0...v0.89.1) (2025-04-04)


### Bug Fixes

* Set default log level for apache2 to "info" ([205f132](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/205f13211fdf68f49661c0bccbb0fa30e768c7f8))
* Set default log level for UMC to "2" ([add40e5](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/add40e570e722462f6029f4bbedaca186c2c8fef))

## [0.89.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.88.0...v0.89.0) (2025-03-12)


### Features

* removed two unused user groups from config that are obsolete since we are no longer using vms ([b4003a8](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/b4003a87379dd2626b434559e0f62afecf22af67))

## [0.88.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.87.0...v0.88.0) (2025-03-04)


### Features

* migrate project from pipfile to uv and update the container build ([2363b49](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/2363b49ecae88d1f38ef7f769fdaacd5ec01c0b4))


### Bug Fixes

* Don't cache the project source and introduce outdated sources and fix e2e test findings ([93b2825](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/93b2825f56e65b50fd05d50c5793ee37d1bb94a0))
* make data-loader unittests run again ([8d5977c](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/8d5977c7b6c5b6c68b18890ed609d26c67e97e92))
* make helm unittests run again in docker compose ([7693b65](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/7693b65079fe9c0c1512b37ca75070a8b0fdad14))
* make stack-data helm unittests run again ([535a17b](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/535a17b482ab5cebf4c978a26b34c5672ef875c1))

## [0.87.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.86.0...v0.87.0) (2025-02-27)


### Features

* Replace "common" with "nubus-common" ([1227241](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/1227241ff2a05d1b2582f6113ef72dfe01c0b24d))
* The the password for svc-portal-server managed ([f2b1312](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/f2b131236d818f4dc52e2cc988553a4d311b6796))

## [0.86.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.85.0...v0.86.0) (2025-02-26)


### Features

* add new data loader actions ([98b86b4](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/98b86b4c3838d45c636a1679aa55b6f1403f91f1))
* support groups in create_or_modify ([7805d08](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/7805d084a759a95c013e25196e5122287cf482a2))

## [0.85.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.84.0...v0.85.0) (2025-02-26)


### Features

* Bump ucs-base-image to use released apt sources ([f277af9](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/f277af9f93cd1599d2eff23a5bab1a78c83e1836))

## [0.84.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.83.1...v0.84.0) (2025-02-26)


### Features

* Create the group "Domain Service Users" ([34808b1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/34808b12d1d16095833483962b8426a42b6f82eb))
* Give UDM Access to the group "Domain Service Users" ([f34f954](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/f34f9546d5dc202ae2afb48ad773c2fde01a7bc4))

## [0.83.1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.83.0...v0.83.1) (2025-02-14)


### Bug Fixes

* Enable OX Contexts module ([0d42c5d](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/0d42c5daf6002e5c7bf9c4d06d6e3923d8a8700c))

## [0.83.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.82.1...v0.83.0) (2025-02-13)


### Features

* remove injected configuration from nubusStackDataUms ([1709f55](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/1709f55e148fd5e21b668813949c66f18d173737))

## [0.82.1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.82.0...v0.82.1) (2025-02-10)


### Bug Fixes

* add .kyverno to helmignore ([6e7ee61](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/6e7ee61819c605c9a81af7425c6ac7c51a0e923d))

## [0.82.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.81.0...v0.82.0) (2024-12-20)


### Features

* upgrade UCS base image to 2024-12-12 ([af10919](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/af10919e54ae0a22112bacce5aca28c038978975))

## [0.81.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.80.2...v0.81.0) (2024-12-11)


### Features

* Allow to disable the data loader job ([394403e](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/394403e7a6d89b1a36fe9d37620742adf0ea6d3c))

## [0.80.2](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.80.1...v0.80.2) (2024-12-10)


### Bug Fixes

* kyverno lint for stack-data-ums ([a957997](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/a957997f484cf440f62e06b85f6cc34243641ba8))

## [0.80.1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.80.0...v0.80.1) (2024-12-04)


### Bug Fixes

* Administrator in the Domain Admins group ([56b02c1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/56b02c1c3a57d0c5801788d71dcfc0d03926c670))

## [0.80.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.79.0...v0.80.0) (2024-12-03)


### Features

* implement PM feedback users module ([dd7db58](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/dd7db58bdb0dac251d46907162a4be0a8f2e6eff))

## [0.79.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.78.0...v0.79.0) (2024-11-27)


### Features

* upgrade kyverno pre-commit hook ([25f03f1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/25f03f16aca1be01b3682f2b4340ef862f2e91ed))


### Bug Fixes

* kyverno lint ([96f83f8](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/96f83f83e6d884d9f6a2b0f426904849db8c6e2e))
* lint, add a systemExtension to the linter_values.yaml file ([333268e](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/333268e240192de39da8adf5abfde29c39a49721))
* move some values to kyverno to not break tests ([5467d4e](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/5467d4e63857f3dd8ad10ef1275d2a746c8efeea))

## [0.78.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.77.0...v0.78.0) (2024-10-26)


### Features

* migrate helm templates to jinja2 ([f6f5a34](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/f6f5a34bd939c9510846f907ccf9d110a86752d7))


### Bug Fixes

* remove unused values from templateContext ([cc6b302](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/cc6b302dcf7bd302a19dec3ecfa74218e7d65057))

## [0.77.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.76.0...v0.77.0) (2024-10-25)


### Features

* change UCR values for Nubus ([23681c0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/23681c07190248558be52736fa13dbb2052db511))

## [0.76.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.75.0...v0.76.0) (2024-10-23)


### Features

* add SAML login tile ([b83cb79](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/b83cb7902e3288be6e96e2a23d94ed502af7753c))

## [0.75.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.74.0...v0.75.0) (2024-10-22)


### Features

* add Welcome! portal tile ([e040bde](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/e040bde049df8db246e751fd021143cabd381be8))


### Bug Fixes

* add self service portal entries to domain portal ([2457e69](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/2457e698340b1ee9dc2ec63ce88a8c4c3be69d77))

## [0.74.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.73.1...v0.74.0) (2024-10-14)


### Features

* enable showUmc for the portal and configure default modules ([e8c80b4](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/e8c80b4885184f55965fb2d94656b720ffb54a08))

## [0.73.1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.73.0...v0.73.1) (2024-10-10)


### Bug Fixes

* **stack-data-ums:** remove unused SysIdpUser ([46ce647](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/46ce647073b45bca0f4d562d48378012999c8576))

## [0.73.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.72.0...v0.73.0) (2024-10-09)


### Features

* change job backoffLimit and restartPolicy ([b0f74ce](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/b0f74ceed0d3fa213bd22fe72d74de33ba3f3406))

## [0.72.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.71.0...v0.72.0) (2024-10-04)


### Features

* default to dark theme ([9e5e748](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/9e5e748932cf4e79d1ab42e36a6da4eac4207b43))


### Bug Fixes

* Portal title to UCS default ([84d7def](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/84d7defc230eb48080da31c7020dcc9134eae20f))

## [0.71.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.70.1...v0.71.0) (2024-09-26)


### Features

* **ci:** enable malware scanning, disable sbom generation ([0a64ff5](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/0a64ff50fc80801ade1d7568fa5472ee289c52a2))

## [0.70.1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.70.0...v0.70.1) (2024-09-16)


### Bug Fixes

* Add parameter "extraDataFiles" into values of stack-data-ums ([a4b4662](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/a4b4662f2eddb81dd320b36b28759fdf0eac76b6))

## [0.70.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.69.3...v0.70.0) (2024-09-13)


### Features

* update UCS base image to 2024-09-09 ([f655213](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/f65521352fe646dff5b5a8cb34ddf8dde660b2ee))
* upgrade joinscript tools base image to UCS 5.2 ([8c0507b](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/8c0507bcaabdbcd8ffb445eb210a4316ea9b2405))

## [0.69.3](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.69.2...v0.69.3) (2024-09-11)


### Bug Fixes

* disable showUmc ([878fc23](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/878fc2350fc2cda297ed0e2775449d48e37d373f))

## [0.69.2](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.69.1...v0.69.2) (2024-09-11)


### Bug Fixes

* default value contains port ([fe09450](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/fe09450203f6a4484b5d9f5dd146477d6b6e9e6a))

## [0.69.1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.69.0...v0.69.1) (2024-09-10)


### Bug Fixes

* **data-loader:** refresh udm-rest-api cache using DNS discovery ([caa3bf3](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/caa3bf3769d26870f4ebdc3242ff2a6180287c9c))

## [0.69.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.68.0...v0.69.0) (2024-09-10)


### Features

* **stack-data-ums:** template UMC login tile ([debea6a](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/debea6a5d3ddff32bb1bf78b2e615fd056416700))

## [0.68.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.67.0...v0.68.0) (2024-09-09)


### Features

* add remove_from_list function ([c2503c3](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/c2503c3ffcdf18a31cd8a9bbdcb352b5a36376eb))
* install UMC policies by default and remove flag ([e3a0f63](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/e3a0f63529c719b1449bc9e652cf827869979db8))

## [0.67.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.66.0...v0.67.0) (2024-09-03)


### Features

* **stack-data-swp:** remove chart and files ([715e319](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/715e319edbdd148e9b11fd71c00904f436f50cea))

## [0.66.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.65.0...v0.66.0) (2024-09-03)


### Features

* added value to enable default login in the portal ([574893c](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/574893cdebfefbf143a3c8916ba9117a2abb2cf5))

## [0.65.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.64.1...v0.65.0) (2024-09-02)


### Features

* migrate test users to external extensions ([e5f0b5b](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/e5f0b5bbdf083e11041e25c46d79bc53b64b3239))


### Bug Fixes

* Administrator has the Guardian admin role ([a064800](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/a06480045e19b60513ff497a75f3f8f6846f70c0))
* Administrator user has its own credentials ([b5708b0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/b5708b0398a8299c18f4398a478799914514e254))

## [0.64.1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.64.0...v0.64.1) (2024-08-29)


### Bug Fixes

* **stack-data-ums:** Merge priorities and order for UCR variables ([646128c](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/646128cf632e24d2fa48d38a7d92441e8e17c7dd))

## [0.64.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.63.0...v0.64.0) (2024-08-28)


### Features

* Add empty base-defaults.conf file ([2950473](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/29504735ca5d18b0807c826feb0142f4a94efef7))
* configure UCR from Helm ([015dd8a](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/015dd8aa3f125d9cbbdc9fdd33203eeff6da1b94))
* support duplicated keys in configmap ([31c25e7](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/31c25e7f1fb2b0d63df3fc50b138406b60149372))


### Bug Fixes

* add missing config ([e0f11c5](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/e0f11c518b07b98885b5447754b1d97c44468095))
* add quotation ([6f0dbd1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/6f0dbd18abf5e27c9c22750ffadb8d59e806bb3f))
* exact match old values ([d01e899](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/d01e8999a74af0334a73bb8c35ed8fa3cc3f9ff5))
* quotation of CSP ([096e9b4](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/096e9b4a24ecb94aebb38fffa988c86300255cb7))
* quote templates ([85b7ce6](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/85b7ce643591c0359f03fc6cc503ab1ad156f2d6))

## [0.63.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.62.0...v0.63.0) (2024-08-27)


### Features

* create user for ldap federation on plain nubus ([ee9a9e7](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/ee9a9e7e5bd48429fd4f74bf36896c9f2848dd1c))


### Bug Fixes

* qa fixes ([4c86ef2](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/4c86ef2aba54888fc1edbc6e97b688ea91647b2e))

## [0.62.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.61.1...v0.62.0) (2024-08-21)


### Features

* set data loader status flag ([ce5b817](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/ce5b8172cb2cbab5ce0c27b8d4fbbefdd25518cf))


### Bug Fixes

* **data-loader:** disable fancy exception formatting by typer / click ([3d9cade](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/3d9cade602aec96700cee7007b0ad4b9f2f2b03d))

## [0.61.1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.61.0...v0.61.1) (2024-08-15)


### Bug Fixes

* Correct self-service sender email address configuration in UCR ([abfabd7](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/abfabd75cc4643f6292bf45753fb173e22f5f176))

## [0.61.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.60.1...v0.61.0) (2024-08-14)


### Features

* remove files added to opendesk repo ([5971d3e](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/5971d3e57578ebacbe35b8e53eb61dc8229d710e))
* remove ox-extension from stack-data ([df9a2c2](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/df9a2c242f7bcde26dc76d06aba6df0e614ba339))


### Bug Fixes

* qa fixes ([fb2f696](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/fb2f69615a032dab9907c599d9240845d1dd422b))

## [0.60.1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.60.0...v0.60.1) (2024-08-09)


### Bug Fixes

* **stack-data-swp:** Drop patches ([38b8fc5](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/38b8fc5381bd98b4eeb434e2e2a2d6d6f0bd1d96))

## [0.60.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.59.2...v0.60.0) (2024-08-05)


### Features

* **stack-data-swp:** remove attribute-to-group mapper ([a776328](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/a776328b50ba9df1d79367eb85f34cdd1bf16aeb))

## [0.59.2](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.59.1...v0.59.2) (2024-08-05)


### Bug Fixes

* **data-loader:** missing dependency ([27123ab](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/27123ab20b320d8e2c71fd44bd37ff0824c9bea9))

## [0.59.1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.59.0...v0.59.1) (2024-08-05)


### Bug Fixes

* **data-loader:** Workaround to refresh the UDM REST API users/user cache ([90c44d1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/90c44d147ab619f4d569fb9e56a2a2e3e638ff4d)), closes [#50253](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/issues/50253)

## [0.59.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.58.1...v0.59.0) (2024-08-02)


### Features

* **stack-data-swp:** remove announcements ([e995c35](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/e995c35120a435a5ba48d9fbceb7483aaffeeaa8))

## [0.58.1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.58.0...v0.58.1) (2024-07-30)


### Bug Fixes

* missing baseDn in user template ([6fa29f4](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/6fa29f49cf558a3a911d807d7a3cc039a16cf604))

## [0.58.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.57.0...v0.58.0) (2024-07-24)


### Features

* remove branding files ([edf24a4](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/edf24a4438cf6635dd0fb2fe1db2285d968cc56f))


### Bug Fixes

* re-add logo_small_border.svg file ([03f2d83](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/03f2d832125f711be0f9aeecbbac6a502132f64f))

## [0.57.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.56.0...v0.57.0) (2024-07-19)


### Features

* Remove data-loader files of the portal-extension ([7f699fe](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/7f699febdfb43df561d0aaefd480545e48f8a076))


### Bug Fixes

* Correct extension related configuration in the values of stack-data-ums ([87baa66](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/87baa66c8361447127ec9f3b2bfeabedafb7aa51))

## [0.56.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.55.1...v0.56.0) (2024-07-19)


### Features

* Add init containers to load the data files from extensions ([7e8680d](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/7e8680da082f922e7ced425742c091936da30713))
* Configure security context by default ([5d525d3](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/5d525d39f956d4126186fde29f3902e05f888ad5))


### Bug Fixes

* Support "containerSecurityContext" in all containers ([51fefc3](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/51fefc3fa6d32baa203e19dc0b78eda9f594c002))
* Support "podSecurityContext" in the Job of stack-data-ums ([313416e](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/313416e929d7cfdbd6868adbe3939203e722855f))

## [0.55.1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.55.0...v0.55.1) (2024-07-18)


### Bug Fixes

* Correct template stack-data-ums.ldapUri ([d2871b2](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/d2871b27247fb93516f2f413c743717dd70a95fd))
* Correct templates around initial passwords ([f194c31](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/f194c313c48b893d76629c347fecfb9abf268766))

## [0.55.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.54.0...v0.55.0) (2024-07-18)


### Features

* Add configuration option "logTemplate" into Helm chart ([88b6f48](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/88b6f48951c6182fa2653a6a4238e08af3d51b2d))
* Allow to log the rendered template in data-loader ([4f2c45e](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/4f2c45e4ca42f66f9b9e6a1d437f1320ebab48fe))


### Bug Fixes

* Apply "global.imageRegistry" also in initContainers ([eea7d94](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/eea7d94562319d35fca3d69174233c6b48664036))
* Correct handling of global.imagePullSecrets ([1ad5286](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/1ad5286cd0fb653ee2888a8505163ccd48511664))
* Correct handling of image registry ([c1bee3b](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/c1bee3ba7aaf3cf506baf1851479f8653f4226e8))
* Correctly apply "global.imagePullPolicy" ([d0187d3](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/d0187d321391ee0d3ffecaf48e3db6970ea5be7b))

## [0.54.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.53.0...v0.54.0) (2024-07-18)


### Features

* Allow to enable logging of the template context ([0a81508](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/0a815082d6b832aa6fddcc3fb51c0200ccf30780))
* Define the template context via values ([b5f5d52](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/b5f5d5227e3827a07cd9d41f3d4fbe0e84e48eb0))
* fixup - Mount into "/template-context" ([2af1281](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/2af12810ae075549b26e580fb2c455825bcd8c6c))
* Process templates with context from secret ([163ab9e](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/163ab9ecb69180f5ee7977c24a1058edd817fbc0))
* **stack-data-ums:** context as secret ([acacd97](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/acacd97ca6f0d4352711f76c2e339244fefd9a2b))
* Support files templated at runtime from "default-v2" folder ([713e719](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/713e7194a8339b5cfe6d3c5a9712c146b8dedd01))


### Bug Fixes

* "installUmcPolicies" always has to be present in the template context ([e079aac](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/e079aac5dd77c0e4175a62058943d45d5def8b55))
* Configure "installUmcPolicies" as boolean ([1d5cdc3](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/1d5cdc3f382238f58fc947ac99a28dd6ea02ca7b))

## [0.53.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.52.2...v0.53.0) (2024-07-17)


### Features

* Add jinja2 and PyYAML as dependencies ([aadf029](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/aadf0296d44b5ddfc17cbb3f1c84758d83b0bf1c))
* Add support for UDM connection configuration into CLI ([c8a6634](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/c8a663457e41b5557b2ed18a9ed86cd47e660b5f))
* Add typer into the Python environment ([e4edd83](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/e4edd83c9035e59e43d4758547b8a2465cac67ae))
* Allow to configure template extension ([b49852d](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/b49852dae96da7cbc0410bfce98e983a8155c804))
* Allow to enable logging of the merged context ([2e1a648](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/2e1a6485941e18016211bc56908165dffb8156ca))
* Allow to pass a template context into the App object ([33873de](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/33873de36ef9d801053b38b61f1d493f8fee20c7))
* Implement deep merging of context values ([9fa4727](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/9fa47274fb8369a945477f32cb15381603ca7358))
* Load template context from file ([8374f44](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/8374f4450c4d3f73b7cd183dae4bea72ae49aecf))
* Process all files through the template engine by default ([5fd6b2d](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/5fd6b2d149dd3e977986b9780d76c221b7224883))
* Run app via typer ([62d5c4f](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/62d5c4f4a524448a718233a0b73de686fd326a54))
* Update Python dependencies ([881e9f6](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/881e9f666413124b47b7630b3b5ec7b5e151790d))
* Use pipenv out of the Debian packages ([fc11ba5](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/fc11ba536da5a9ac16bfd3da43ce2633de9b8852))


### Bug Fixes

* Accept the filename to process as cli argument ([199917d](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/199917d1da0aaf2b502cbc49b0aa700e06294b7f))
* Install Python dependencies into final image ([0e68c35](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/0e68c351d0c20cfce3400e59112ffc9b3017dacd))
* Move pytest dependencies into dev section ([4f697d9](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/4f697d96212442fd539b154c1f08ce07139ebd73))
* Simple merge of context values ([5c711b7](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/5c711b7c0dfec8d4a1b98ebd1a1085bf5516a836))

## [0.52.2](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.52.1...v0.52.2) (2024-07-16)


### Bug Fixes

* make UCR umc/web/title available as Helm value ([4bbca4e](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/4bbca4e6b77a7a7872c10cc7ff92c142b953b7ed))

## [0.52.1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.52.0...v0.52.1) (2024-07-16)


### Bug Fixes

* **stack-data-swp:** wrong portal title ([08074b3](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/08074b3b387ac8fd45e6d3c340f3903f8f73b429))
* **stack-data-swp:** wrong tile links ([ec2ad42](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/ec2ad42034c52e95038d7521914040537e1bbd91))

## [0.52.0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.51.1...v0.52.0) (2024-07-05)


### Features

* password reset email customizable now customizable; text moved to openDesk ([605a2f0](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/605a2f05b525a197c92a58f6457e842ba9675575))

## [0.51.1](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/compare/v0.51.0...v0.51.1) (2024-07-04)


### Bug Fixes

* guardian UDM property now in vanilla UDM, fix role value ([54072e3](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/54072e3c19f303814176de07353fea20732b6bed))
* remove LDAP index for App Center attribute ([06f01ee](https://git.knut.univention.de/univention/customers/dataport/upx/stack-data/commit/06f01ee368c100300994a0d43cbcc24e92b9e318))

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
