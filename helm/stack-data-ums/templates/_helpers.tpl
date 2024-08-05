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
{{- include "nubusTemplates.credentials.ldap.users.admin.password" . -}}
{{- else -}}
{{- required "stackDataContext.initialPasswordAdministrator is missing" .Values.stackDataContext.initialPasswordAdministrator -}}
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.initialPasswordSysIdpUser" -}}
{{- if .Values.global.nubusDeployment -}}
{{- include "nubusTemplates.credentials.ldap.users.idp.password" . -}}
{{- else -}}
{{- required "stackDataContext.initialPasswordSysIdpUser is missing" .Values.stackDataContext.initialPasswordSysIdpUser -}}
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

{{- define "stack-data-ums.ldapDomainName" -}}
{{- if .Values.stackDataContext.domainname -}}
{{- .Values.stackDataContext.domainname -}}
{{- else if .Values.global.nubusDeployment -}}
{{- include "nubusTemplates.ldapServer.ldap.domainName" . -}}
{{- else -}}
univention-organization.intranet
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
http://udm-rest-api/udm/
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

FIXME: Double check this, I'm not sure if it's correct

{{- define "stack-data-ums.oxDefaultContext" -}}
{{- if .Values.stackDataContext.oxDefaultContext -}}
{{- .Values.stackDataContext.oxDefaultContext -}}
{{- else if .Values.global.nubusDeployment -}}
{{- include "stack-data-ums.stackDataContext.oxDefaultContext" . -}}
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.portaltileGroupUserStandard" -}}
{{- if .Values.stackDataContext.portaltileGroupUserStandard -}}
{{- .Values.stackDataContext.portaltileGroupUserStandard -}}
{{- else if .Values.global.nubusDeployment -}}
{{- include "stack-data-ums.stackDataContext.portaltileGroupUserStandard" . -}}
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.portaltileGroupUserAdmin" -}}
{{- if .Values.stackDataContext.portaltileGroupUserAdmin -}}
{{- .Values.stackDataContext.portaltileGroupUserAdmin -}}
{{- else if .Values.global.nubusDeployment -}}
{{- include "stack-data-ums.stackDataContext.portaltileGroupUserAdmin" . -}}
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.portaltileGroupUserAll" -}}
{{- if .Values.stackDataContext.portaltileGroupUserAll -}}
{{- .Values.stackDataContext.portaltileGroupUserAll -}}
{{- else if .Values.global.nubusDeployment -}}
{{- include "stack-data-ums.stackDataContext.portaltileGroupUserAll" . -}}
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.portaltileGroupGroupware" -}}
{{- if .Values.stackDataContext.portaltileGroupGroupware -}}
{{- .Values.stackDataContext.portaltileGroupGroupware -}}
{{- else if .Values.global.nubusDeployment -}}
{{- include "stack-data-ums.stackDataContext.portaltileGroupGroupware" . -}}
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.portaltileGroupFileshare" -}}
{{- if .Values.stackDataContext.portaltileGroupFileshare -}}
{{- .Values.stackDataContext.portaltileGroupFileshare -}}
{{- else if .Values.global.nubusDeployment -}}
{{- include "stack-data-ums.stackDataContext.portaltileGroupFileshare" . -}}
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.portaltileGroupManagementProject" -}}
{{- if .Values.stackDataContext.portaltileGroupManagementProject -}}
{{- .Values.stackDataContext.portaltileGroupManagementProject -}}
{{- else if .Values.global.nubusDeployment -}}
{{- include "stack-data-ums.stackDataContext.portaltileGroupManagementProject" . -}}
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.portaltileGroupManagementKnowledge" -}}
{{- if .Values.stackDataContext.portaltileGroupManagementKnowledge -}}
{{- .Values.stackDataContext.portaltileGroupManagementKnowledge -}}
{{- else if .Values.global.nubusDeployment -}}
{{- include "stack-data-ums.stackDataContext.portaltileGroupManagementKnowledge" . -}}
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.portaltileGroupManagementLearn" -}}
{{- if .Values.stackDataContext.portaltileGroupManagementLearn -}}
{{- .Values.stackDataContext.portaltileGroupManagementLearn -}}
{{- else if .Values.global.nubusDeployment -}}
{{- include "stack-data-ums.stackDataContext.portaltileGroupManagementLearn" . -}}
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.portaltileGroupLiveCollaboration" -}}
{{- if .Values.stackDataContext.portaltileGroupLiveCollaboration -}}
{{- .Values.stackDataContext.portaltileGroupLiveCollaboration -}}
{{- else if .Values.global.nubusDeployment -}}
{{- include "stack-data-ums.stackDataContext.portaltileGroupLiveCollaboration" . -}}
{{- end -}}
{{- end -}}

