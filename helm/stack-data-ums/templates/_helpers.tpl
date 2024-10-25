{{- /*
SPDX-FileCopyrightText: 2024 Univention GmbH
SPDX-License-Identifier: AGPL-3.0-only
*/}}

{{- /*
These template definitions relate to the use of this Helm chart as a sub-chart of the Nubus Umbrella Chart.
Templates defined in other Helm sub-charts are imported to be used to configure this chart.
If the value .Values.global.nubusDeployment equates to true, the defined templates are imported.
*/}}
{{- define "stack-data-ums.initialPasswordAdministrator" -}}
{{- if .Values.global.nubusDeployment -}}
{{- include "nubusTemplates.credentials.administrator.password" . -}}
{{- else -}}
{{- required "stackDataContext.initialPasswordAdministrator is missing" .Values.stackDataContext.initialPasswordAdministrator -}}
{{- end -}}
{{- end -}}


{{- define "stack-data-ums.ldapUri" -}}
{{- if .Values.global.nubusDeployment -}}
{{- include "nubusTemplates.ldapServer.ldap.connection.uri" . -}}
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.ldapHost" -}}
{{- if .Values.stackDataContext.ldapHost -}}
{{- tpl .Values.stackDataContext.ldapHost . -}}
{{- else if .Values.global.nubusDeployment -}}
{{- include "nubusTemplates.ldapServer.ldap.connection.host" . -}}
{{- else -}}
ldap-server
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.ldapPort" -}}
{{- if .Values.stackDataContext.ldapPort -}}
{{- .Values.stackDataContext.ldapPort -}}
{{- else if .Values.global.nubusDeployment -}}
{{- include "nubusTemplates.ldapServer.ldap.connection.port" . -}}
{{- else -}}
389
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.ldapMasterHost" -}}
{{- if .Values.stackDataContext.ldapMasterHost -}}
{{- tpl .Values.stackDataContext.ldapMasterHost . -}}
{{- else if .Values.global.nubusDeployment -}}
{{- include "nubusTemplates.ldapServer.ldap.connection.host" . -}}
{{- else -}}
{{- include "stack-data-ums.ldapHost" . -}}
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.ldapMasterPort" -}}
{{- if .Values.stackDataContext.ldapMasterPort -}}
{{- .Values.stackDataContext.ldapMasterPort -}}
{{- else if .Values.global.nubusDeployment -}}
{{- include "nubusTemplates.ldapServer.ldap.connection.port" . -}}
{{- else -}}
389
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.ldapBaseDn" -}}
{{- if .Values.stackDataContext.ldapBase -}}
{{- .Values.stackDataContext.ldapBase -}}
{{- else if .Values.global.nubusDeployment -}}
{{- include "nubusTemplates.ldapServer.ldap.baseDn" . -}}
{{- else -}}
dc=univention-organization,dc=intranet
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.enableDefaultLogin" -}}
{{- if .Values.stackDataContext.enableDefaultLogin -}}
{{- .Values.stackDataContext.enableDefaultLogin -}}
{{- else if .Values.global.nubusDeployment -}}
{{- include "nubusTemplates.enablePlainUmcLogin" . -}}
{{- else -}}
false
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.samlServiceProviders" -}}
{{- if .Values.stackDataContext.ldapSamlSpUrls -}}
{{- .Values.stackDataContext.ldapSamlSpUrls -}}
{{- else if .Values.global.nubusDeployment -}}
{{- include "nubusTemplates.ldapServer.samlServiceProviders" . -}}
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.samlMetadataUrl" -}}
{{- if .Values.stackDataContext.idpSamlMetadataUrl -}}
{{- .Values.stackDataContext.idpSamlMetadataUrl -}}
{{- else if .Values.global.nubusDeployment -}}
{{- include "nubusTemplates.ldapServer.samlMetadataUrl" .  -}}
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.samlMetadataUrlInternal" -}}
{{- if .Values.stackDataContext.idpSamlMetadataUrlInternal -}}
{{- .Values.stackDataContext.idpSamlMetadataUrlInternal -}}
{{- else if .Values.global.nubusDeployment -}}
{{- include "nubusTemplates.ldapServer.samlMetadataUrlInternal" .  -}}
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.ldapAdminDn" -}}
{{- if .Values.stackDataContext.ldapHostDn -}}
{{- .Values.stackDataContext.ldapHostDn -}}
{{- else if .Values.global.nubusDeployment -}}
{{- include "nubusTemplates.ldapServer.ldap.adminDn" . -}}
{{- else -}}
cn=admin,dc=univention-organization,dc=intranet
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.udmApiUrl" -}}
{{- if .Values.stackDataUms.udmApiUrl -}}
{{- .Values.stackDataUms.udmApiUrl -}}
{{- else if .Values.global.nubusDeployment -}}
{{- include "nubusTemplates.udmRestApi.uri" . -}}
{{- else -}}
http://udm-rest-api:9979/udm/
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.udmApiPort" -}}
{{- if .Values.stackDataUms.udmApiPort -}}
{{- .Values.stackDataUms.udmApiPort -}}
{{- else if .Values.global.nubusDeployment -}}
{{- include "nubusTemplates.udmRestApi.port" . -}}
{{- else -}}
9979
{{- end -}}
{{- end -}}

{{- /*
These template definitions are only used in this chart and do not relate to templates defined elsewhere.
*/}}

