# stack-data-ums

A Helm chart to load the initial data into the UMS Stack

- **Version**: 0.1.0
- **Type**: application
- **Homepage:** <https://www.univention.de/>

## TL;DR

```console
helm upgrade --install stack-data-udm oci://gitregistry.knut.univention.de/univention/customers/dataport/upx/stack-data/helm/stack-data-udm
```

## Introduction

The chart does install Kubernetes Jobs to load the initial data of the UMS Stack.

It depends on a functional UDM Rest API being available and configured. The UDM
Rest API is used to load the data.

## Installing

To install the chart with the release name `stack-data-ums`:

```console
helm upgrade --install stack-data-udm oci://gitregistry.knut.univention.de/univention/customers/dataport/upx/stack-data/helm/stack-data-udm
```

## Uninstalling

To uninstall the chart with the release name `stack-data-udm`:

```console
helm uninstall stack-data-udm
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
			<td>additionalAnnotations</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td>Additional custom annotations to add to deployed objects.</td>
		</tr>
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
			<td>configMapUcr</td>
			<td>string</td>
			<td><pre lang="json">
"{{ include \"common.names.fullname\" . }}-ucr"
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
			<td>stackDataContext.domainname</td>
			<td>string</td>
			<td><pre lang="json">
"univention-organization.intranet"
</pre>
</td>
			<td>Domain name of the instance. Example: `"example.org"`</td>
		</tr>
		<tr>
			<td>stackDataContext.externalMailDomain</td>
			<td>string</td>
			<td><pre lang="json">
"univention-organization.test"
</pre>
</td>
			<td>Interim. The external mail domain in use. Currently required to create the Administrator account.</td>
		</tr>
		<tr>
			<td>stackDataContext.hostname</td>
			<td>string</td>
			<td><pre lang="json">
"portal"
</pre>
</td>
			<td>Host name of the instance. Example: `"souvap"`</td>
		</tr>
		<tr>
			<td>stackDataContext.idpFqdn</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td>The FQDN of the identity provider (w/o the protocol specification). Example: `"id.souvap.example.org"`</td>
		</tr>
		<tr>
			<td>stackDataContext.idpSamlMetadataUrl</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td>SAML Identity Provider metadata URL (as visible from the user/internet). Example: `"https://id.souvap.example.org/realms/ucs/protocol/saml/descriptor"`</td>
		</tr>
		<tr>
			<td>stackDataContext.idpSamlMetadataUrlInternal</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td>SAML Identity Provider metadata URL (as visible from inside the container), optional. Example: `"http://keycloak:8080/realms/ucs/protocol/saml/descriptor"`</td>
		</tr>
		<tr>
			<td>stackDataContext.initialPasswordAdministrator</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td>The initial password of the user "Administrator".</td>
		</tr>
		<tr>
			<td>stackDataContext.initialPasswordSysIdpUser</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td>The initial password of the user "sys-idp-user.</td>
		</tr>
		<tr>
			<td>stackDataContext.installUmcPolicies</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td>This parameter allows to skip the installation of the default UMC policies if set to "false".</td>
		</tr>
		<tr>
			<td>stackDataContext.ldapBase</td>
			<td>string</td>
			<td><pre lang="json">
"dc=univention-organization,dc=intranet"
</pre>
</td>
			<td>Base DN of the LDAP directory. Example: `"dc=example,dc=org"`</td>
		</tr>
		<tr>
			<td>stackDataContext.ldapHost</td>
			<td>string</td>
			<td><pre lang="json">
"ldap-server"
</pre>
</td>
			<td>Hostname of the LDAP server. Example: `"ucs-1234.univention.intranet"`</td>
		</tr>
		<tr>
			<td>stackDataContext.ldapHostDn</td>
			<td>string</td>
			<td><pre lang="json">
"cn=admin,dc=univention-organization,dc=intranet"
</pre>
</td>
			<td>DN of the UMS instance. Example: `"cn=ucs-1234,cn=dc,cn=computers,dc=example,dc=org"`</td>
		</tr>
		<tr>
			<td>stackDataContext.ldapPort</td>
			<td>int</td>
			<td><pre lang="json">
389
</pre>
</td>
			<td>Port to connect to the LDAP server. Example: `389`</td>
		</tr>
		<tr>
			<td>stackDataContext.ldapSamlSpUrls</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td>List of SAML Service Provider URLs which the LDAP server should trust (comma-separated). Example: `"https://portal.souvap.example.org/univention/saml/metadata"`</td>
		</tr>
		<tr>
			<td>stackDataContext.umcMemcachedHostname</td>
			<td>string</td>
			<td><pre lang="json">
"umc-server-memcached"
</pre>
</td>
			<td>Hostname to use for memcached of the selfservice in UMC. This does set the UCR variable `umc/self-service/memcached/socket`.</td>
		</tr>
		<tr>
			<td>stackDataContext.umcPostgresqlHostname</td>
			<td>string</td>
			<td><pre lang="json">
"umc-server-postgresql"
</pre>
</td>
			<td>Hostname to use for postgresql of the selfservice in UMC. This does set the UCR variable `umc/self-service/postgresql/hostname`.</td>
		</tr>
		<tr>
			<td>stackDataContext.umcSamlSchemes</td>
			<td>string</td>
			<td><pre lang="json">
"https"
</pre>
</td>
			<td>Which address scheme to consider for SAML ACS (string, comma-separated). Example: `"https, http"`</td>
		</tr>
		<tr>
			<td>stackDataContext.umcSamlSpFqdn</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td>SAML Service Provider hostname (FQDN of the UMC, which is the service provider) Example: `"portal.souvap.example.org"`</td>
		</tr>
		<tr>
			<td>stackDataUms.dependencyUdmApiWait</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td>Wait for the udm-rest-api to be available</td>
		</tr>
		<tr>
			<td>stackDataUms.loadDevData</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td>Load data which is useful during development (opt-in)</td>
		</tr>
		<tr>
			<td>stackDataUms.udmApiPassword</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td>The password to access the UDM Rest API</td>
		</tr>
		<tr>
			<td>stackDataUms.udmApiPasswordFile</td>
			<td>string</td>
			<td><pre lang="json">
"/run/secrets/univention.de/data-loader/udm_secret"
</pre>
</td>
			<td>The filename which contains the password</td>
		</tr>
		<tr>
			<td>stackDataUms.udmApiUrl</td>
			<td>string</td>
			<td><pre lang="json">
"http://udm-rest-api/udm/"
</pre>
</td>
			<td>The URL by which the UDM Rest API can be reached</td>
		</tr>
		<tr>
			<td>stackDataUms.udmApiUser</td>
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

