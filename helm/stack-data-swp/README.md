# stack-data-swp

A Helm chart to load the SWP specific initial data into the UMS Stack

- **Version**: 0.1.0
- **Type**: application
- **Homepage:** <https://www.univention.de/>

## TL;DR

```console
helm upgrade --install stack-data-udm oci://gitregistry.knut.univention.de/univention/customers/dataport/upx/stack-data/helm/stack-data-swp
```

## Introduction

The chart does install Kubernetes Jobs to load the SWP specific initial data of
the UMS Stack.

It depends on:

- A functional UDM Rest API being available and configured. The UDM Rest API is
  used to load the data.

- The base data from the chart "stack-data-ums".

## Installing

To install the chart with the release name `stack-data-swp`:

```console
helm upgrade --install stack-data-swp oci://gitregistry.knut.univention.de/univention/customers/dataport/upx/stack-data/helm/stack-data-swp
```

## Uninstalling

To uninstall the chart with the release name `stack-data-swp`:

```console
helm uninstall stack-data-swp
```

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://gitregistry.knut.univention.de/univention/customers/dataport/upx/common-helm/helm | common | ^0.3.0 |

## Values

<table>
	<thead>
		<th>Key</th>
		<th>Type</th>
		<th>Default</th>
		<th>Description</th>
	</thead>
	<tbody>
		<tr>
			<td>affinity</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>environment</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>fullnameOverride</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>image</td>
			<td>object</td>
			<td><pre lang="json">
{
  "imagePullPolicy": "Always",
  "registry": "gitregistry.knut.univention.de",
  "repository": "univention/customers/dataport/upx/stack-data/data-loader",
  "sha256": null,
  "tag": "latest"
}
</pre>
</td>
			<td>Container image configuration</td>
		</tr>
		<tr>
			<td>image.sha256</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td>Define image sha256 as an alternative to `tag`</td>
		</tr>
		<tr>
			<td>mountSecrets</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nodeSelector</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>podAnnotations</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>podSecurityContext</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>resources</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td>Will be mapped into the containers which run the import job as attribute "resources". See https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ .</td>
		</tr>
		<tr>
			<td>securityContext</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>stackDataContext</td>
			<td>object</td>
			<td><pre lang="json">
{
  "externalDomainName": "univention-organization.test",
  "externalMailDomain": "univention-organization.test",
  "ldapBase": "dc=univention-organization,dc=intranet",
  "oxDefaultContext": "10",
  "portalFileshareLinkBase": "https://fs.{{ .Values.stackDataContext.externalDomainName }}",
  "portalGroupwareLinkBase": "https://webmail.{{ .Values.stackDataContext.externalDomainName }}",
  "portalManagementKnowledgeLinkBase": "https://wiki.{{ .Values.stackDataContext.externalDomainName }}",
  "portalManagementProjectLinkBase": "https://project.{{ .Values.stackDataContext.externalDomainName }}",
  "portalRealtimeCollaborationLinkBase": "https://ucc.{{ .Values.stackDataContext.externalDomainName }}",
  "portalRealtimeVideoconferenceLinkBase": "https://jitsi.{{ .Values.stackDataContext.externalDomainName }}",
  "portalTitleDE": "Souveräner Arbeitsplatz",
  "portalTitleEN": "Sovereign Workplace",
  "portaltileGroupFileshare": [
    "cn=managed-by-attribute-Fileshare,cn=groups,{{ .Values.stackDataContext.ldapBase }}"
  ],
  "portaltileGroupGroupware": [
    "cn=managed-by-attribute-Groupware,cn=groups,{{ .Values.stackDataContext.ldapBase }}"
  ],
  "portaltileGroupLiveCollaboration": [
    "cn=managed-by-attribute-Livecollaboration,cn=groups,{{ .Values.stackDataContext.ldapBase }}"
  ],
  "portaltileGroupManagementKnowledge": [
    "cn=managed-by-attribute-Knowledgemanagement,cn=groups,{{ .Values.stackDataContext.ldapBase }}"
  ],
  "portaltileGroupManagementLearn": [
    "cn=managed-by-attribute-Learnmanagement,cn=groups,{{ .Values.stackDataContext.ldapBase }}"
  ],
  "portaltileGroupManagementProject": [
    "cn=managed-by-attribute-Projectmanagement,cn=groups,{{ .Values.stackDataContext.ldapBase }}"
  ],
  "portaltileGroupUserAdmin": [
    "cn=Domain Admins,cn=groups,{{ .Values.stackDataContext.ldapBase }}",
    "cn=Support,cn=groups,{{ .Values.stackDataContext.ldapBase }}"
  ],
  "portaltileGroupUserAll": [
    "cn=Domain Admins,cn=groups,{{ .Values.stackDataContext.ldapBase }}",
    "cn=Domain Users,cn=groups,{{ .Values.stackDataContext.ldapBase }}"
  ],
  "portaltileGroupUserStandard": [
    "cn=Domain Users,cn=groups,{{ .Values.stackDataContext.ldapBase }}"
  ]
}
</pre>
</td>
			<td>Context used for rendering the data files</td>
		</tr>
		<tr>
			<td>stackDataContext.portalTitleDE</td>
			<td>string</td>
			<td><pre lang="json">
"Souveräner Arbeitsplatz"
</pre>
</td>
			<td>Portal title (Deutsch)</td>
		</tr>
		<tr>
			<td>stackDataContext.portalTitleEN</td>
			<td>string</td>
			<td><pre lang="json">
"Sovereign Workplace"
</pre>
</td>
			<td>Portal title (English)</td>
		</tr>
		<tr>
			<td>stackDataSwp.dataConfigMapName</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td>The name of the ConfigMap to import the data from</td>
		</tr>
		<tr>
			<td>stackDataSwp.demoUsers</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td>An additional set of demo users, typically supplied in a seperate values file in the form: - username: dummy.user   firstname: Dummy   lastname: User   primaryGroupCN: Domain Users   password: secretPW</td>
		</tr>
		<tr>
			<td>stackDataSwp.dependencyUdmApiWait</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td>Wait for the udm-rest-api to be available</td>
		</tr>
		<tr>
			<td>stackDataSwp.loadDevData</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td>Load data which is useful during development (opt-in)</td>
		</tr>
		<tr>
			<td>stackDataSwp.udmApiPassword</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td>The password to access the UDM Rest API</td>
		</tr>
		<tr>
			<td>stackDataSwp.udmApiPasswordFile</td>
			<td>string</td>
			<td><pre lang="json">
"/run/secrets/univention.de/data-loader/udm_secret"
</pre>
</td>
			<td>The filename which contains the password</td>
		</tr>
		<tr>
			<td>stackDataSwp.udmApiUrl</td>
			<td>string</td>
			<td><pre lang="json">
"http://udm-rest-api/udm/"
</pre>
</td>
			<td>The URL by which the UDM Rest API can be reached</td>
		</tr>
		<tr>
			<td>stackDataSwp.udmApiUser</td>
			<td>string</td>
			<td><pre lang="json">
"cn=admin"
</pre>
</td>
			<td>The username to use to connect to the UDM Rest API</td>
		</tr>
		<tr>
			<td>tolerations</td>
			<td>list</td>
			<td><pre lang="json">
[]
</pre>
</td>
			<td></td>
		</tr>
	</tbody>
</table>

