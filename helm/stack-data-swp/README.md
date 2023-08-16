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
| oci://gitregistry.knut.univention.de/univention/customers/dataport/upx/common-helm/helm | common | ^0.2.0 |

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
			<td>securityContext</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
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
