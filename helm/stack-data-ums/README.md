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

It depends on a functional UDM REST API being available and configured. The UDM
REST API is used to load the data.

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
| oci://artifacts.software-univention.de/nubus/charts | nubus-common | 0.28.0 |

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
			<td>containerSecurityContext.privileged</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
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
			<td>dataLoader.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td>Allows to disable the data loader Job.</td>
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
			<td>extraEnvVars</td>
			<td>list</td>
			<td><pre lang="json">
[]
</pre>
</td>
			<td>Array with extra environment variables to add to containers.  extraEnvVars:   - name: FOO     value: "bar"</td>
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
null
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
			<td>global.postgresql.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.postgresql.connection.port</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td></td>
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
			<td>global.udm.connection.url</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td>Global default for the URL via which the UDM REST API can be reached. See "udm.connection.url".</td>
		</tr>
		<tr>
			<td>image</td>
			<td>object</td>
			<td><pre lang="json">
{
  "pullPolicy": "",
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
			<td>nubusUmcServer.host</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td>Hostname of the UMC server used to disable self-service rate-limiting for requests from inside the cluster This does set the UCR variable `umc/self-service/rate-limit/trusted-hosts`</td>
		</tr>
		<tr>
			<td>nubusUmcServer.memcached.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td>Username to use for memcached of the selfservice in UMC. This does set the UCR variable `umc/self-service/memcached/username`. UCR has no default.</td>
		</tr>
		<tr>
			<td>nubusUmcServer.memcached.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td>Hostname to use for memcached of the selfservice in UMC. This does set the UCR variable `umc/self-service/memcached/socket`.</td>
		</tr>
		<tr>
			<td>nubusUmcServer.postgresql.auth.database</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.postgresql.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td>Username to use for postgresql of the selfservice in UMC. This does set the UCR variable `umc/self-service/postgresql/username`. UCR default is `selfservice`.</td>
		</tr>
		<tr>
			<td>nubusUmcServer.postgresql.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td>Hostname to use for postgresql of the selfservice in UMC. This does set the UCR variable `umc/self-service/postgresql/hostname`. UCR default is `localhost`.</td>
		</tr>
		<tr>
			<td>nubusUmcServer.postgresql.connection.port</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td>Port to use for postgresql of the selfservice in UMC. This does set the UCR variable `umc/self-service/postgresql/port`. UCR default is `5432`.</td>
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
			<td>serviceAccount.annotations</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>serviceAccount.automountServiceAccountToken</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>serviceAccount.create</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>serviceAccount.labels</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td>Additional custom labels for the ServiceAccount.</td>
		</tr>
		<tr>
			<td>serviceAccount.name</td>
			<td>string</td>
			<td><pre lang="json">
""
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
			<td>stackDataContext.idpOidcIssuerUrl</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td>OIDC Identity Provider issuer URL (as visible from the user/internet). Example: `"https://id.souvap.example.org/realms/ucs"`</td>
		</tr>
		<tr>
			<td>stackDataContext.idpOidcIssuerUrlInternal</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td>OIDC Identity Provider issuer URL (as visible from inside the container), optional. Example: `"http://keycloak:8080/realms/ucs"`</td>
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
"oidc"
</pre>
</td>
			<td>The authentication method to use for the portal. Default is `oidc`.</td>
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
			<td>stackDataContext.showUmc</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td>Default portal show UMC modules</td>
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
"Univention Portal"
</pre>
</td>
			<td>UMC web page title. Chart supports templated values.</td>
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
			<td>stackDataUms.extraDataFiles</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td>Allow to configure additional data files. This has to be a map from the desired filename to the content. The content has to be a valid YAML stream which the data loader is able to process.</td>
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
			<td>stackDataUms.udmApiPort</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td>The internal port on which the UDM REST API is listening in the Kubernetes Pod. Chart defaults to `9979`.</td>
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
  "enableDefaultLogin": "{{ include \"stack-data-ums.enableDefaultLogin\" . }}",
  "externalMailDomain": "{{ include \"stack-data-ums.externalMailDomain\" . }}",
  "initialPasswordAdministrator": null,
  "keycloakTwofaGroup": "2FA Users",
  "ldapBaseDn": "{{ include \"stack-data-ums.ldapBaseDn\" . }}",
  "readonlyUserPassword": null,
  "showUmc": "{{ include \"stack-data-ums.showUmc\" . }}",
  "subDomainsKeycloak": "{{ include \"stack-data-ums.subDomains.keycloak\" . }}",
  "svcPortalServerUserPassword": null
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
"{{ include \"stack-data-ums.enableDefaultLogin\" . }}"
</pre>
</td>
			<td>Enable the plain UMC login. Enabling it will show the UMC login tile. This value is also controlled globally, which will cause the ingress to be disabled as well. Enabling it here will show the UMC login tile, but will not enable the ingress path. Example: `false`</td>
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
null
</pre>
</td>
			<td>The initial password of the user "Administrator".  A random password will be generated if unset.</td>
		</tr>
		<tr>
			<td>templateContext.keycloakTwofaGroup</td>
			<td>string</td>
			<td><pre lang="json">
"2FA Users"
</pre>
</td>
			<td>Creates the group needed for enforcing configuration of a second factor in Keycloak.</td>
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
			<td>templateContext.readonlyUserPassword</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td>The password for the Keycloak service readonly user  A random password will be generated if unset.</td>
		</tr>
		<tr>
			<td>templateContext.svcPortalServerUserPassword</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td>The password for the Portal service user  A random password will be generated if unset.</td>
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
		<tr>
			<td>udm.auth.existingSecret.keyMapping.password</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>udm.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>udm.auth.password</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>udm.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"cn=admin"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>udm.connection.url</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td>The URL by which the UDM REST API can be reached. Default `http://udm-rest-api/udm/`.</td>
		</tr>
	</tbody>
</table>

