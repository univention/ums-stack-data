{{- /*
SPDX-FileCopyrightText: 2024-2025 Univention GmbH
SPDX-License-Identifier: AGPL-3.0-only
*/}}

{{- /*
These template definitions relate to the use of this Helm chart as a sub-chart of the Nubus Umbrella Chart.
Templates defined in other Helm sub-charts are imported to be used to configure this chart.
If the value .Values.global.nubusDeployment equates to true, the defined templates are imported.
*/}}
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

{{- define "stack-data-ums.oidcIssuerUrl" -}}
{{- if .Values.stackDataContext.idpOidcIssuerUrl -}}
{{- .Values.stackDataContext.idpOidcIssuerUrl -}}
{{- else if .Values.global.nubusDeployment -}}
    {{- $protocol := "https" -}}
    {{- $keycloakService := (include "stack-data-ums.keycloakFqdn" .) -}}
    {{- $nubusKeycloakDefaultRealm := "nubus" -}}
    {{- if and .Values.global.keycloak .Values.global.keycloak.realm -}}
        {{- printf "%s://%s/realms/%s" $protocol $keycloakService .Values.global.keycloak.realm -}}
    {{- else if .Values.global.nubusDeployment -}}
        {{- printf "%s://%s/realms/%s" $protocol $keycloakService $nubusKeycloakDefaultRealm -}}
    {{- end -}}
{{- end -}}
{{- end -}}

{{- define "stack-data-ums.oidcIssuerUrlInternal" -}}
{{- if .Values.stackDataContext.idpOidcIssuerUrlInternal -}}
{{- .Values.stackDataContext.idpOidcIssuerUrlInternal -}}
{{- else if .Values.global.nubusDeployment -}}
    {{- $protocol := "http" -}}
    {{- $keycloakService := printf "%s-keycloak" .Release.Name -}}
    {{- $keycloakServicePort := "8080" -}}
    {{- $nubusKeycloakDefaultRealm := "nubus" -}}
    {{- if and .Values.global.keycloak .Values.global.keycloak.realm -}}
        {{- printf "%s://%s:%s/realms/%s" $protocol $keycloakService $keycloakServicePort .Values.global.keycloak.realm -}}
    {{- else if .Values.global.nubusDeployment -}}
        {{- printf "%s://%s:%s/realms/%s" $protocol $keycloakService $keycloakServicePort $nubusKeycloakDefaultRealm -}}
    {{- end -}}
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
