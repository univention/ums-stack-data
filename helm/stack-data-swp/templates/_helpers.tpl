{{- /*
SPDX-FileCopyrightText: 2024 Univention GmbH
SPDX-License-Identifier: AGPL-3.0-only
*/}}

{{- /*
These template definitions relate to the use of this Helm chart as a sub-chart of the Nubus Umbrella Chart.
Templates defined in other Helm sub-charts are imported to be used to configure this chart.
If the value .Values.global.nubusDeployment equates to true, the defined templates are imported.
*/}}
{{- define "stack-data-swp.udmApiUrl" -}}
{{- if .Values.stackDataSwp.udmApiUrl -}}
{{- .Values.stackDataSwp.udmApiUrl -}}
{{- else if .Values.global.nubusDeployment -}}
{{- include "nubusTemplates.udmRestApi.uri" . -}}
{{- else -}}
http://udm-rest-api/udm/
{{- end -}}
{{- end -}}

{{- define "stack-data-swp.ldapBaseDn" -}}
{{- if .Values.stackDataContext.ldapBase -}}
{{- .Values.stackDataContext.ldapBase -}}
{{- else if .Values.global.nubusDeployment -}}
{{- include "nubusTemplates.ldapServer.ldap.baseDn" . -}}
{{- else -}}
dc=univention-organization,dc=intranet
{{- end -}}
{{- end -}}

{{- /*
These template definitions are only used in this chart and do not relate to templates defined elsewhere.
*/}}

{{- define "stack-data-swp.udmApi.credentialSecret.name" -}}
{{- if .Values.global.nubusDeployment -}}
{{- printf "%s-udm-rest-api-credentials" .Release.Name -}}
{{- end -}}
{{- end -}}

{{- define "stack-data-swp.udmApi.credentialSecret.key" -}}
{{- if .Values.global.nubusDeployment -}}
machine.secret
{{- end -}}
{{- end -}}


{{- define "stack-data-swp.externalDomainName" -}}
{{- if .Values.stackDataContext.externalDomainName -}}
{{- .Values.stackDataContext.externalDomainName -}}
{{- else if .Values.global.nubusDeployment -}}
{{- required ".Values.global.domain has to be defined" .Values.global.domain -}}
{{- else -}}
univention-organization.intranet
{{- end -}}
{{- end -}}

{{- define "stack-data-swp.externalMailDomain" -}}
{{- if .Values.stackDataContext.externalMailDomain -}}
{{- .Values.stackDataContext.externalMailDomain -}}
{{- else if .Values.global.nubusDeployment -}}
{{- required ".Values.global.domain has to be defined" .Values.global.domain -}}
{{- else -}}
univention-organization.test
{{- end -}}
{{- end -}}
