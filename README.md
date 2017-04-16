# php-update-all-projects
Simple command line tool to update all PHP projects. The tool is writen in Python3

If you are working a lot of php projects and If you want to pull lastest commits and intall lastest library for each projects by calling only one command. This command tool can save your time to do all of it.

## How to use
You think there are projects is in one directory like this.

```sh
/Users/mahmut/Code/Acme/
├── acme-account
├── acme-acquirer
├── acme-acquirer-creditcard
├── acme-acquirerreference
├── acme-admin-ui
├── acme-api
├── acme-banking
├── acme-chargeback
├── acme-client
├── acme-conf
├── acme-dump
├── acme-fraud
├── acme-fx
├── acme-helper
├── acme-integration-tests
├── acme-mahmut
├── acme-merchant
├── acme-merchant-ui
├── acme-notification
├── acme-payment-ui
├── acme-reporting
├── acme-reporting-api
├── acme-tokenization
```

```sh
$./up-all.py -p /Users/mahmut/Code/Acme/

```
Now shell scripts works asynchronously for each projects.

## Requiretments
Todo