{{- define "stack-data-ums.umcPostgresqlHostname" -}}
{{- if .Values.stackDataContext.umcPostgresqlHostname -}}
{{- .Values.stackDataContext.umcPostgresqlHostname -}}
{{- else if .Values.global.nubusDeployment -}}
{{- (coalesce .Values.nubusUmcServer.postgresql.connection.host .Values.global.postgresql.connection.host) | default (printf "%s-postgresql" .Release.Name)  -}}
{{- else -}}
umc-server-postgresql
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.umcPostgresqlPort" -}}
{{- if .Values.stackDataContext.umcPostgresqlPort -}}
{{- .Values.stackDataContext.umcPostgresqlPort -}}
{{- else if .Values.global.nubusDeployment -}}
{{- coalesce .Values.nubusUmcServer.postgresql.connection.port .Values.global.postgresql.connection.port | default "5432" -}}
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.umcPostgresqlUsername" -}}
{{- if .Values.stackDataContext.umcPostgresqlUsername -}}
{{- .Values.stackDataContext.umcPostgresqlUsername -}}
{{- else if .Values.global.nubusDeployment -}}
{{- .Values.nubusUmcServer.postgresql.auth.username -}}
{{- else -}}
selfservice
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.umcPostgresqlDatabase" -}}
{{- if .Values.stackDataContext.umcPostgresqlDatabase -}}
{{- .Values.stackDataContext.umcPostgresqlDatabase -}}
{{- else if .Values.global.nubusDeployment -}}
{{- .Values.nubusUmcServer.postgresql.auth.database -}}
{{- else -}}
selfservice
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.umcMemcachedHostname" -}}
{{- if .Values.stackDataContext.umcMemcachedHostname -}}
{{- .Values.stackDataContext.umcMemcachedHostname -}}
{{- else if .Values.global.nubusDeployment -}}
{{- printf "%s-%s" .Release.Name (coalesce .Values.nubusUmcServer.memcached.nameOverride .Values.nubusUmcServer.memcached.connection.host) -}}
{{- else -}}
umc-server-memcached
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.umcMemcachedUsername" -}}
{{- if .Values.stackDataContext.umcMemcachedUsername -}}
{{- .Values.stackDataContext.umcMemcachedUsername -}}
{{- else if .Values.global.nubusDeployment -}}
{{- .Values.nubusUmcServer.memcached.auth.username -}}
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.domainName" -}}
{{- if .Values.stackDataContext.domainname -}}
{{- .Values.stackDataContext.domainname -}}
{{- else if .Values.global.nubusDeployment -}}
{{- required ".Values.global.domain has to be defined" .Values.global.domain -}}
{{- else -}}
univention-organization.intranet
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.externalMailDomain" -}}
{{- if .Values.stackDataContext.externalMailDomain -}}
{{- .Values.stackDataContext.externalMailDomain -}}
{{- else if .Values.global.nubusDeployment -}}
{{- required ".Values.global.domain has to be defined" .Values.global.domain -}}
{{- else -}}
univention-organization.test
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.subDomains.portal" -}}
{{- if .Values.stackDataContext.hostname -}}
{{- .Values.stackDataContext.hostname -}}
{{- else if .Values.global.nubusDeployment -}}
{{- required ".Values.global.subDomains.portal has to be defined" .Values.global.subDomains.portal -}}
{{- else -}}
portal
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.subDomains.keycloak" -}}
{{- if and .Values.global.nubusDeployment (not .Values.stackDataContext.idpFqdn) -}}
{{- required ".Values.global.subDomains.keycloak has to be defined" .Values.global.subDomains.keycloak -}}
{{- else -}}
id
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.keycloakFqdn" -}}
{{- if .Values.stackDataContext.idpFqdn -}}
{{- .Values.stackDataContext.idpFqdn -}}
{{- else if .Values.global.nubusDeployment -}}
{{- printf "%s.%s" (include "stack-data-ums.subDomains.keycloak" .) .Values.global.domain -}}
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.portalFqdn" -}}
{{- if .Values.stackDataContext.umcSamlSpFqdn -}}
{{- .Values.stackDataContext.umcSamlSpFqdn -}}
{{- else if .Values.global.nubusDeployment -}}
{{- printf "%s.%s" (include "stack-data-ums.subDomains.portal" .) .Values.global.domain -}}
{{- end -}}
{{- end -}}


{{- define "stack-data-ums.portalAuthMode" -}}
{{- if .Values.stackDataContext.portalAuthMode -}}
{{- .Values.stackDataContext.portalAuthMode -}}
{{- else if .Values.global.nubusDeployment -}}
saml
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.umcSamlSchemes" -}}
{{- if .Values.stackDataContext.umcSamlSchemes -}}
{{- .Values.stackDataContext.umcSamlSchemes -}}
{{- else if .Values.global.nubusDeployment -}}
https
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.udmApi.credentialSecret.name" -}}
{{- if .Values.global.nubusDeployment -}}
{{- printf "%s-udm-rest-api-credentials" .Release.Name -}}
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.udmApi.credentialSecret.key" -}}
{{- if .Values.global.nubusDeployment -}}
machine.secret
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.externalDomainName" -}}
{{- if .Values.stackDataContext.externalDomainName -}}
{{- .Values.stackDataContext.externalDomainName -}}
{{- else if .Values.global.nubusDeployment -}}
{{- required ".Values.global.domain has to be defined" .Values.global.domain -}}
{{- else -}}
univention-organization.intranet
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.showUmc" -}}
{{- if .Values.stackDataContext.showUmc -}}
{{- .Values.stackDataContext.showUmc -}}
{{- else -}}
false
{{- end -}}
{{- end -}}
