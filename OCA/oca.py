import pyone
from pyone import OneException
from sys import argv
import re
from ascii import print_cat

### Your Authnetication parameters.

oneadmin = argv[1]
onepassword = argv[2]
one_fqdn = argv[3]

one_xmlrpc_url = str('http://' + one_fqdn + ':<<CHANGE ME>>/RPC2')
session = str(one_admin + ':' + one_password)

one = pyone.OneServer(one_xmlrpc_url, session=session)

#### define variables

alma_linux_name = '<<CHANGE ME>>'

#### main script body.



try:

    # Get default datastore ID
    datastores = one.datastorepool.info().DATASTORE
    image_datastore_id = [datastores[_].ID for _ in range(len(datastores)) if datastores[_].NAME == 'default' and datastores[_].TYPE == 0][0]

    # Get Alpine Linux image ID                
    marketplace_apps = one.marketapppool.info(-1, -1,-1).MARKETPLACEAPP
    marketplace_app_id = [marketplace_apps[_].ID for _ in range(len(marketplace_apps)) if marketplace_apps[_].NAME == alma_linux_name][0]

    # import the Alpine Linux to the default datastore.
    imported_alpine_linux = pyone.marketapp_export(one,marketplace_app_id,image_datastore_id)
    alma_linux_image_id = imported_alpine_linux['image']
    alma_linux_vmtemplate_id = imported_alpine_linux['vmtemplate']

except OneException as error:
    raise

### work with templates

try:
    template_settings = 'HYPERVISOR="kvm" NIC = [NETWORK = "private"] CONTEXT = [NETWORK="YES", TOKEN="yes", START_SCRIPT_BASE64="ZWNobyAkKGRhdGUpID4+IC9yb290L2RhdGUudHh0Cg==", PASSWORD="opennebula"]'

    one.template.update(alma_linux_vmtemplate_id,template_settings,1)

    one.template.instantiate(alma_linux_vmtemplate_id,'',False,'')

except OneException as error:
    raise

print_cat()