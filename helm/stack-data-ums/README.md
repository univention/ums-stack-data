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
			<td>containerSecurityContext.allowPrivilegeEscalation</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td>Enable container privileged escalation.</td>
		</tr>
		<tr>
			<td>containerSecurityContext.capabilities</td>
			<td>object</td>
			<td><pre lang="json">
{
  "drop": [
    "ALL"
  ]
}
</pre>
</td>
			<td>Security capabilities for container.</td>
		</tr>
		<tr>
			<td>containerSecurityContext.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td>Enable security context.</td>
		</tr>
		<tr>
			<td>containerSecurityContext.readOnlyRootFilesystem</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td>Mounts the container's root filesystem as read-only.</td>
		</tr>
		<tr>
			<td>containerSecurityContext.runAsGroup</td>
			<td>int</td>
			<td><pre lang="json">
1000
</pre>
</td>
			<td>Process group id.</td>
		</tr>
		<tr>
			<td>containerSecurityContext.runAsNonRoot</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td>Run container as a user.</td>
		</tr>
		<tr>
			<td>containerSecurityContext.runAsUser</td>
			<td>int</td>
			<td><pre lang="json">
1000
</pre>
</td>
			<td>Process user id.</td>
		</tr>
		<tr>
			<td>containerSecurityContext.seccompProfile.type</td>
			<td>string</td>
			<td><pre lang="json">
"RuntimeDefault"
</pre>
</td>
			<td>Disallow custom Seccomp profile by setting it to RuntimeDefault.</td>
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
			<td>extensions</td>
			<td>list</td>
			<td><pre lang="json">
[]
</pre>
</td>
			<td>Extensions to load. This will override the configuration in `global.extensions`.</td>
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
			<td>global.configUcr</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.extensions</td>
			<td>list</td>
			<td><pre lang="json">
[]
</pre>
</td>
			<td>Allows to configure extensions globally.</td>
		</tr>
		<tr>
			<td>global.imagePullPolicy</td>
			<td>string</td>
			<td><pre lang="json">
"IfNotPresent"
</pre>
</td>
			<td>Define an ImagePullPolicy.  Ref.: https://kubernetes.io/docs/concepts/containers/images/#image-pull-policy </td>
		</tr>
		<tr>
			<td>global.imagePullSecrets</td>
			<td>list</td>
			<td><pre lang="json">
[]
</pre>
</td>
			<td>Credentials to fetch images from private registry. Ref: https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/  imagePullSecrets:   - "docker-registry"</td>
		</tr>
		<tr>
			<td>global.imageRegistry</td>
			<td>string</td>
			<td><pre lang="json">
"artifacts.software-univention.de"
</pre>
</td>
			<td>Container registry address.</td>
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
			<td>global.systemExtensions</td>
			<td>list</td>
			<td><pre lang="json">