# FIXME: Read it from portal title somewhere

{{- define "stack-data-ums.portalTitleDE" -}}
{{- if .Values.stackDataContext.portalTitleDE -}}
{{- .Values.stackDataContext.portalTitleDE -}}
{{- else if .Values.global.nubusDeployment -}}
{{- include "stack-data-ums.stackDataContext.portalTitleDE" . -}}
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.portalTitleEN" -}}
{{- if .Values.stackDataContext.portalTitleEN -}}
{{- .Values.stackDataContext.portalTitleEN -}}
{{- else if .Values.global.nubusDeployment -}}
{{- include "stack-data-ums.stackDataContext.portalTitleEN" . -}}
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.portalGroupwareLinkBase" -}}
{{- if .Values.stackDataContext.portalGroupwareLinkBase -}}
{{- .Values.stackDataContext.portalGroupwareLinkBase -}}
{{- else if .Values.global.nubusDeployment -}}
{{- include "stack-data-ums.stackDataContext.portalGroupwareLinkBase" . -}}
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.portalFileshareLinkBase" -}}
{{- if .Values.stackDataContext.portalFileshareLinkBase -}}
{{- .Values.stackDataContext.portalFileshareLinkBase -}}
{{- else if .Values.global.nubusDeployment -}}
{{- printf "https://fs.%s" (include "stack-data-ums.domainName" .) -}}
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.portalRealtimeCollaborationLinkBase" -}}
{{- if .Values.stackDataContext.portalRealtimeCollaborationLinkBase -}}
{{- .Values.stackDataContext.portalRealtimeCollaborationLinkBase -}}
{{- else if .Values.global.nubusDeployment -}}
{{- printf "https://chat.%s" (include "stack-data-ums.domainName" .) -}}
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.portalRealtimeVideoconferenceLinkBase" -}}
{{- if .Values.stackDataContext.portalRealtimeVideoconferenceLinkBase -}}
{{- .Values.stackDataContext.portalRealtimeVideoconferenceLinkBase -}}
{{- else if .Values.global.nubusDeployment -}}
{{- printf "https://meet.%s" (include "stack-data-ums.domainName" .) -}}
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.portalManagementProjectLinkBase" -}}
{{- if .Values.stackDataContext.portalManagementProjectLinkBase -}}
{{- .Values.stackDataContext.portalManagementProjectLinkBase -}}
{{- else if .Values.global.nubusDeployment -}}
{{- printf "https://project.%s" (include "stack-data-ums.domainName" .) -}}
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.portalManagementKnowledgeLinkBase" -}}
{{- if .Values.stackDataContext.portalManagementKnowledgeLinkBase -}}
{{- .Values.stackDataContext.portalManagementKnowledgeLinkBase -}}
{{- else if .Values.global.nubusDeployment -}}
{{- printf "https://wiki.%s" (include "stack-data-ums.domainName" .) -}}
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.ldapSearchUsers" -}}
{{- $newList := default (list) -}}
{{- if .Values.stackDataContext.ldapSearchUsers -}}
{{- range $item := .Values.stackDataContext.ldapSearchUsers -}}
{{- $newList = append $newList (dict "username" $item.username "lastname" $item.lastname "password" $item.password) -}}
{{- end -}}
{{ toYaml $newList | nindent 2 }}
{{- else if .Values.global.nubusDeployment -}}
{{- range $item := include "stack-data-ums.stackDataContext.ldapSearchUsers" . -}}
{{- $newList = append $newList (dict "username" $item.username "lastname" $item.lastname "password" $item.password) -}}
{{- end -}}
{{ toYaml $newList | nindent 2 }}
{{- end -}}
{{- end -}}


{{- define "stack-data-ums.ldapSystemUsers" -}}
{{- $newList := default (list) -}}
{{- if .Values.stackDataContext.ldapSystemUsers -}}
{{- range $item := .Values.stackDataContext.ldapSystemUsers -}}
{{- $newList = append $newList (dict "username" $item.username "lastname" $item.lastname "password" $item.password) -}}
{{- end -}}
{{ toYaml $newList | nindent 2 }}
{{- else if .Values.global.nubusDeployment -}}
{{- range $item := include "stack-data-ums.stackDataContext.ldapSystemUsers" . -}}
{{- $newList = append $newList (dict "username" $item.username "lastname" $item.lastname "password" $item.password) -}}
{{- end -}}
{{ toYaml $newList | nindent 2 }}
{{- else -}}
{{- range $item := include "stack-data-ums.stackDataContext.ldapSystemUsers" . -}}
{{- $newList = append $newList (dict "username" $item.username "lastname" $item.lastname "password" $item.password) -}}
{{- end -}}
{{ toYaml $newList | nindent 2 }}
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
