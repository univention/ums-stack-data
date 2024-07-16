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
			<td>global.nubusDeployment</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td>Indicates wether this chart is part of a Nubus deployment.</td>
		</tr>
		<tr>
			<td>image</td>
			<td>object</td>
			<td><pre lang="json">
{
  "imagePullPolicy": "IfNotPreset",
  "registry": "artifacts.software-univention.de",
  "repository": "nubus-dev/images/data-loader",
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
""
</pre>
</td>
			<td>Domain name of the instance. Chart defaults to `univention-organization.intranet` Example: `"example.org"`</td>
		</tr>
		<tr>
			<td>stackDataContext.externalMailDomain</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td>Interim. The external mail domain in use. Currently required to create the Administrator account. Chart defaults to `univention-organization.test`.</td>
		</tr>
		<tr>
			<td>stackDataContext.hostname</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td>Host name of the instance. Chart defaults to `portal`. Example: `"souvap"`</td>
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
""
</pre>
</td>
			<td>Base DN of the LDAP directory. Chart defaults to `dc=univention-organization,dc=intranet`. Example: `"dc=example,dc=org"`</td>
		</tr>
		<tr>
			<td>stackDataContext.ldapHost</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td>Hostname of the LDAP server. Chart defaults to `ldap-server`. Example: `"ucs-1234.univention.intranet"`</td>
		</tr>
		<tr>
			<td>stackDataContext.ldapHostDn</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td>DN of the UMS instance. Chart defaults to `cn=admin,dc=univention-organization,dc=intranet`. Example: `"cn=ucs-1234,cn=dc,cn=computers,dc=example,dc=org"`</td>
		</tr>
		<tr>
			<td>stackDataContext.ldapMasterHost</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td>Hostname of the primary LDAP server. Chart defaults to `ldap-server`. Example: `"ucs-1234.univention.intranet"`</td>
		</tr>
		<tr>
			<td>stackDataContext.ldapMasterPort</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td>Port to connect to the primary LDAP server. Chart defaults to `389`. Example: `389`</td>
		</tr>
		<tr>
			<td>stackDataContext.ldapPort</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td>Port to connect to the LDAP server. Chart defaults to `389`. Example: `389`</td>
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
			<td>stackDataContext.portalAuthMode</td>
			<td>string</td>
			<td><pre lang="json">
"saml"
</pre>
</td>
			<td>The authentication method to use for the portal. Default is `saml`.</td>
		</tr>
		<tr>
			<td>stackDataContext.umcHtmlTitle</td>
			<td>string</td>
			<td><pre lang="json">
"Nubus Management Console"
</pre>
</td>
			<td>UMC web page title. Chart supports templated values.</td>
		</tr>
		<tr>
			<td>stackDataContext.umcMemcachedHostname</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td>Hostname to use for memcached of the selfservice in UMC. This does set the UCR variable `umc/self-service/memcached/socket`. Chart default is `umc-server-memcached`.</td>
		</tr>
		<tr>
			<td>stackDataContext.umcMemcachedUsername</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td>Username to use for memcached of the selfservice in UMC. This does set the UCR variable `umc/self-service/memcached/username`. UCR has no default.</td>
		</tr>
		<tr>
			<td>stackDataContext.umcPostgresqlDatabase</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>stackDataContext.umcPostgresqlHostname</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td>Hostname to use for postgresql of the selfservice in UMC. This does set the UCR variable `umc/self-service/postgresql/hostname`. UCR default is `localhost`. Chart default is `umc-server-postgresql`.</td>
		</tr>
		<tr>
			<td>stackDataContext.umcPostgresqlPort</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td>Port to use for postgresql of the selfservice in UMC. This does set the UCR variable `umc/self-service/postgresql/port`. UCR default is `5432`. Chart default is `5432`.</td>
		</tr>
		<tr>
			<td>stackDataContext.umcPostgresqlUsername</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td>Username to use for postgresql of the selfservice in UMC. This does set the UCR variable `umc/self-service/postgresql/username`. UCR default is `selfservice`. Chart default is `selfservice`.</td>
		</tr>
		<tr>
			<td>stackDataContext.umcSamlSchemes</td>
			<td>string</td>
			<td><pre lang="json">
"https"
</pre>
</td>
			<td>Which address scheme to consider for SAML ACS (string, comma-separated). Chart default is `https`. Example: `"https, http"`</td>
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
			<td>stackDataUms.logContext</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td>Enables logging of the template context used to render the template files.  Be aware that this may log sensitive information.</td>
		</tr>
		<tr>
			<td>stackDataUms.udmApiPassword</td>
			<td>string</td>
			<td><pre lang="json">
""
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
""
</pre>
</td>
			<td>The URL by which the UDM Rest API can be reached. Chart defaults to `http://udm-rest-api/udm/`. Nubus defaults to `http://$RELEASE_NAME-udm-rest-api/udm/`.</td>
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