[]
</pre>
</td>
			<td>Allows to configure system extensions globally.</td>
		</tr>
		<tr>
			<td>image</td>
			<td>object</td>
			<td><pre lang="json">
{
  "imagePullPolicy": "",
  "registry": "",
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
			<td>stackDataContext.domainname</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td>Domain name of the instance. Chart defaults to `univention-organization.intranet` Example: `"example.org"`</td>
		</tr>
		<tr>
			<td>stackDataContext.externalDomainName</td>
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
false
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
			<td>stackDataContext.portalFqdn</td>
			<td>string</td>
			<td><pre lang="json">
"portal.{{ include \"stack-data-ums.externalDomainName\" . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>stackDataContext.smtpHost</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td>Self-service emails: SMTP host</td>
		</tr>
		<tr>
			<td>stackDataContext.smtpPort</td>
			<td>int</td>
			<td><pre lang="json">
587
</pre>
</td>
			<td>Self-service emails: SMTP port (default: `587`)</td>
		</tr>
		<tr>
			<td>stackDataContext.smtpStartTls</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td>Self-service emails: SMTP via TLS (default: `true`)</td>
		</tr>
		<tr>
			<td>stackDataContext.smtpUser</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td>Self-service emails: SMTP username</td>
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
			<td>stackDataUms.logContext</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td>Enables logging of the template context used to render the template files.  Be aware that this may log sensitive information.</td>
		</tr>
		<tr>
			<td>stackDataUms.logTemplate</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td>Enables logging of the rendered templates for troubleshooting.  Be aware that this may log sensitive information.</td>
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
			<td>systemExtensions</td>
			<td>list</td>
			<td><pre lang="json">
[]
</pre>
</td>
			<td>Allows to configure the system extensions to load. This is intended for internal usage, prefer to use `extensions` for user configured extensions. This value will override the configuration in `global.systemExtensions`.</td>
		</tr>
		<tr>
			<td>templateContext</td>
			<td>object</td>
			<td><pre lang="json">
{
  "domainName": "{{ include \"stack-data-ums.domainName\" . }}",
  "enableDefaultLogin": "false",
  "externalMailDomain": "{{ include \"stack-data-ums.externalMailDomain\" . }}",
  "initialPasswordAdministrator": "{{ include \"stack-data-ums.initialPasswordAdministrator\" . }}",
  "initialPasswordSysIdpUser": "{{ include \"stack-data-ums.initialPasswordSysIdpUser\" . }}",
  "installUmcPolicies": false,
  "keycloakFqdn": "{{ include \"stack-data-ums.keycloakFqdn\" . }}",
  "ldapAdminDn": "{{ include \"stack-data-ums.ldapAdminDn\" . }}",
  "ldapBaseDn": "{{ include \"stack-data-ums.ldapBaseDn\" . }}",
  "ldapDomainName": "{{ include \"stack-data-ums.ldapDomainName\" . }}",
  "ldapHost": "{{ include \"stack-data-ums.ldapHost\" . }}",
  "ldapMasterHost": "{{ include \"stack-data-ums.ldapMasterHost\" . }}",
  "ldapMasterPort": "{{ include \"stack-data-ums.ldapMasterPort\" . }}",
  "ldapPort": "{{ include \"stack-data-ums.ldapPort\" . }}",
  "ldapUri": "{{ include \"stack-data-ums.ldapUri\" . }}",
  "loadDevData": true,
  "portalAuthMode": "{{ include \"stack-data-ums.portalAuthMode\" . }}",
  "portalFqdn": "{{ include \"stack-data-ums.portalFqdn\" . }}",
  "samlMetadataUrl": "{{ include \"stack-data-ums.samlMetadataUrl\" . }}",
  "samlMetadataUrlInternal": "{{ include \"stack-data-ums.samlMetadataUrlInternal\" . }}",
  "samlServiceProviders": "{{ include \"stack-data-ums.samlServiceProviders\" . }}",
  "subDomainsKeycloak": "{{ include \"stack-data-ums.subDomains.keycloak\" . }}",
  "subDomainsPortal": "{{ include \"stack-data-ums.subDomains.portal\" . }}",
  "udmApiCredentialSecretKey": "{{ include \"stack-data-ums.udmApi.credentialSecret.key\" . }}",
  "udmApiCredentialSecretName": "{{ include \"stack-data-ums.udmApi.credentialSecret.name\" . }}",
  "udmApiUrl": "{{ include \"stack-data-ums.udmApiUrl\" . }}",
  "umcMemcachedHostname": "{{ include \"stack-data-ums.umcMemcachedHostname\" . }}",
  "umcMemcachedUsername": "{{ include \"stack-data-ums.umcMemcachedUsername\" . }}",
  "umcPostgresqlDatabase": "{{ include \"stack-data-ums.umcPostgresqlDatabase\" . }}",
  "umcPostgresqlHostname": "{{ include \"stack-data-ums.umcPostgresqlHostname\" . }}",
  "umcPostgresqlPort": "{{ include \"stack-data-ums.umcPostgresqlPort\" . }}",
  "umcPostgresqlUsername": "{{ include \"stack-data-ums.umcPostgresqlUsername\" . }}",
  "umcSamlSchemes": "{{ include \"stack-data-ums.umcSamlSchemes\" . }}"
}
</pre>
</td>
			<td>Context used to render the data file templates in the data loader.</td>
		</tr>
		<tr>
			<td>templateContext.domainName</td>
			<td>string</td>
			<td><pre lang="json">
"{{ include \"stack-data-ums.domainName\" . }}"
</pre>
</td>
			<td>Domain name of the instance. Chart defaults to `univention-organization.intranet` Example: `"example.org"`</td>
		</tr>
		<tr>
			<td>templateContext.enableDefaultLogin</td>
			<td>string</td>
			<td><pre lang="json">
"false"
</pre>
</td>
			<td>Enable the default Portal login</td>
		</tr>
		<tr>
			<td>templateContext.externalMailDomain</td>
			<td>string</td>
			<td><pre lang="json">
"{{ include \"stack-data-ums.externalMailDomain\" . }}"
</pre>
</td>
			<td>Interim. The external mail domain in use. Currently required to create the Administrator account. Chart defaults to `univention-organization.test`.</td>
		</tr>
		<tr>
			<td>templateContext.initialPasswordAdministrator</td>
			<td>string</td>
			<td><pre lang="json">
"{{ include \"stack-data-ums.initialPasswordAdministrator\" . }}"
</pre>
</td>
			<td>The initial password of the user "Administrator".</td>
		</tr>
		<tr>
			<td>templateContext.initialPasswordSysIdpUser</td>
			<td>string</td>
			<td><pre lang="json">
"{{ include \"stack-data-ums.initialPasswordSysIdpUser\" . }}"
</pre>
</td>
			<td>The initial password of the user "sys-idp-user.</td>
		</tr>
		<tr>
			<td>templateContext.ldapBaseDn</td>
			<td>string</td>
			<td><pre lang="json">
"{{ include \"stack-data-ums.ldapBaseDn\" . }}"
</pre>
</td>
			<td>Base DN of the LDAP directory. Chart defaults to `dc=univention-organization,dc=intranet`. Example: `"dc=example,dc=org"`</td>
		</tr>
		<tr>
			<td>templateContext.ldapHost</td>
			<td>string</td>
			<td><pre lang="json">
"{{ include \"stack-data-ums.ldapHost\" . }}"
</pre>
</td>
			<td>Hostname of the LDAP server. Chart defaults to `ldap-server`. Example: `"ucs-1234.univention.intranet"`</td>
		</tr>
		<tr>
			<td>templateContext.ldapMasterHost</td>
			<td>string</td>
			<td><pre lang="json">
"{{ include \"stack-data-ums.ldapMasterHost\" . }}"
</pre>
</td>
			<td>Hostname of the primary LDAP server. Chart defaults to `ldap-server`. Example: `"ucs-1234.univention.intranet"`</td>
		</tr>
		<tr>
			<td>templateContext.ldapMasterPort</td>
			<td>string</td>
			<td><pre lang="json">
"{{ include \"stack-data-ums.ldapMasterPort\" . }}"
</pre>
</td>
			<td>Port to connect to the primary LDAP server. Chart defaults to `389`. Example: `389`</td>
		</tr>
		<tr>
			<td>templateContext.ldapPort</td>
			<td>string</td>
			<td><pre lang="json">
"{{ include \"stack-data-ums.ldapPort\" . }}"
</pre>
</td>
			<td>Port to connect to the LDAP server. Chart defaults to `389`. Example: `389`</td>
		</tr>
		<tr>
			<td>templateContext.loadDevData</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td>Load development data, such as test users.</td>
		</tr>
		<tr>
			<td>templateContext.portalAuthMode</td>
			<td>string</td>
			<td><pre lang="json">
"{{ include \"stack-data-ums.portalAuthMode\" . }}"
</pre>
</td>
			<td>The authentication method to use for the portal. Default is `saml`.</td>
		</tr>
		<tr>
			<td>templateContext.samlMetadataUrl</td>
			<td>string</td>
			<td><pre lang="json">
"{{ include \"stack-data-ums.samlMetadataUrl\" . }}"
</pre>
</td>
			<td>SAML Identity Provider metadata URL (as visible from the user/internet). Example: `"https://id.souvap.example.org/realms/ucs/protocol/saml/descriptor"`</td>
		</tr>
		<tr>
			<td>templateContext.samlMetadataUrlInternal</td>
			<td>string</td>
			<td><pre lang="json">
"{{ include \"stack-data-ums.samlMetadataUrlInternal\" . }}"
</pre>
</td>
			<td>SAML Identity Provider metadata URL (as visible from inside the container), optional. Example: `"http://keycloak:8080/realms/ucs/protocol/saml/descriptor"`</td>
		</tr>
		<tr>
			<td>templateContext.umcMemcachedHostname</td>
			<td>string</td>
			<td><pre lang="json">
"{{ include \"stack-data-ums.umcMemcachedHostname\" . }}"
</pre>
</td>
			<td>Hostname to use for memcached of the selfservice in UMC. This does set the UCR variable `umc/self-service/memcached/socket`. Chart default is `umc-server-memcached`.</td>
		</tr>
		<tr>
			<td>templateContext.umcMemcachedUsername</td>
			<td>string</td>
			<td><pre lang="json">
"{{ include \"stack-data-ums.umcMemcachedUsername\" . }}"
</pre>
</td>
			<td>Username to use for memcached of the selfservice in UMC. This does set the UCR variable `umc/self-service/memcached/username`. UCR has no default.</td>
		</tr>
		<tr>
			<td>templateContext.umcPostgresqlHostname</td>
			<td>string</td>
			<td><pre lang="json">
"{{ include \"stack-data-ums.umcPostgresqlHostname\" . }}"
</pre>
</td>
			<td>Hostname to use for postgresql of the selfservice in UMC. This does set the UCR variable `umc/self-service/postgresql/hostname`. UCR default is `localhost`. Chart default is `umc-server-postgresql`.</td>
		</tr>
		<tr>
			<td>templateContext.umcPostgresqlPort</td>
			<td>string</td>
			<td><pre lang="json">
"{{ include \"stack-data-ums.umcPostgresqlPort\" . }}"
</pre>
</td>
			<td>Port to use for postgresql of the selfservice in UMC. This does set the UCR variable `umc/self-service/postgresql/port`. UCR default is `5432`. Chart default is `5432`.</td>
		</tr>
		<tr>
			<td>templateContext.umcPostgresqlUsername</td>
			<td>string</td>
			<td><pre lang="json">
"{{ include \"stack-data-ums.umcPostgresqlUsername\" . }}"
</pre>
</td>
			<td>Username to use for postgresql of the selfservice in UMC. This does set the UCR variable `umc/self-service/postgresql/username`. UCR default is `selfservice`. Chart default is `selfservice`.</td>
		</tr>
		<tr>
			<td>templateContext.umcSamlSchemes</td>
			<td>string</td>
			<td><pre lang="json">
"{{ include \"stack-data-ums.umcSamlSchemes\" . }}"
</pre>
</td>
			<td>Which address scheme to consider for SAML ACS (string, comma-separated). Chart default is `https`. Example: `"https, http"`</td>
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

